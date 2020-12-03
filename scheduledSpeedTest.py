# --- Imports ---
import datetime
import schedule
import speedtest
import socket
import smtplib, ssl
from requests import get
from email.message import EmailMessage
# --- Job ---
def job():
# --- Time and date ---
    time = datetime.datetime.now().strftime("%H:%M:%S %p")
    date = datetime.datetime.now().strftime("%d/%m/%Y")
# --- speedtest ---
    s = speedtest.Speedtest()
    downspeed = round((round(s.download()) / 1048576), 2)
    upspeed = round((round(s.upload()) / 1048576), 2)
# --- Public IP address ---
    public_ip = get("https://api.ipify.org").text
# --- Email login details ---
    EmailAddressSender = ''
    EmailPassword = ''
# --- Email list ---
    EmailAddressReceiver = ""
# --- Email message ---
    msg = EmailMessage()
    msg['Subject'] = f'Speedtest results for: {date}'
    msg['To'] = EmailAddressReceiver
    msg['From'] = EmailAddressSender
    msg.set_content(f"IP address: {public_ip}, time: {time}, downspeed: {downspeed} Mb/s, upspeed: {upspeed} Mb/s")
# --- SMTP over SSL ---
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EmailAddressSender, EmailPassword)
        smtp.send_message(msg)
# --- Job schedule ---
schedule.every().day.at("17:28").do(job)
# --- while loop ---
while True:
    schedule.run_pending()
# --- End ---
