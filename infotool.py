import sys, socket, requests, json, time, re
try:
    import pyperclip
    HAS_PYPERCLIP = True
except ImportError:
    HAS_PYPERCLIP = False
def is_valid_domain(domain):
    """Basic validation for domain format."""
    pattern = r"^(?!\-)(?:[a-zA-Z0-9\-]{1,63}\.)+[a-zA-Z]{2,6}$"
    return re.match(pattern, domain) is not None

def get_ip_address(domain):
    """Resolve IP address from domain."""
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        print(f" Could not resolve IP for: {domain}")
        sys.exit(1)

def get_ip_location(ip):
    """Fetch location info from ipinfo.io with latency measurement."""
    try:
        start = time.time()
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        latency = (time.time() - start) * 1000  # in ms
        response.raise_for_status()
        return response.json(), latency
    except requests.RequestException:
        print(" Failed to fetch location data from ipinfo.io")
        sys.exit(1)

def copy_to_clipboard(text):
    """Copy text to clipboard if pyperclip is available."""
    if HAS_PYPERCLIP:
        pyperclip.copy(text)
        print("IP address copied to clipboard!")
    else:
        print("pyperclip not installed. Install with 'pip install pyperclip' to enable clipboard copy.")

def print_pretty(domain, ip, location_data, latency):
    """Print nicely formatted output."""
    print("\n Website Info Lookup")
    print(f" Domain     : {domain}")
    print(f" IP Address : {ip}")
    print(f" API Latency : {latency:.2f} ms\n")

    print(" Location Data (via ipinfo.io):")
    for key in ['city', 'region', 'country', 'loc', 'org', 'timezone']:
        value = location_data.get(key, 'N/A')
        print(f"  {key.capitalize():10}: {value}")

def print_raw_json(data):
    """Print raw JSON output."""
    print(json.dumps(data, indent=4))
##-----main function------------------##
def main():
    args = sys.argv[1:]

    if not args or '--help' in args or '-h' in args:
        print("Usage: python infotool.py <website_url> [--raw] [--copy]")
        print("  --raw   : output raw JSON")
        print("  --copy  : copy IP address to clipboard")
        sys.exit(0)
    # Parse flags
    raw_output = '--raw' in args
    copy_flag = '--copy' in args
    # Extract domain (first argument that's not a flag)
    domain = next((a for a in args if not a.startswith('--')), None)
    if not domain:
        print(" Please provide a website domain.")
        sys.exit(1)
    if not is_valid_domain(domain):
        print(f" Invalid domain format: {domain}")
        sys.exit(1)

    ip = get_ip_address(domain)
    location_data, latency = get_ip_location(ip)

    if copy_flag:
        copy_to_clipboard(ip)

    if raw_output:
        print_raw_json(location_data)
    else:
        print_pretty(domain, ip, location_data, latency)

if __name__ == "__main__":
    main()
