#!/usr/bin/env python3
"""
manual_dns.py — The "old way" of managing DNS.

This is what happens when someone writes a one-off script on their laptop.
Run it and notice the problems.
"""
import requests
import os

API_KEY = os.environ.get("BLOXONE_API_KEY", "HARDCODED_KEY_OOPS")
BASE_URL = "https://csp.infoblox.com/api/ddi/v1"

# Hardcoded records — no environment separation
records = [
    {"name": "webserver", "ip": "10.0.0.5"},
    {"name": "dbserver", "ip": "10.0.0.6"},
    {"name": "appserver", "ip": "10.0.0.7"},
]

for r in records:
    print(f"Creating {r['name']} -> {r['ip']}...")
    # No error handling — what if the API is down?
    # No idempotency — what happens if you run this twice?
    # No state tracking — how do you know what already exists?
    # No audit trail — who ran this, when, from where?
    # No rollback — oops, wrong IP? Good luck.
    print(f"  -> Record '{r['name']}' created (simulated)")

print("\nDone. But ask yourself:")
print("  - What if the API was down halfway through?")
print("  - What if someone already created 'webserver'?")
print("  - What if you need to undo this?")
print("  - What if 10 people run this at the same time?")
print("  - Where is the audit trail?")
print("\nThis is Stage 2: One-off scripts. Fragile and dangerous at scale.")
