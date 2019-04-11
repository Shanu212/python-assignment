import urllib.request
from bs4 import BeautifulSoup
# import MySQLdb
# db = MySQLdb.connect("192.168.121.187", "first_year", "first_year", "first_year_db")
p_scrapped = []

#sql decorator
# def decorator(func):
#     def inner1(*args):
#         for i in args:
#             name=i
#         cursor = db.cursor()
#         cursor.execute("SELECT * FROM shanu_user_python WHERE username = '{}'".format(name))
#         row = cursor.fetchone()
#         if row:
#             func(args)
#         else:
#             raise exception('user does not exist')
#     return inner1

#decorator for scrap
def decorator1(func):
    def inner1(name):
        x=0
        for i in range(len(p_scrapped)):
            if name == p_scrapped[i].username:
                x=1
                break
        if x > 0:
            p_scrapped[i].show()
        else:
            func(name)
    return inner1

#class
class Person:
    def __init__(self, username, name, work=[], city='Roorkee', fav={}):
        self.name = name
        self.username = username
        if len(work) != 0:
            self.work = work 
        self.city = city
        self.fav = fav
    def show(self):
        print("My name is %s and my city is %s" % (self.name, self.city))

#scrap
@decorator1
def scrap(name):
    fb = "https://en-gb.facebook.com/{}".format(name)
    page = urllib.request.urlopen(fb)
    soup = BeautifulSoup(page, 'lxml')
    NAME = soup.find('a', class_='_2nlw _2nlv').get_text()
    CITY = soup.find(class_='_2iel _50f7').get_text()
    WORK = []
    try:
        for tags in soup.find(class_='_4qm1').find_all(class_='_2lzr _50f5 _50f7'):
            WORK.append(tags.find('a').get_text())
        print(WORK)
    except:
        print("Unemployed")         
    fav = {}
    try:
        for rows in soup.find(class_='mtm _5e7- profileInfoTable _3stp _3stn').find_all('tbody'):
            if rows.find(class_='labelContainer').get_text() != 'Other':
                fav.update({rows.find(class_='labelContainer').get_text(): rows.find(class_='mediaPageName').get_text()})
        if fav == {}:
            raise exception() 
    except:
        fav = "There are no favourites."
    print(fav)    
    p = Person(name, NAME, WORK, CITY, fav)
    p_scrapped.append(p)
