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

date_str = now_ist.strftime("%A, %b %d, %Y")
marrow_expiry = datetime(2027, 1, 16, tzinfo=IST)
days_to_marrow = (marrow_expiry - now_ist).days

transit_target = datetime(2027, 2, 23, tzinfo=IST)
days_to_peak_lift = (transit_target - now_ist).days

# Determine morning vs evening
briefing_type = sys.argv[1] if len(sys.argv) > 1 else "auto"
if briefing_type == "auto":
    # If after 2:00 PM IST (14:00), treat as evening
    briefing_type = "evening" if now_ist.hour >= 14 else "morning"

bot_token = (os.environ.get("TELEGRAM_BOT_TOKEN") or "").strip()
chat_id = (os.environ.get("TELEGRAM_CHAT_ID") or "").strip()

if briefing_type == "morning":
    anchors = [
        ("Medicine / Pharmacology", "Rapid Review 1 module + 20 MCQs. Accuracy over speed."),
        ("Pathology / Microbiology", "High-yield image flashcards + 20 MCQs. Recognize visual patterns."),
        ("Surgery / Obstetrics", "Procedural anatomy & clinical vignettes. Hand-eye surgical logic."),
        ("Biochemistry / Physiology", "High-yield cycles & clinical correlations."),
        ("PSM / Forensic", "Vaccine schedules, biostatistics & IPC codes. High-yield scoring."),
        ("Pediatrics / ENT / Ophtha", "Milestones, audiograms, fundus images. 20 MCQs."),
        ("Diagnostic Integration & Rest", "Light revision of bookmarks + relaxed walk with Mom.")
    ]
    day_index = now_ist.weekday()
    focus_subject, focus_task = anchors[day_index % len(anchors)]

    message = f"""🌅 *LIFE OS | MORNING BRIEFING*
🗓️ *{date_str}*

⚡ *TODAY'S 3 CLEAN SWINGS*
1. *Cellular Energy*: 750ml water + 15 min morning daylight.
2. *Marrow Rhythm*: {focus_subject} — {focus_task}
3. *Mother*: 10 mins peaceful presence (zero phone).

🪐 *ASTRONOMICAL & ASSET GAUGES*
• *Janma Shani Peak*: ~{max(0, days_to_peak_lift)} days remaining until Saturn compression lifts.
• *Marrow Runway*: {max(0, days_to_marrow)} active days left on Plan C.
• *Truth of the Day*: _"Routine heals what thinking paralyzes. Win the next 60 minutes."_

📱 *TAP TO LAUNCH LIFE OS*
👉 [Open Your Dashboard](https://archiboltmusk.github.io/life/)
"""
    reply_markup = {
        "inline_keyboard": [
            [
                {"text": "🚀 Open Life OS", "url": "https://archiboltmusk.github.io/life/"}
            ]
        ]
    }

else:
    # Evening Briefing
    message = f"""🌙 *LIFE OS | EVENING REFLECTION*
🗓️ *{date_str}*

Did you close your 3 rings today?
• 💧 *Biology*: 750ml water + 15 min sunlight
• 📚 *Marrow*: 20 MCQs (kinetic friction broken)
• 🌸 *Mother*: 10 mins peaceful tea & presence

Tap an action below to sync and close your ring on your dashboard:
"""
    reply_markup = {
        "inline_keyboard": [
            [
                {"text": "💧 Closed Water", "url": "https://archiboltmusk.github.io/life/?check=bio"},
                {"text": "📚 20 MCQs Done", "url": "https://archiboltmusk.github.io/life/?check=study"}
            ],
            [
                {"text": "🌸 Mom Time Done", "url": "https://archiboltmusk.github.io/life/?check=peace"}
            ],
            [
                {"text": "📱 Open Full Dashboard", "url": "https://archiboltmusk.github.io/life/"}
            ]
        ]
    }

if not bot_token or not chat_id:
    print("WARNING: TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID is not configured.")
    print("Briefing generated successfully (dry-run output):")
    print("--------------------------------------------------")
    print(message)
    print("Payload Markup:", json.dumps(reply_markup, indent=2))
    print("--------------------------------------------------")
    sys.exit(0)

# Send to Telegram
url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
payload = {
    "chat_id": chat_id,
    "text": message,
    "parse_mode": "Markdown",
    "reply_markup": reply_markup,
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
            print(f"Successfully dispatched {briefing_type} briefing to Telegram.")
        else:
            print("Telegram API returned non-OK:", res)
except Exception as e:
    print(f"Error sending message to Telegram: {e}")
    sys.exit(1)
