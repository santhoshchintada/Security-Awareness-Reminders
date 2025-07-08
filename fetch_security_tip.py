import smtplib
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os

# === Fetch Latest CISA Exploited Vulnerabilities ===
def fetch_cisa_vulnerabilities(limit=3):
    url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        tips = [f"CISA Known Exploited Vulnerabilities – {datetime.now().strftime('%A, %d %B %Y')}"]

        for item in data["vulnerabilities"][:limit]:
            cve = item.get("cveID", "N/A")
            vendor = item.get("vendorProject", "Unknown Vendor")
            product = item.get("product", "Unknown Product")
            desc = item.get("vulnerabilityName", "No description provided.")
            action = item.get("requiredAction", "No mitigation provided.")
            date_added = item.get("dateAdded", "Unknown")

            tips.append(
                f"\n🔐 **Attack**: {desc}\n"
                f"🧩 **Impact**: {vendor} - {product} | CVE: {cve}\n"
                f"🛠️ **Remediation**: {action}\n"
                f"📆 **Disclosed**: {date_added}"
            )

        return "\n\n".join(tips)

    except Exception as e:
        return f"❌ Failed to fetch CISA data: {e}"

# === Email Sender ===
def send_email(subject, body):
    sender = os.environ.get("EMAIL_USER")
    password = os.environ.get("EMAIL_PASS")
    recipient = os.environ.get("TO_EMAIL")
    host = os.environ.get("EMAIL_HOST", "smtp.gmail.com")
    port = int(os.environ.get("EMAIL_PORT", 587))

    if not all([sender, password, recipient]):
        print("❌ Email environment variables missing!")
        return

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(host, port) as server:
            server.starttls()
            server.login(sender, password)
            server.send_message(msg)
            print("✅ Security alert email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

# === Main Entry ===
def main():
    tips = fetch_cisa_vulnerabilities(limit=3)
    subject = f"🚨 Daily Exploited Vulnerabilities – {datetime.now().strftime('%d %b %Y')}"
    send_email(subject, tips)

if __name__ == "__main__":
    main()
