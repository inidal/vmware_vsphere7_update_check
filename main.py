from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

URL = 'https://www.virten.net/vmware/esxi-release-build-number-history/'

# Update with latest release
installed_version = "ESXi 7.0 Update 3j"

req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, "html.parser")

latest_version = soup.find_all('table')[1].tbody.td.text

if __name__ == '__main__':
    if latest_version != installed_version:
        print(f"New ESXi 7.0 update available.\nINFO: You're using '{installed_version}' while '{latest_version}' is available.")
    else:
        print(f"vSphere ESXi 7.0 up to date.\nINFO: You're using '{installed_version}'.")