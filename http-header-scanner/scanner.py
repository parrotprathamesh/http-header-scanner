import requests

# List of recommended security headers
SECURITY_HEADERS = {
    "Strict-Transport-Security": "Helps enforce HTTPS.",
    "Content-Security-Policy": "Prevents XSS and other code injection attacks.",
    "X-Content-Type-Options": "Prevents MIME-type sniffing.",
    "X-Frame-Options": "Prevents clickjacking.",
    "X-XSS-Protection": "Basic XSS protection (deprecated but still useful)."
}

def scan_headers(url):
    try:
        # Send a GET request to fetch headers
        response = requests.get(url, timeout=10)
        headers = response.headers

        print("[+] HTTP Headers found:")
        for header, value in headers.items():
            print(f"    {header}: {value}")

        print("\n[+] Checking for missing security headers:\n")
        for header, description in SECURITY_HEADERS.items():
            if header not in headers:
                print(f"[-] {header} is missing! ({description})")
            else:
                print(f"[+] {header} is present.")

    except requests.exceptions.RequestException as e:
        print(f"[!] Error: Unable to connect to {url}. Details: {e}")
