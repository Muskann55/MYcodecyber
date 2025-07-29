import requests

subdomains = ['www', 'mail', 'blog', 'admin']
domain = 'microsoft.com'

for sub in subdomains:
    url = f"https://www.microsoft.com/en-in/"
    print(f"[+] Found: {url}")

    try:
        response = requests.get(url.strip(), timeout=3)
        if response.status_code == 200:
            print(f"[✓] Live: {url}")
    except requests.exceptions.InvalidURL as e:
        print(f"[✗] Invalid URL: {url}")
    except requests.exceptions.RequestException as e:
        print(f"[✗] Error accessing {url}: {e}")
print(f"Trying URL: {repr(url)}")  
