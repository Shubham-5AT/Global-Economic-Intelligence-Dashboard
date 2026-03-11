from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import pandas as pd
app = FastAPI()
templates = Jinja2Templates(directory="templates")
df = pd.read_csv("data/cleaned_data.csv")
@app.get("/")
def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
@app.get("/data")
def get_data():
    return df.to_dict(orient="records")