import os
import string

folder = './files/'
# files = os.listdir(folder)
files = ['16los angeles.jpg',
'17cairo.jpg',
'22rochester.jpg',
'25madrid.jpg',
'28houston.jpg',
'29bristol.jpg',
'29buenos aires.jpg',
'2chennai.jpg',
'2hyderabad.jpg',
'35miami.jpg',
'36sydney.jpg',
'37athens.jpg',
'41seoul.jpg',
'45austin.jpg',
'45ithaca.jpg',
'46colombo.jpg',
'47london.jpg',
'47sao paulo.jpg',
'47singapore.jpg',
'48sunnyvale.jpg',
'4istanbul.jpg',
'50san diego.jpg',
'52new york.jpg',
'54dallas.jpg',
'55kiev.jpg',
'5bogota.jpg',
'61edinbrugh.jpg',
'64seattle.jpg',
'66san jose.jpg',
'68pune.jpg',
'69chicago.jpg',
'69shanghai.jpg',
'72bangalore.jpg',
'72bucharest.jpg',
'73delhi.jpg',
'74tel aviv.jpg',
'83gainesville.jpg',
'88jacksonville.jpg',
'89berkeley.jpg',
'90beijing.jpg',
'93manchester.jpg',
'96karachi.jpg',
'97oakland.jpg',
'9barcelona.jpg']

for f in files:
    # newname = ''.join(c for c in f if c.isalpha() or c in allowed_chars)
    table = str.maketrans('0123456789','          ','0123456789')
    newname = f.translate(table)
    print('rename '+ f + ' to ' + newname)
    # os.rename(folder + f, folder + newname)
