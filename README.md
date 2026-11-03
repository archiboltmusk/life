# Life OS — Project Autonomy

> Master Life Architecture, Astrological Transit Alignment & Daily Execution OS.

- **Live URL**: [https://archiboltmusk.github.io/life/](https://archiboltmusk.github.io/life/)
- **Target**: Sovereign Liquid Corpus by Age 43 & Pro-Bono Purulia Healthcare.

---

## 📱 Apple iOS PWA Installation (Home Screen App)

1. Open **[https://archiboltmusk.github.io/life/](https://archiboltmusk.github.io/life/)** in **Safari** on your iPhone.
2. Tap the **Share** button (the square with an arrow pointing up).
3. Scroll down and tap **Add to Home Screen**.
4. Tap **Add** in the top right corner.
5. The **Life OS** icon will appear on your iPhone home screen. Tapping it opens full-screen OLED with zero browser bars.

---

## 🤖 60-Second Telegram Morning Briefing Setup

To receive daily 08:00 AM IST lockscreen briefings via GitHub Actions:

### Step 1: Create Your Private Bot (30 seconds)
1. Open Telegram and search for `@BotFather`.
2. Send `/newbot`, give it a name (e.g. `MyLifeOSBot`) and username (e.g. `archibolt_life_bot`).
3. Copy the **HTTP API Token** BotFather gives you.

### Step 2: Get Your Chat ID (15 seconds)
1. Search for `@userinfobot` on Telegram and tap **Start**.
2. Copy your numerical **Id** (e.g. `123456789`).
3. Send a greeting (e.g. `Hello`) to your newly created bot so it can message you.

### Step 3: Add to GitHub Secrets (15 seconds)
Run in terminal (with GitHub CLI):
```bash
gh secret set TELEGRAM_BOT_TOKEN --body "YOUR_BOT_TOKEN_HERE" --repo archiboltmusk/life
gh secret set TELEGRAM_CHAT_ID --body "YOUR_NUMERICAL_ID_HERE" --repo archiboltmusk/life
```
Or set them via GitHub Web:
`Repo Settings -> Secrets and variables -> Actions -> New repository secret`.

Once added, GitHub Actions will automatically send you your briefing every morning at 08:00 AM IST!
