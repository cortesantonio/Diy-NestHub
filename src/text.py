from datetime import datetime
date = datetime.now()
x = int(date.time().strftime("%H"))

if x > 19:
    print('buenas noches')
elif x <19 and x>=12:
    print('buenas tardes')
elif x >=0 and x<12:
    print('buenos dias')
