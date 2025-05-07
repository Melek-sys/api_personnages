from fastapi import FastAPI
from pydantic import BaseModel
import json
from pathlib import Path

# Initialize the application
app = FastAPI()

# ---------------------- Data Model ----------------------

# Model for characters received via webhook
class WebhookCharacter(BaseModel):
    nom: str
    score: int

# ---------------------- File Paths ----------------------

# JSON file to log characters
log_file = Path(__file__).parent / "webhook_log.json"

# Text file to simulate a notification
notif_file = Path(__file__).parent / "notifications.txt"

# If the JSON file does not exist, create it empty
if not log_file.exists():
    with open(log_file, "w", encoding="utf-8") as f:
        json.dump([], f)

# ---------------------- Webhook Route ----------------------

@app.post("/webhook/personnage")
async def receive_character(data: WebhookCharacter):
    # Determine the level based on the score
    niveau = "élite" if data.score >= 90 else "standard"

    # Create the complete event
    evenement = {
        "nom": data.nom,
        "score": data.score,
        "niveau": niveau
    }

    # 🔹 Step 1: Record in webhook_log.json
    with open(log_file, "r", encoding="utf-8") as f:
        historique = json.load(f)
    historique.append(evenement)
    with open(log_file, "w", encoding="utf-8") as f:
        json.dump(historique, f, indent=2, ensure_ascii=False)

    # 🔹 Step 2: Write a notification line in notifications.txt
    message = f"⚡ Notification : {data.nom} ({niveau}) ajouté avec score {data.score}\n"
    with open(notif_file, "a", encoding="utf-8") as f:
        f.write(message)

    # Display in the console
    print(f"📥 Webhook received: {evenement}")
    print(message.strip())

    # Response sent back to the sender
    return {
        "status": "ok",
        "message": "Character recorded and notification sent",
        "data": evenement
    }
