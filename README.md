# Frappe Aviation MRO Aircraft Maintenance & Airworthiness Engine

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Aviation](https://img.shields.io/badge/DGCA%20%2F%20FAA-CAR%20145%20Airworthiness-blue.svg)](https://dgca.gov.in)

Civil aviation Maintenance, Repair & Overhaul (MRO) engine tracking Flight Hours (FH), Flight Cycles (FC), and scheduled A/B/C/D check airworthiness work orders.

## Features
- **Flight Hour & Cycle Telemetry:** Continuous tracking of engine and airframe wear against structural limits.
- **A & C Check Scheduling:** Automatic detection of scheduled inspection thresholds.
- **CAR 145 Certificate of Release to Service (CRS):** AME licensed sign-off and return-to-service validation.

## Installation & Tests
```bash
python3 -m unittest discover tests
```
