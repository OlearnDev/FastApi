from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI(title="API TODO", version="v1")

class Todo (BaseModel):
    name: str
    due_date: str
    description: str
    
store_todo= []

@app.get("/")
async def home() :
	return {"hello": "world"}


@app.post("/todo")
async def create_todo(todo:Todo):
    store_todo.append(todo)
    return todo