from time import gmtime, strftime, time
from datetime import datetime

spent = gmtime(0)
month=strftime("%B", spent)
print(f"Seconds since {month} {spent.tm_mon}, {spent.tm_year}: {'{:,.4f}'.format(time())} or {'{:.2e}'.format(time())} in scientific notation")

spent = datetime.now()
print(spent.strftime("%b %d %Y"))
