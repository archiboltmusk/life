#!/usr/bin/env python3
import os
import sys
import json
import urllib.request
import urllib.parse
from datetime import datetime, timezone, timedelta

# IST is UTC + 5:30
IST = timezone(timedelta(hours=5, minutes=30))
now_ist = datetime.now(IST)

# Calculations
date_str = now_ist.strftime("%A, %b %d, %Y")
marrow_expiry = datetime(2027, 1, 16, tzinfo=IST)
days_to_marrow = (marrow_expiry - now_ist).days

# Janma Shani peak lifts in early 2027 (Saturn shifts to Pisces)
transit_target = datetime(2027, 2, 23, tzinfo=IST)
days_to_peak_lift = (transit_target - now_ist).days

# Rotating daily high-yield focus
anchors = [
    ("Medicine / Pharmacology", "Rapid Review 1 module + 25 MCQs. Focus on accuracy over speed."),
    ("Pathology / Microbiology", "High-yield image flashcards + 25 MCQs. Look at patterns, not memorization."),
    ("Surgery / Obstetrics", "Procedural anatomy & clinical vignettes. Hand-eye visualization."),
    ("Biochemistry / Physiology", "High-yield cycles & clinical correlations. Connect dots with clinical cases."),
    ("PSM / Forensic", "Vaccine schedules, biostatistics & IPC codes. Low-hanging fruit scoring."),
    ("Pediatrics / ENT / Ophtha", "Milestones, audiograms, fundus images. 25 MCQs to lock high-yield memory."),
    ("Diagnostic Integration & Rest", "Light revision of past bookmark notes + relaxed walk with Mom.")
]
day_index = now_ist.weekday()
focus_subject, focus_task = anchors[day_index % len(anchors)]

message = f"""🌅 *LIFE OS | MORNING BRIEFING*
🗓️ *{date_str}*

⚡ *TODAY'S 3 CLEAN SWINGS*
1. *Cellular Energy*: 750ml water + 15 min natural morning light.
2. *Marrow Rhythm*: {focus_subject} — {focus_task}
3. *Mother*: 10 mins peaceful tea & presence (zero phone).

🪐 *ASTRONOMICAL & ASSET GAUGES*
• *Janma Shani Peak*: ~{max(0, days_to_peak_lift)} days of Saturn compression remaining.
• *Marrow Runway*: {max(0, days_to_marrow)} active days left on Plan C.
• *Truth of the Day*: _"Routine heals what thinking paralyzes. You only have to win the next 60 minutes."_

📱 *TAP TO OPEN LIFE OS*
👉 [Open Your Dashboard](https://archiboltmusk.github.io/life/)
"""

bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
chat_id = os.environ.get("TELEGRAM_CHAT_ID")

if not bot_token or not chat_id:
    print("WARNING: TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID is not configured in repository secrets.")
    print("Briefing generated successfully (dry-run output):")
    print("--------------------------------------------------")
    print(message)
    print("--------------------------------------------------")
    sys.exit(0)

# Send to Telegram
url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
payload = {
    "chat_id": chat_id,
    "text": message,
    "parse_mode": "Markdown",
    "disable_web_page_preview": False
}

req = urllib.request.Request(
    url,
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)

try:
    with urllib.request.urlopen(req, timeout=15) as response:
        res = json.loads(response.read().decode())
        if res.get("ok"):
            print("Successfully dispatched morning briefing to Telegram.")
        else:
            print("Telegram API returned non-OK:", res)
except Exception as e:
    print(f"Error sending message to Telegram: {e}")
    sys.exit(1)
