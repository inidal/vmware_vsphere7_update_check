from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# [MAINTENANCE] Update with the latest release link
URL = 'https://docs.vmware.com/en/VMware-vSphere/7.0/rn/vsphere-esxi-70u3j-release-notes.html'

# [MAINTENANCE] Update with previous version name (list on website doesn't include the latest version)
previous_version_recorded = "VMware ESXi 7.0, ESXi 7.0 Update 3i Release Notes"

req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, "html.parser")

previous_version_grabbed = soup.find_all("ul")[6].li.text


if __name__ == '__main__':
    if previous_version_grabbed != previous_version_recorded:
        print("VMware new update available.")
    else:
        print("VMware up to date.")