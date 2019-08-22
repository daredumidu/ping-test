#execute ping and hping3 to hosts listed in a txt file and write the result to a csv file.

import os
import csv

f = open ("host.txt", "r")
f1 = f.readlines()

f = open ("result.csv","w+")

for address in f1:
 address = address.rstrip() # rstrip - remove the new line
 response = os.system('ping -c 1 ' + address)
 
 if response == 0:
  f.write("%s,up \n" % address) # \n - new line, %s - read from %
 else:
  response1 = os.system('hping3 -S -p 80 -c 1 ' + address)
   
  if response1 == 0:
   f.write("%s,up,icmp block \n" % address)
  else:
   response2 = os.system('hping3 -S -p 443 -c 1 ' + address)

   if response2 == 0:
    f.write("%s,up,icmp block,port 80 block,port 443 open \n" % address)
   else:
    f.write("%s,down \n" % address)
