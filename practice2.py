#program to find area,diagnol and circumfrance of cubiod
import math
l=10
w=20
h=24
volume=l*w*h
x=l**2+w**2+h**2
diagnoal= math.sqrt(x)
circumference=4*(l+w+h)
print("volume:",volume)
print("diagonal:",diagnoal)
print("circumfrance:",circumference)
