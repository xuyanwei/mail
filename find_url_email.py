#-*- coding: utf-8 -*-
import requests
import re  
  
url = 'http://sina.com.cn'

regex = r"([a-zA-Z0-9_.+-]+@[a-pr-zA-PRZ0-9-]+\.[a-zA-Z0-9-.]+)"
html = requests.get(url).text
emails = re.findall(regex,html)

i = 0  
for email in emails:  
    i += 1  
    if i < 16:  
        print("{} :{}".format(i,email))


# import urllib
# content = urllib.urlopen('http://www.iplaypy.com/').read()

# s1=0
# while s1>=0:
#     begin = content.find(r'<a',s1) href=",begin)
#     m2 = content.find(r" m1="content.find(r'">',m1)

#     s1 = m2
#     if(begin<=0):
#         break
#     elif(content[m1:m2].find(r" ")!=-1):
#         m2 = content[m1:m2].find(r' ')
#         url = content[m1+6:m1+m2-1]
#         print url
#     elif m2>=0:
#         url = content[m1+6:m2-1]
#         print url
# print "end."
