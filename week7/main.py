from fastapi import FastAPI, Form, Request, Query, HTTPException
from fastapi.responses import RedirectResponse,JSONResponse
from starlette.middleware.sessions import SessionMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import mysql.connector
from dotenv import load_dotenv
import os
from pydantic import BaseModel

load_dotenv()


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY"))
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

@app.get("/error")
def error(request: Request, message: str):
    return templates.TemplateResponse("error.html", {"request": request, "message": message})

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

#登出會員
@app.get("/signout")
def signout(request: Request):
    request.session["SIGNED-IN"] = False
    return RedirectResponse(url="/", status_code=303)

#會員查詢
@app.get("/api/member")
def get_member(username: str = Query(..., description="要查詢的會員帳號")):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name, username FROM member WHERE username = %s", (username,))
    member = cursor.fetchone()
    cursor.close()
    conn.close()

    if member:
        return JSONResponse(content={"data": member})
    return JSONResponse(content={"data": None})

#更新會員名
class UpdateNameRequest(BaseModel):
    name: str

@app.patch("/api/member")
async def update_username(request: Request, update_data: UpdateNameRequest):
    if not request.session.get("SIGNED-IN"):
        return JSONResponse(content={"error": True})

    user_id = request.session["USER-ID"] 
    new_name = update_data.name

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE member SET name = %s WHERE id = %s", (new_name, user_id))
    conn.commit()
    cursor.close()
    conn.close()

    request.session["USER-NAME"] = new_name
    return {"ok": True}