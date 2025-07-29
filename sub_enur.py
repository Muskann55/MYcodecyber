import requests

target_domain = "google.com"

with open("wordlist.txt", "r") as file:
    for subdomain in  file:
        subdomain = subdomain.strip()
        url = f"http://www.google.com"
        
        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                print(f"[+] Found: {url}")
        except requests.ConnectionError:
            pass 
with open("wordlist.txt", "r") as f:
    print(f.read())                   