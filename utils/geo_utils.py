import requests

def get_ip():
    return requests.get("https://api64.ipify.org?format=json").json()["ip"]

def get_country(ip_address):
    return requests.get(f"http://ipinfo.io/{ip_address}/json").json().get("country")
