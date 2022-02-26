# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 14:01:30 2022

@author: Gaurav Mishra
"""
import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 

emails={}


    
  
def check(email,count):   
  
    if(re.search(regex,email)): 
        b={}
        c={}
        
        b["occurance"]=count
        charlist=email.split("@")
        char=str(charlist[0])
        
        length=len(char.split("."))
        if length>1:
           c["type"]="human"
        else:
           c["type"]="nonhuman"
        
        
        
        b.update(c)
        print(b)
        emails[email]=b
   
if __name__ == '__main__' :   
      
    text_file='Get sdfsd ds dsvs vfs sdvcs sdcs abc@qq.com. fdgdf fdgdfg vfdv jeff.bezoz@gmail.com qq.com dsfsdf abc@qq.com'

    a=text_file.split()
    for word in a:
        
        count=text_file.count(word)
        check(word,count)
print(emails)