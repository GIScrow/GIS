import urllib2
from bs4 import BeautifulSoup

url = "http://wdfw.wa.gov/hatcheries/facilities.php"  # change to whatever your url is

page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, "lxml")

for tr in soup.find_all('tr')[2:]:
    tds = tr.find_all('td class="reading_text"')
    print str(tds)
