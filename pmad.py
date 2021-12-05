import os
import threading
import time
try:
    import samino as amino
except ModuleNotFoundError:
    os.system("pip install samino")
    import samino as amino
try:
    import colorama
except ModuleNotFoundError:
    os.system("pip install colorama")
    import colorama
try:
    import pyfiglet
except ModuleNotFoundError:
    os.system("pip install pyfiglet")
    import pyfiglet
colorama.init()
print(colorama.Fore.GREEN)
print(colorama.Style.BRIGHT)
def main():
    client = amino.Client("22D3085F471DF87A00FB4CE43052685FE93239644F93AD2140B23F3C77277FF6CAE5A0C164593CD9A8")
    os.system("clear||cls")
    f = pyfiglet.Figlet(font='5lineoblique')
    print (f.renderText('Sadv v2'))
    print("Translated by coma\n")
    print("ÐÐ²Ñ‚Ð¾Ñ€: Darkwater\n")
    print("t.me/DWReaction\n\n")
    email = input("enter your email: ")
    password = input("password: ")
    client.login(email = email, password = password)
    global comchoice
    def comchoice():
        comresp = client.get_my_communitys(start = 0, size = 500)
        for i, name in enumerate(comresp.name, 1):
            print(f"{i} > {name}")
        global comId
        comId = comresp.comId[int(input("community: "))-1]
        print(f"ID communty: {comId}")
        global sub_client
        sub_client = amino.Local(comId = comId)
    comchoice()
    print("1. regular")
    print("2. invite to group chat")
    advtype = int(input("how many?: "))
    if advtype == 1:
        msg = input("insert message: ")
        tc = int(input("number of threads: "))
        for i in range(tc):
            threading.Thread(target = first_type, args = (i, msg)).start()
    if advtype == 2:
        msg = input("insert message: ")
        usercount = int(input("how many to one chat?: "))
        for i in range(9):
            threading.Thread(target = second_type, args=(i, msg, usercount)).start()
def first_type(i, msg):
    def verifychecker(i):
        while True:
            if i == 0:
                verify = True
                return
            else:
                if "verify" not in locals():
                    pass
                else:
                    return
    while True:
        try:
            a = i
            b = 1
            onlist = sub_client.get_online_users(start = a, size = b)
            if onlist.userId == []:
                print("Online users in this community have run out. Back to the selection.")
                comchoice()
            else:
                sub_client.start_chat(userId = onlist.userId, message = msg, asWeb = True)
                a += 1
                print("Message Sent")
        except KeyboardInterrupt:
            print("An interrupt was detected. Back to the selection of communities")
            comchoice()
        except Exception as ext:
            try:
                if ext.args[0]['url']:
                    if i == 0:
                        time.sleep(3)
                        link = ext.args[0]['url']
                        print(f"Go through the captcha and press Enter")
                        print(link)
                        input("> ")
                        verifychecker(i)
                    else:
                        verifychecker(i)
                else:
                    print(f"Message not sent ({ext})")
            except:
                pass
def second_type(i, msg, usercount):
    def verifychecker(i):
        while True:
            if i == 0:
                verify = True
                return
            else:
                if "verify" not in locals():
                    pass
                else:
                    return
    if i == 0:
        iden = 0
    if i == 1:
        iden = usercount
    if i == 2:
        preiden = usercount + usercount
        iden = preiden
    else:
        preiden = usercount + usercount
        for r in range(i):
            preiden = preiden + usercount
            iden = preiden
    while True:
        try:
            a = iden
            b = usercount
            onlist = sub_client.get_online_users(start = a, size = b)
            if onlist.userId == []:
                print("Online users in this community have run out. Back to the selection.")
                comchoice()
            else: 
                sub_client.start_chat(userId = onlist.userId, message = msg, asWeb = True)
                a += usercount
                print("Chat created")
        except KeyboardInterrupt:
            print("An interrupt was detected. Back to the selection of communities")
            comchoice()
        except Exception as ext:
            if ext.args[0]['url']:
                if i == 0:
                    verify = False
                    time.sleep(3)
                    link = ext.args[0]['url']
                    print(f"Go through the captcha and press Enter")
                    print(link)
                    input("> ")
                    verifychecker(i)
                else:
                    print(f"Stream with number {i} awaiting verification")
                    verifychecker(i)
                    
            else:
                print(f"Chat not created ({ext})")
main()