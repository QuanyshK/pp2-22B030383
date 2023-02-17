import datetime
c_data = datetime.date.today()
delta = datetime.timedelta(days=5)
c_new = c_data - delta
print(c_data)
print(c_new)
#
import datetime
c_data = datetime.date.today()
delta = datetime.timedelta(days=1)
c_new = c_data - delta
c_future = c_data + delta
print(c_data)
print(c_new)
print(c_future)
#
import datetime
x = datetime.datetime.now()
print(x)
#
from datetime import datetime
def difference(date1, date2):
	datetime1 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
	datetime2 = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')
	diffe = abs(datetime1 - datetime2)
	return diffe.total_seconds()
d1 = input()
d2 = input()
difference = difference(d1, d2)
print(difference)