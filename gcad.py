
import samino
import requests,json
from os import _exit
#http://aminoapps.com/c/emp_g
#BY_Emp
email = input("email>>>")
password = input("password>>>")
client = samino.Client(input("Device       :")) 
client.login(email, password) 
obj=client.get_from_link(input(' >>> chatLink:  '))
Ch=obj.objectId
com=obj.comId
local = samino.Local(com) 

C_On=int(0)
On=int(100)
sa=int(input(" >>>  Number of invitations:  "))
while True:

     for Us in local.get_online_users(start=C_On,size=On).userId:
        InFO=client.get_user_info(Us).nickname
        if C_On<sa:
          On+=1
          C_On+=1      
          try:
             t=requests.post(headers=client.headers, url=f"{client.api}/x{com}/s/chat/thread/{Ch}/member/{Us}")
             error=json.loads(t.text)     
             error=str(error["api:message"])
             print(C_On,"-",InFO,">",error)
          except:
                    print("Information error",error)   

        if C_On==sa:
                      print(">>>",f"- {C_On} people we tried to invite.")

                      _exit(1)