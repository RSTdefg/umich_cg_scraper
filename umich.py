import requests
from bs4 import BeautifulSoup
import re
import sys ,time

start_time=time.time()
course = sys.argv[1]

response= requests.get("https://www.lsa.umich.edu/cg/cg_detail.aspx?content=2370"+course+"001&termArray=w_22_2370")

soup = BeautifulSoup(response.content,"html.parser" )

table=soup.findAll("div", {"id":"classScheduleBody"})

subj=soup.findAll("span", {"id":"contentMain_lblSubject_2"})
no=soup.findAll("span", {"id":"contentMain_lblCatNo_2"})
title=soup.findAll("span", {"id":"contentMain_lblLongTitle_2"})


sections= soup.findAll("div", {"class": "row clsschedulerow toppadding_main bottompadding_main"})
def is_lec(section):
    return section.find("span", string=re.compile("LEC"))

def print_sections(section,inte):

    number=section.find("div", string="Class No:")
    section_no=number.find_parent().text
    open_seats=section.find("div", string="Open Seats:").find_parent().text
    result=re.findall('\d+', open_seats )
    if is_lec(section):
        print(f"No.{inte} has {result[0]} left")
        return int(result[0])
    return 0
    
i=1
total=0;
for section in sections:
    total+=print_sections(section,i)
    i+=1
print(F"Total left:{total}")
print("--- %s seconds ---" % (time.time() - start_time))
