import pycurl
import re
from StringIO import StringIO
from bs4 import BeautifulSoup

buffer = StringIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://www3.imperial.ac.uk/eatinganddrinking/cateringoutlets/hbar/cafemenu')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
soup = BeautifulSoup(body)

main_content = soup.find("table",{"id":"rg588883"}).find("div",{"id":"main-content"})

chef_salad =main_content.find(text=re.compile("Chef's Salad"))
if chef_salad:
    print "Chef's Salad"
    print "\t"+chef_salad.findNext('p').get_text()

main_items=main_content.find_all("strong")

for item in main_items:
    txt = item.get_text()
    if (not ("allergy" in txt or "Allergy" in txt or "served" in txt)) and len(txt)>6:
        print "\t"+item.get_text()
