from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(SessionMiddleware, secret_key="your_secret_key")

templates = Jinja2Templates(directory="templates")

#Task1: 首頁
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

#Task2: 驗證機制
@app.post("/signin")
def signin(request: Request, username: str = Form(""), password: str = Form("")):
    if not username or not password:
        return RedirectResponse(url="/error?message=請輸入帳號和密碼", status_code=303)
    
    if username == "test" and password == "test":
        request.session["SIGNED-IN"] = True
        return RedirectResponse(url="/member", status_code=303)
    
    return RedirectResponse(url="/error?message=帳號、或密碼輸入錯誤", status_code=303)

@app.get("/member")
def member(request: Request):
    if not request.session.get("SIGNED-IN"):
        return RedirectResponse(url="/", status_code=303)
    return templates.TemplateResponse("success.html", {"request": request})

@app.get("/error")
def error(request: Request, message: str):
    return templates.TemplateResponse("error.html", {"request": request, "message": message})

#Task3: 會員狀態管理
@app.get("/signout")
def signout(request: Request):
    request.session["SIGNED-IN"] = False
    return RedirectResponse(url="/", status_code=303)

#Task4: 平方計算
@app.get("/square/{number}")
def square(request: Request, number: int):
    squared = number ** 2
    return templates.TemplateResponse("square.html", {"request": request, "number": number, "squared": squared})