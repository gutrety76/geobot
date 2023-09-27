TOKEN = '6435860276:AAHt08jxyDzsdGTVz2rX6Rd26-bc18hIAJ4'
import sqlite3

conn = sqlite3.connect('cities.db', check_same_thread=False)
c = conn.cursor()

countries = ['Россия', 'СНГ', 'МИР']

c.execute("select name from cities where level = 'Россия'")

RU = [item[0].strip() for item in c.fetchall()]

c.execute("select name from cities where level = 'СНГ'")

SNG = [item[0].strip() for item in c.fetchall()]

c.execute("select name from cities where level = 'МИР'")

WORLD = [item[0].strip() for item in c.fetchall()]

conn.close()

all_domains = {'Россия': RU, 'СНГ': SNG, 'МИР': WORLD}


