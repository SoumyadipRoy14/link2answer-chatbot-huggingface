import requests
from bs4 import BeautifulSoup
import re

url = input("Enter the URL to extract content from: ")

# Fetch and parse webpage
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract and clean text
text_content = soup.get_text(separator=" ", strip=True)

# Remove noisy dialogue markers and boilerplate
patterns = [r"(Human:|User:|\[/ASS\])", r"Subscribe.*", r"Advertisement.*"]

for p in patterns:
    text_content = re.sub(p, "", text_content, flags=re.IGNORECASE)

# Extract links and images (optional)
links = [l['href'] for l in soup.find_all('a', href=True)]
images = [i['src'] for i in soup.find_all('img', src=True)]

print("Run Successful web_extract.py")
