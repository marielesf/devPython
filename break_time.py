import webbrowser
import time

count = 0

print ("Started on "+time.ctime())
while (count < 3):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=2vjPBrBU-TM")
    count = count + 1

print "Good bye!"

