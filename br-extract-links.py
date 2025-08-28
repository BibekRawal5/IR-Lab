
import urllib.request
import re

def extract_links(url, outfile):
    response = urllib.request.urlopen(url)
    html = response.read().decode("utf-8")
    links = re.findall(r'href=["\'](.*?)["\']', html)
    with open(outfile, "w", encoding="utf-8") as f:
        for link in links:
            f.write(link + "\n")
    print("Total links found:", len(links))

url = "https://bibek.rawal.com.np"
outfile = "br-links.txt"
extract_links(url, outfile)
