"""import datetime

x=datetime.datetime.now()
y=x-datetime.timedelta(days=5)
print (x)
print (y)
"""

"""import datetime

x=datetime.datetime.now()
y=x-datetime.timedelta(days=1)
z=x+datetime.timedelta(days=1)

print(y)
print(x)
print(z)"""

import datetime

x=datetime.datetime.now()

"""print(x.strftime("%f"))"""

import datetime

x=datetime.datetime.now()
y=datetime.datetime(2025, 10, 3)

z=x-y

date=datetime.datetime(1,1,1)+z
print(date.strftime("%S"))