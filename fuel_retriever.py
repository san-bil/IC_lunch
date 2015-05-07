import pycurl
import re
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

main_items=soup.find("div",{"class":"generic-content-block"}).find_all('p')

for item in main_items:
    if not item is None:
        txt = item.get_text()
        if (("of the day" in txt) or ("of the Day" in txt)) and ("-" in txt):
            print "\t"+txt.lstrip()
