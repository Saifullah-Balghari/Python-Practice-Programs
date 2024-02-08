import time

hour = int(time.strftime('%H'))
print("Time is: ", time.strftime('%H:%M:%S'))

if 5 <= hour <= 9:
    print("Good-morning!")
elif 10 <= hour <= 12:
    print("Good-Afternoon")
elif 13 <= hour <= 16:
    print("Good-Evening")
elif 17 <= hour <= 19:
    print("Good-night")
else:
    print("Sweet-Dreams")
