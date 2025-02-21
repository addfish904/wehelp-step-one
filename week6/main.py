from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="apple3361858",
        database="website"
    )

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(SessionMiddleware, secret_key="your_secret_key")
templates = Jinja2Templates(directory="templates")

#首頁
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

#註冊會員
@app.post("/signup")
def signup(request: Request, name: str = Form(""), username: str = Form(""), password: str = Form("")):
    if not name or not username or not password:
        return RedirectResponse(url="/error?message=請填寫所有欄位", status_code=303)
    
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM member WHERE username = %s", (username,))
    if cursor.fetchone():
        cursor.close()
        conn.close()
        return RedirectResponse(url="/error?message=帳號已被使用", status_code=303)
    
    cursor.execute("INSERT INTO member (name, username, password) VALUES (%s, %s, %s)", (name, username, password))
    conn.commit()
    cursor.close()
    conn.close()
    return RedirectResponse(url="/", status_code=303)

#登入驗證
@app.post("/signin")
def signin(request: Request, name:str = Form(""), username: str = Form(""), password: str = Form("")):
    if not username or not password:
        return RedirectResponse(url="/error?message=請輸入帳號和密碼", status_code=303)
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name FROM member WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if user:
        request.session["SIGNED-IN"] = True
        request.session["USER-ID"] = user["id"]
        request.session["USER-NAME"] = user["name"]
        return RedirectResponse(url="/member", status_code=303)
    else:
        return RedirectResponse(url="/error?message=帳號或密碼錯誤", status_code=303)


@app.get("/member")
def member(request: Request):
    if not request.session.get("SIGNED-IN"):
        return RedirectResponse(url="/", status_code=303)

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT message.id, message.content, member.name FROM message JOIN member ON message.member_id = member.id ORDER BY message.id DESC")
    messages = cursor.fetchall()

    cursor.close()
    conn.close()
    
    return templates.TemplateResponse("success.html", {
        "request": request,
        "name": request.session["USER-NAME"],
        "messages": messages
    })


@app.get("/error")
def error(request: Request, message: str):
    return templates.TemplateResponse("error.html", {"request": request, "message": message})

#登出會員
@app.get("/signout")
def signout(request: Request):
    request.session["SIGNED-IN"] = False
    return RedirectResponse(url="/", status_code=303)

#發布留言
@app.post("/CreateMessage")
def create_message(request: Request, content: str = Form("")):
    if not request.session.get("SIGNED-IN"):
        return RedirectResponse(url="/", status_code=303)
    
    user_id = request.session["USER-ID"]
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO message (member_id, content) VALUES (%s, %s)", (user_id, content))
    conn.commit()
    cursor.close()
    conn.close()
    return RedirectResponse(url="/member", status_code=303)

#刪除留言
@app.post("/DeleteMessage")
def delete_message(request: Request, message_id: int = Form(...)):
    if not request.session.get("SIGNED-IN"):
        return RedirectResponse(url="/", status_code=303)
    
    user_id = request.session["USER-ID"]
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM message WHERE id = %s AND member_id = %s", (message_id, user_id))
    conn.commit()
    cursor.close()
    conn.close()
    return RedirectResponse(url="/member", status_code=303)