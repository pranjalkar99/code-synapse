from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import HTMLResponse

from fastapi import FastAPI
from typing import List
import json

from pydantic import BaseModel
import uvicorn


with open('json/test.json') as f:
    data = json.load(f)


app = FastAPI()

@app.get("/")
async def form_post():
    html_content = """
    <form method="post" enctype="multipart/form-data">
    <input name="file" type="file">
    <input type="submit">
    </form>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.post("/")
async def form_post(file: UploadFile = File(...), name: str = Form(...)):
    return {"file_name": file.filename, "name": name}

@app.get('/data')
async def get_data():
    return data



class Element(BaseModel):
    id: str
    x: int
    y: int
    width: int
    height: int

class Text(BaseModel):
    element_id: str
    x: int
    y: int
    value: str

class Data(BaseModel):
    elements: List[Element]
    text: List[Text]


@app.post('/data')
async def create_data(data: Data):
    return data


if __name__ == '__main__':
    uvicorn.run(app, port=8000)
