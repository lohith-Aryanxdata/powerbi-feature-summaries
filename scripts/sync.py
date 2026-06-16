import requests
import re
from pathlib import Path
from datetime import datetime

RAW_URL = "https://raw.githubusercontent.com/NajiElKotob/Awesome-Power-BI/master/README.md"

content = requests.get(RAW_URL).text

desktop_pattern = (
    r"## Power BI Desktop Feature Summary(.*?)"
    r"## Power BI Service and Mobile Feature Summary"
)

service_pattern = (
    r"## Power BI Service and Mobile Feature Summary(.*?)"
    r"## Power BI Samples"
)

desktop = re.search(desktop_pattern, content, re.S)
service = re.search(service_pattern, content, re.S)

# Create folders if they don't exist
Path("Desktop").mkdir(exist_ok=True)
Path("Service-Mobile").mkdir(exist_ok=True)

desktop_content = ""
service_content = ""

if desktop:
    desktop_content = desktop.group(1).strip()

    with open(
        "Desktop/desktop_feature_summary.md",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(desktop_content)

if service:
    service_content = service.group(1).strip()

    with open(
        "Service-Mobile/service_mobile_feature_summary.md",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(service_content)

last_updated = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

readme = f"""# Power BI Feature Summaries

A curated repository containing automatically synchronized Power BI feature summaries.

## Last Updated

{last_updated}

## Source Repository

https://github.com/NajiElKotob/Awesome-Power-BI

All content is sourced from the Awesome-Power-BI repository and synchronized automatically.

---

## Contents

### Desktop Feature Summary

📂 [Desktop Feature Summary](Desktop/desktop_feature_summary.md)

### Service & Mobile Feature Summary

📂 [Service & Mobile Feature Summary](Service-Mobile/service_mobile_feature_summary.md)

---

## Preview

### Power BI Desktop Feature Summary

{desktop_content[:2000]}

---

### Power BI Service and Mobile Feature Summary

{service_content[:2000]}
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

print("README updated successfully")
