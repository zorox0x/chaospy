#!/usr/bin/env python
import requests,json,os,argparse

#Colors
red = '\033[91m'
green = '\33[32m'
orange = '\33[33m'
blue = '\33[34m'
grey = '\33[90m'
white = '\33[37m'
magenta = '\033[95m'
end = '\033[0m'

parser = argparse.ArgumentParser(description='Chaos Tool')

parser.add_argument('-d',dest='download',help='Download Specific Program Subdomains')
parser.add_argument('-a',dest='all_download',help='Download all programs Subdomains',action='store_true')
parser.add_argument('-l',dest='list',help='List all programs',action='store_true')
parser.add_argument('-bc',dest='list_bc',help='List BugCrowd programs',action='store_true')
parser.add_argument('-h1',dest='list_h1',help='List Hackerone programs',action='store_true')
parser.add_argument('-ext',dest='list_ext',help='List external programs',action='store_true')
parser.add_argument('-new',dest='list_new',help='List new programs',action='store_true')
parser.add_argument('-upd',dest='list_upd',help='List updated programs',action='store_true')
parser.add_argument('-dbc',dest='download_bc',help='Download BugCrowd programs',action='store_true')
parser.add_argument('-dh1',dest='download_h1',help='Download Hackerone programs',action='store_true')
parser.add_argument('-dext',dest='download_ext',help='Download external programs',action='store_true')
parser.add_argument('-dnew',dest='download_new',help='Download new programs',action='store_true')
parser.add_argument('-dupd',dest='download_upd',help='Download updated programs',action='store_true')

args = parser.parse_args()

os.system('clear')
d = args.download
a = args.all_download
l = args.list
bc = args.list_bc
h1=args.list_h1
ext=args.list_ext
new=args.list_new
upd=args.list_upd
dbc=args.download_bc
dh1=args.download_h1
dext=args.download_ext
dnew=args.download_new
dupd=args.download_upd
banner="""


          %s   _                                 
         ___| |__   __ _  ___  ___ _ __  _   _ 
        / __| '_ \ / _` |/ _ \/ __| '_ \| | | |
       %s| (__| | | | (_| | (_) \__ \ |_) | |_| |
        \___|_| |_|\__,_|\___/|___/ .__/ \__, |
                                  |_|    |___/ 
	%s  Small Tool written based on chaos from projectdiscovery.io
        %s      https://chaos.projectdiscovery.io/
	%s  *Author -> 0x0x (https://twitter.com/dr_0x0x)*                                                    
%s \n"""%(blue,red,orange,grey,grey,end)

print (banner)

url = "https://chaos-data.projectdiscovery.io/index.json"
source= requests.get(url)
data = source.json()




def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '%.2f%s' % (num, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])



def down():
    for item in data:
        if item['name'] == d:
            print(green+"[!] Program Found."+end)
            print(blue+"[!] Downloading",d, "..."+end)
            url ="https://chaos-data.projectdiscovery.io/"+d+".zip"
            resp = requests.get(url)
            zname= d+".zip"
            zfile = open(zname, 'wb')
            zfile.write(resp.content)
            zfile.close()
            print(green+"[!] {} File successfully downloaded.".format(zname)+end)
def all_down():
    for item in data:
        print(blue+"[!] Downloading {}                   ".format(item['name']),end="\r"+end)
        resp = requests.get(item['URL'])
        zname= item['name']+".zip"
        zfile = open(zname, 'wb')
        zfile.write(resp.content)
        zfile.close()
    print(green+"[!] All Domains successfully downloaded."+end)

def info():
    new = 0
    h = 0
    b= 0
    ext = 0
    ch = 0
    sub = 0
    for item in data:
        if item['is_new'] is True:
            new += 1
        if item['platform'] == "hackerone":
            h +=1
        elif item['platform'] == "bugcrowd":
            b += 1
        else:
            ext += 1
        if item['change'] != 0:
            ch +=1
        sub = sub +item['count']

    print(red+"[!] Programs Last Updated {}".format(item['last_updated'][:10]))
    print(blue+"[!] {} Subdomains.".format(human_format(sub)))
    print(white+"[!] {} Programs.".format(len(data))+end)
    print(green+"[!] {} New programs.".format(new)+end)
    print(red+"[!] {} HackerOne programs.".format(h)+end)
    print(orange+"[!] {} BugCrowd programs.".format(b)+end)
    print(magenta+"[!] {} External programs.".format(ext)+end)
    print(blue+"[!] {} Programs changes.".format(ch)+end)
       

