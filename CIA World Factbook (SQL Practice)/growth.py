import sqlite3
import pandas as pd
import numpy as np
import math 

conn = sqlite3.connect("factbook.db")
query = "select * from facts;"
facts = pd.read_sql_query(query, conn)
facts = facts.dropna(axis=0)
def population_growth(row):
    n = row['population']*(math.e**((row['population_growth']/100)*35))
    return round(n,0)
facts["population_2050"] = facts.apply(population_growth, axis = 1)
facts.sort_values("population_2050", ascending = False, inplace = True)
print(facts["name"][:10])