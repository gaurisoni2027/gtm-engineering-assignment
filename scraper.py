import requests
import pandas as pd

url = "https://camx2025.mapyourshow.com/8_0/explore/exhibitor-gallery.cfm"

params = {
    "featured": "false"
}

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, params=params, headers=headers)

print("Status Code:", response.status_code)

text = response.text

# split by common company blocks
lines = text.split("\n")

data = []

for line in lines:
    line = line.strip()

    if "exhibitor" in line.lower() or "company" in line.lower():
        data.append({"Company Name": line})

df = pd.DataFrame(data)

df.to_csv("data.csv", index=False)

print(df.head(20))
print("Saved")