def ls():
    print(blue+"[!] Listing all Programs. "+end)
    for item in data:
        print (blue+item['name']+end)

def bugcrowd():
    print(orange+"[!] Listing Bugcrowd Programs."+end)
    for item in data:
        if item['platform'] == "bugcrowd":
            print (orange+item['name']+end)

def hackerone():
    print(red+"[!] Listing HackerOne Programs."+end)
    for item in data:
        if item['platform'] == "hackerone":
            print (red+item['name']+end)

def extern():
    print(magenta+"[!] Listing External Programs."+end)
    for item in data:
        if item['platform'] == "":
            print (magenta+item['name']+end)
def list_new():
    print(magenta+"[!] Listing New Programs."+end)
    for item in data:
        if item['is_new'] is True:
            print (magenta+item['name']+end)
def list_upd():
    print(magenta+"[!] Listing Updated Programs."+end)
    for item in data:
        if item['change'] != 0:
            print (magenta+item['name']+end)
def down_bc():
    for item in data:
        if item['platform'] == "bugcrowd":
            print(orange+"[!] Downloading {}                   ".format(item['name']),end="\r"+end)
            resp = requests.get(item['URL'])
            zname= item['name']+".zip"
            zfile = open(zname, 'wb')
            zfile.write(resp.content)
            zfile.close()
    print(green+"[!] All BugCrowd programs successfully downloaded."+end)


def down_h1():
    for item in data:
        if item['platform'] == "hackerone":
            print(red+"[!] Downloading {}                   ".format(item['name']),end="\r"+end)
            resp = requests.get(item['URL'])
            zname= item['name']+".zip"
            zfile = open(zname, 'wb')
            zfile.write(resp.content)
            zfile.close()
    print(green+"[!] All HackerOne programs successfully downloaded."+end)


def down_ext():
    for item in data:
        if item['platform'] == "":
            print(magenta+"[!] Downloading {}                   ".format(item['name']),end="\r"+end)
            resp = requests.get(item['URL'])
            zname= item['name']+".zip"
            zfile = open(zname, 'wb')
            zfile.write(resp.content)
            zfile.close()
    print(green+"[!] All External programs successfully downloaded."+end)

def down_new():
    for item in data:
        if item['is_new'] is True:
            print(magenta+"[!] Downloading {}                   ".format(item['name']),end="\r"+end)
            resp = requests.get(item['URL'])
            zname= item['name']+".zip"
            zfile = open(zname, 'wb')
            zfile.write(resp.content)
            zfile.close()
    print(green+"[!] All New prgrams successfully downloaded."+end)
def down_upd():
    for item in data:
        if item['change'] != 0:
            print(magenta+"[!] Downloading {}                   ".format(item['name']),end="\r"+end)
            resp = requests.get(item['URL'])
            zname= item['name']+".zip"
            zfile = open(zname, 'wb')
            zfile.write(resp.content)
            zfile.close()
    print(green+"[!] All Updated programs successfully downloaded."+end)
def main():
    info()
    if d is not None:
        down()
    elif a :
        all_down()
    elif l :
        ls()
    elif bc:
        bugcrowd()
    elif h1:
        hackerone()
    elif ext:
        extern()
    elif new:
        list_new()
    elif upd:
        list_upd()
    elif dbc:
        down_bc()
    elif dh1:
        down_h1()
    elif dext:
        down_ext()
    elif dnew:
        down_new()
    elif dupd:
        down_upd()
    else:
        print(red+"[!] Type python3 chaospy.py -h for help.")

if __name__ == '__main__':
    main()
