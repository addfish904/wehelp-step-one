from fastapi import FastAPI, Form, Request, Depends
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# 設定 SessionMiddleware（管理使用者登入狀態）
app.add_middleware(SessionMiddleware, secret_key="your_secret_key")

templates = Jinja2Templates(directory="templates")

#Task 1: 首頁 (Home Page)
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

#Task 2: 驗證機制 (Login Verification)
@app.post("/signin")
def signin(request: Request, username: str = Form(""), password: str = Form("")):
    if not username or not password:
        return RedirectResponse(url="/error?message=Please enter username and password", status_code=303)
    
    if username == "test" and password == "test":
        request.session["SIGNED-IN"] = True
        return RedirectResponse(url="/member", status_code=303)
    
    return RedirectResponse(url="/error?message=帳號、或密碼輸入錯誤", status_code=303)

# 🔹 Task 2: 成功與錯誤頁面
@app.get("/member")
def member(request: Request):
    if not request.session.get("SIGNED-IN"):
        return RedirectResponse(url="/", status_code=303)
    return templates.TemplateResponse("success.html", {"request": request})

@app.get("/error")
def error(request: Request, message: str):
    return templates.TemplateResponse("error.html", {"request": request, "message": message})

# 🔹 Task 3: 登出功能
@app.get("/signout")
def signout(request: Request):
    request.session["SIGNED-IN"] = False
    return RedirectResponse(url="/", status_code=303)

# 🔹 Task 4: Path Parameter（平方計算）
@app.get("/square/{number}")
def square(request: Request, number: int):
    squared = number ** 2
    return templates.TemplateResponse("square.html", {"request": request, "number": number, "squared": squared})