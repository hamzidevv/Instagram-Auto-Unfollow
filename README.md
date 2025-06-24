# Instagram Auto-Unfollow Bot 🤖

A Python automation script that unfollows everyone from your Instagram account using Selenium — giving you time to binge-watch Netflix while it handles the boring stuff. 😎

> **Note:** This script interacts with the Instagram web interface. It may break if Instagram updates its layout or security features.

---

## Features

- Automates Instagram login using your credentials.
- Opens and scrolls through your **Following** list.
- Unfollows each user individually with confirmation.
- Fully hands-free once launched.

---

## Requirements

- Python 3.x
- Google Chrome browser
- `chromedriver` installed (compatible with your browser version)
- A `.env` file containing your Instagram credentials
- Required Python packages:
  - `selenium`
  - `python-dotenv`

---

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/hamzidevv/Instagram-Auto-Unfollow.git
   cd Instagram-Auto-Unfollow

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   
3. **Add your Instagram credentials in a `.env` file at the project root:**
   ```bash
   user=your_instagram_username
   pass=your_instagram_password
   
4. **Download the appropriate version of `chromedriver` for your OS and Chrome version:**
   [Chrome Driver](https://chromedriver.chromium.org/downloads)
   Place the driver in the project directory or your system PATH.

5. **Run the script:**
   ```bash
   python main.py

## How It Works
1. Logs into your Instagram account using your saved credentials.
2. Navigates to your profile and opens the Following list.
3. Scrolls to load all the followed accounts.
4. Clicks the Unfollow button for each user and confirms.
5. Waits briefly between actions to mimic human behavior.

## Customize & Adjust
- You can modify `time.sleep()` delays in the script to match your internet or system speed.
- If the script fails (e.g., due to changes in Instagram's UI):
  - Update selectors or logic in `main.py`.
  - Or, reach out — I'm happy to help you debug it!

## ⚠️ Disclaimer
Instagram frequently updates its layout and security policies.
This script **may break** in the future. You can adjust it to match the updated interface or:
> Contact the author for help, or tweak it yourself — it's designed to be easily modifiable!

## 🎉 Bonus: The Backstory
After recovering from a hack, I found my "Following" list packed with 2000+ random accounts — and I hadn't followed a single one of them (not even my siblings 😂). Manually cleaning it up was way too boring. So, I wrote this script, kicked back with two Netflix episodes, and let Python handle the dirty work.

## 📄 License
This project is intended for educational use only. Automating interactions with Instagram may violate their terms of service. Use responsibly and at your own risk.
