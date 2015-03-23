import pycurl
from StringIO import StringIO
from bs4 import BeautifulSoup

buffer = StringIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://www3.imperial.ac.uk/eatinganddrinking/cateringoutlets/fuel')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
soup = BeautifulSoup(body)

main_items=soup.find("div",{"class":"generic-content-block"}).find_all("strong")

for item in main_items:
    if not item is None:
        txt = item.get_text()
        next_item = item.next_sibling
        if (not ("allergy" in txt or "Allergy" in txt or "served" in txt)) and len(txt)>6 and (not next_item is None) and (not "Week" in txt):
            to_print = "\t"+(item.get_text().encode('utf-8')+(next_item.encode('utf-8'))).split("(")[0].strip()
            print to_print