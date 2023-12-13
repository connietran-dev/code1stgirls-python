import datetime

x = datetime.datetime.now()
print(f'x = {x}')

# from [module] import [class]
from datetime import datetime

y = datetime.now()
print(f'y = {y}')

from datetime import date

my_date = date(2023, 12, 13)

# string format time
print(my_date.strftime("%d-%b-%Y"))

from datetime import datetime as dt

z = dt.now()
print(f'z = {z}')

