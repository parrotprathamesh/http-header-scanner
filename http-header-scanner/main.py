import argparse
from scanner import scan_headers

def main():
    parser = argparse.ArgumentParser(description="HTTP Header Scanner")
    parser.add_argument("url", help="Target URL to scan (e.g., https://example.com)")
    args = parser.parse_args()

    url = args.url
    print(f"Scanning headers for: {url}\n")
    scan_headers(url)

if __name__ == "__main__":
    main()
