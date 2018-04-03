import time
import webbrowser

total_breaks = 3
n=0

print('Started at: ' + time.ctime())
while n < total_breaks:
    time.sleep(2)
    print('BREAK')
    # webbrowser.open('https://www.youtube.com/watch?v=3o94NzqOwcc')
    n+=1
