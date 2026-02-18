# ==========================================================
# Save/load JSON files, cloud-ready paths
# ==========================================================

import json
import os

SAVE_FILE = "phase_dot_save.json"

DEFAULT_SAVE = {
    "unlocked_skins": [0],  # Start with first skin
    "high_score": 0,
    "recent_scores": []     # Store last 10 scores
}

def load_save():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    else:
        return DEFAULT_SAVE.copy()

def save_progress(data):
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def update_score(score):
    """
    Update the high score if current score is higher.
    Also append to recent_scores list.
    """
    data = load_save()
    
    if score > data.get("high_score", 0):
        data["high_score"] = score
    
    # Keep a rolling list of last 10 scores
    recent = data.get("recent_scores", [])
    recent.append(score)
    if len(recent) > 10:
        recent = recent[-10:]
    data["recent_scores"] = recent
    
    save_progress(data)