import pycurl
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

main_items=soup.find("table",{"id":"rg588883"}).find("div",{"id":"main-content"}).find_all("strong")

for item in main_items:
    txt = item.get_text()
    if (not ("allergy" in txt or "Allergy" in txt or "served" in txt)) and len(txt)>6:
        print "\t"+item.get_text()
