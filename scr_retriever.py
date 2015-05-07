import pycurl
import re
from StringIO import StringIO
from bs4 import BeautifulSoup

buffer = StringIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://www3.imperial.ac.uk/eatinganddrinking/cateringoutlets/seniorcommonroom/scrrestaurantmenu')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
soup = BeautifulSoup(body)

main_content = soup.find("table",{"id":"rg588879"}).find("div",{"id":"main-content"})

to_start =main_content.find(text=re.compile("To start"))
if to_start:
    print "To start:"
    print "\t"+to_start.findNext('h3').get_text()

main_items=main_content.find(text=re.compile("To follow")).findNext('ul').findNext("ul").find_all("li")

if main_items:
    print "To follow:"

    for item in main_items:
        txt = item.get_text()
        if (not ("allergy" in txt or "Allergy" in txt )) and len(txt)>6:
            print "\t"+item.get_text()
