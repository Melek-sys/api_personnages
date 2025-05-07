# Import necessary modules
import json  # For reading and writing JSON files
from pathlib import Path  # For handling file paths
from typing import List  # To declare a typed list

from fastapi import (FastAPI, Header,  # FastAPI and security via Header
                     HTTPException)
from fastapi.middleware.cors import CORSMiddleware  # To allow frontend calls
from pydantic import BaseModel  # For data models (validation)

# Create the FastAPI application
app = FastAPI()

# ---------------------- CORS ----------------------

# Origins allowed to call the API (e.g., React frontend, local HTML file...)
origins = [
    "http://localhost:3000",       # For local React frontend
    "http://127.0.0.1:5500",       # For Live Server on VSCode
    "file://"                      # For locally opened HTML page
]

# Enable CORS management in the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # Allow these domains
    allow_credentials=True,
    allow_methods=["*"],          # Allow all methods (GET, POST, etc.)
    allow_headers=["*"]           # Allow all headers (including "token")
)

# ---------------------- Models ----------------------

# Pydantic model for a character (GET)
class Character(BaseModel):
    id: int
    nom: str
    equipe: str

# Pydantic model for a score (POST)
class Score(BaseModel):
    name: str
    city: str
    avis: str

# ---------------------- Loading or Creating JSON ----------------------

# Path to the JSON file containing the characters
path = Path(__file__).parent / "personnages.json"

# If the file does not exist, create it automatically with two characters
if not path.exists():
    print("⚠️ File personnages.json not found. Creating automatically...")
    example_characters = [
        {"id": 1, "nom": "Olivier Atton", "equipe": "Nankatsu"},
        {"id": 2, "nom": "Thomas Price", "equipe": "Nankatsu"}
    ]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(example_characters, f, ensure_ascii=False, indent=2)

# Read the JSON file (now definitely present)
with open(path, "r", encoding="utf-8") as f:
    personnages = [Character(**p) for p in json.load(f)]

# ---------------------- Endpoints ----------------------

# ✅ Endpoint GET /personnages (protected by a token)
@app.get("/personnages", response_model=List[Character])
def get_characters(token: str = Header(...)):
    # Token verification
    if token != "SECRET123":
        raise HTTPException(status_code=401, detail="Invalid token")
    # Return the list of characters
    return personnages

# ✅ Endpoint POST /scores (receives a score and logs it to the console)
@app.post("/scores")
def post_scores(score: Score, token: str = Header(...)):
    # Token verification
    if token != "SECRET123":
        raise HTTPException(status_code=401, detail="Invalid token")

    # Display the received score in the console
    print(f"✅ Score received: {score}")

    # Return a confirmation message
    return {"message": "Score received", "data": score}
