from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

openai.api_key = os.getenv("OPENAI_API_KEY")

class UserInput(BaseModel):
    name: str
    dob: str
    time: str
    place: str

@app.post("/api/analyze")
def analyze_chart(data: UserInput):
    return {
        "numerology": {
            "life_path": "7",
            "expression": "5",
            "soul_urge": "2"
        },
        "horoscope": {
            "Sun": 102.5,
            "Moon": 220.3,
            "Mars": 45.7
        }
    }

@app.post("/api/interpret")
async def interpret_chart(request: Request):
    data = await request.json()
    prompt = f"Interpret this data astrologically:\n{data}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"message": response['choices'][0]['message']['content']}