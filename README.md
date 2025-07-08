# 🛡️ Security Awareness Reminders Automation

This project automates the process of collecting the latest real-world security vulnerabilities (CVEs), enriches them with actionable information (attack, impact, remediation), and sends daily reminders to your email inbox using GitHub Actions.

---

## 🚀 Features

- ✅ Fetches recent **exploited vulnerabilities** from [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- 🔎 Enriches data using **NIST CVE API**
- 🧠 Optionally summarizes using **AI** (OpenAI, HuggingFace, etc.)
- 📬 Sends formatted email reminders via **SMTP**
- ⏰ Fully automated with **GitHub Actions** (runs daily at 8:00 AM IST)

---

## 📁 Folder Structure

```
Security-Awareness-Reminders/
├── .github/
│   └── workflows/
│       └── vuln_tip_automation.yml   # GitHub Actions automation
├── requirements.txt                 # Python dependencies
├── fetch_and_send.py                # Core script
```

---

## 📦 Installation (Local Testing)

```bash
git clone https://github.com/yourusername/Security-Awareness-Reminders.git
cd Security-Awareness-Reminders
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### 🔐 Setup .env (for local test)
Create a `.env` file in the project root with the following content:

```
EMAIL_USER=your-email@gmail.com
EMAIL_PASS=your-app-password
TO_EMAIL=recipient-email@example.com
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
OPENAI_API_KEY=sk-...   # (optional)
```

💡 You can generate Gmail App Passwords from: [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)

---

## ⚙️ GitHub Actions Setup
Go to your GitHub repository → **Settings** → **Secrets** → **Actions**

Add the following secrets:

| Secret Name      | Description                        |
|------------------|------------------------------------|
| EMAIL_USER       | Your Gmail address                 |
| EMAIL_PASS       | App password from Gmail            |
| TO_EMAIL         | Receiver email address             |
| OPENAI_API_KEY   | (Optional) for AI summaries        |

---

## 📤 What You Get
Example daily email:

```
📅 CISA Known Exploited Vulnerabilities – Tuesday, 08 July 2025

🔐 Attack: Synacor Zimbra SSRF (CVE-2019-9621)
🧩 Impact: Server-side request forgery in ZCS
🛠️ Remediation: Apply vendor patch or discontinue use
📆 Disclosed: 2025-07-07

🔐 Attack: PHPMailer Command Injection (CVE-2016-10033)
...
```

---

## 🤖 Future Improvements
- Slack or Teams integration
- Store tips to Notion/Confluence/Sheets
- Auto-classify tips by product/team

---

## 👨‍💻 Maintainers
Santhosh Kumar Chintada ([@santhoshchintada](https://github.com/santhoshchintada))

---

## 📄 License
MIT License

---

Made with ❤️ to build a security-first culture every day.