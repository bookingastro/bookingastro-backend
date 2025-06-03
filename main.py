from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os

# Initialize app
app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# === Models ===

class UserInput(BaseModel):
    name: str
    dob: str
    time: str
    place: str

class ChartData(BaseModel):
    numerology: dict
    horoscope: dict

# === Routes ===

@app.post("/api/analyze")
def analyze_chart(data: UserInput):
    # Dummy numerology + horoscope values
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
async def interpret_chart(data: ChartData):
    prompt = f"Interpret this data astrologically:\n{data.dict()}"
    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return {"message": response.choices[0].message.content}
    except Exception as e:
        return {"message": f"Interpretation error: {str(e)}"}
