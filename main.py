import requests
from bs4 import BeautifulSoup

myresponse=requests.get("http://menu.dining.ucla.edu/Menus")
soup = BeautifulSoup(myresponse.content, 'html.parser')

def is_menu_block(class_name):
    return str(class_name).startswith("menu-block")
menublocks= soup.findAll("div", {"class": is_menu_block})
print(menublocks[0].prettify())

def print_food_from_block(block):
    time=block.find_previous_sibling("h2").text
    dining_hall=block.h3.text
    menu_items= soup.findAll("li", {"class": "menu-item"})
    for item in menu_items:
        food = item.span.a.text
        print(f"{dining_hall} is serving {food} for {time}")

for block in menublocks:
    print_food_from_block(block)


