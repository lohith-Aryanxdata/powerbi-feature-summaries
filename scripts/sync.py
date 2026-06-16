import requests
import re

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

output = """
# Power BI Feature Summaries

This repository automatically syncs selected feature summary sections from the Awesome-Power-BI repository.

Source:
https://github.com/NajiElKotob/Awesome-Power-BI

---

"""

if desktop:
    output += "\n## Power BI Desktop Feature Summary\n"
    output += desktop.group(1).strip()

if service:
    output += "\n\n## Power BI Service and Mobile Feature Summary\n"
    output += service.group(1).strip()

with open("README.md", "w", encoding="utf-8") as f:
    f.write(output)

print("README updated successfully")
