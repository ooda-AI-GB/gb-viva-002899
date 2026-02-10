from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory=".")

# In-memory storage for tasks
tasks = []

@app.get("/health", response_class=HTMLResponse)
async def health_check():
    return "OK"

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})

@app.post("/add_task", response_class=HTMLResponse)
async def add_task(request: Request, task: str = Form(...)):
    tasks.append(task)
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
