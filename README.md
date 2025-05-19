
# IP & Location Lookup Tool

A simple Python command-line utility that resolves the IP address of any website domain and fetches detailed geolocation information from [ipinfo.io](https://ipinfo.io).

---

## What is this tool?

This tool helps you quickly find the IP address and location details (city, country, ISP, timezone, etc.) of any website. It’s great for developers, sysadmins, cybersecurity enthusiasts, or anyone curious about the geographical and network information behind a domain.

---

## Why use this tool?

- Instantly get IP and location info via terminal.
- Supports pretty formatted or raw JSON output.
- Optional clipboard copy of IP address.
- Minimal dependencies, easy to run.
- Useful for debugging, networking, or learning about web infrastructure.

---

## How does it work?

1. Converts a domain name to its IP address using Python’s `socket` module.
2. Queries the `ipinfo.io` API to retrieve location and network details about the IP.
3. Displays results in your chosen format and optionally copies the IP to clipboard.

---

## Requirements

- Python 3.x
- `requests` library
- Optional: `pyperclip` for clipboard support
  ## Usage

Run the tool from the command line as follows:

```bash
python infotool.py <website_domain> [--raw] [--copy]


Install dependencies with:

```bash
pip install requests
pip install pyperclip   # optional, only if using --copy flag
