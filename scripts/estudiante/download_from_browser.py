import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
import requests
from tqdm import tqdm

query = "industrial boat"
num_pages = 5
image_size = "640x640"
if not os.path.exists(""):
    os.mkdir("")

for i in range(num_pages):
    url = f"https://www.google.com/search?q={query}&tbm=isch&safe=active&s=0&tbs=isz:lt,islt:{image_size}&start={i*20}"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    image_tags = soup.find_all("img")
    image_urls = [tag["src"] for tag in image_tags]
    
    for j, url in tqdm(enumerate(image_urls), desc="Copying files", unit="file"):
        absolute_url = urljoin(response.url, url)
        response = requests.get(absolute_url)
        filename = f"{i*20+j}.jpg"
        with open(filename, "wb") as f:
            f.write(response.content)
