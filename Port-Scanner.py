import socket
import _thread
import time
class colors:
    head = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    red = '\033[91m'
    purple = '\033[35m'
    end = '\033[36m'
    bold = '\033[1m'
    line = '\033[4m'
    
class Core(object):
    ipurl=0
    mode=1024
    menu1=False
    f=None
    network="Local Area Network"
    menu2=False
    def GetData(self, url):
        self.url = url
        try:
            self.ipurl = socket.gethostbyname(self.url)
        except Exception as e:
            j = "Invalid"
            print(colors,red,j)
            exit(0)
        Core.ipurl=self.ipurl
        while Core.menu1 is not True:
            choice = input("\033[92m" + "1 - simple \n2 - extend\n")
            if choice == "1":
                Core.mode=1024
                menu=True
                break
            elif choice == "2":
                Core.mode=64000
                menu = True
                break
            else:
                c = " choose 1 or 2"
                print(colors,red,c)
        while Core.menu2 is not True:
            choice = input("\033[31]"+"\n1 - Local Area Network \n2 - Global Network\n")
            if choice == "1":
                Core.network_speed=0.05
                menu2=True
                break
            elif choice == "2":
                Core.network_speed=0.3
                menu2 = True
                break
            else:
                p = "INVALID, Choose 1 or 2"
                print(colors,red,p)

    def Start_Scan(self, port_start, port_end):
        Core.f = open(Core.ipurl, "a")
        try:
            for x in range(port_start,port_end):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                res = sock.connect_ex((Core.ipurl,x))
                if res is 0:
                    tmp="Port",x,"is open", socket.getservbyport(x)
                    tmp1=str(tmp[0])+" "+str(tmp[1])+" "+str(tmp[2])+" "+str(tmp[3])
                    print(colors.green,tmp1)
                    Core.f.write(str(tmp)+"\n")
            Core.f.close()
        except Exception as e:
            print (e)
try:
    scan = Core()
    scan.GetData(input("\033[31m"+"Input Target IP or URL\n"))
    print(colors.red,"Range:",Core.mode,"\n Target:",Core.ipurl,"\n Scanning speed:",Core.network_speed,colors.end)
    print(colors.bold,"Please wait",colors.end)
    for count in range(0,Core.mode):

        time.sleep(Core.network_speed)
        _thread.start_new_thread(scan.Start_Scan, (count,count+1))
        if count > Core.mode:
            exit(0)
except Exception as e:
    print (e)
