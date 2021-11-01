#!/usr/bin/python3
import requests
import time,os,argparse

#Colors
Black        = "\033[30m"
Red          = "\033[31m"
Green        = "\033[32m"
Yellow       = "\033[33m"
Blue         = "\033[34m"
Magenta      = "\033[35m"
Cyan         = "\033[36m"
LightGray    = "\033[37m"
DarkGray     = "\033[90m"
LightRed     = "\033[91m"
LightGreen   = "\033[92m"
LightYellow  = "\033[93m"
LightBlue    = "\033[94m"
LightMagenta = "\033[95m"
LightCyan    = "\033[96m"
White        = "\033[97m"
Default      = '\033[0m'

banner= """

          %s             ________                     ____
                      / ____/ /_  ____ _____  _____/ __ \__  __
                     / /   / __ \/ __ `/ __ \/ ___/ /_/ / / / /
                    / /___/ / / / /_/ / /_/ (__  ) ____/ /_/ /
                    \____/_/ /_/\__,_/\____/____/_/    \__, /
                                                      /____/
          %s  Small Tool written based on chaos from projectdiscovery.io
          %s          https://chaos.projectdiscovery.io/
          %s    *Author -> Moaaz (https://twitter.com/photonbo1t)*

   %s \n """%(LightGreen,Yellow,DarkGray,DarkGray,Default)

parser = argparse.ArgumentParser(description='ChaosPY Tool')

parser.add_argument('-list',dest='list',help='List all programs',action='store_true')
parser.add_argument('--list-bugcrowd',dest='list_bugcrowd',help='List BugCrowd programs',action='store_true')
parser.add_argument('--list-hackerone',dest='list_hackerone',help='List Hackerone programs',action='store_true')
parser.add_argument('--list-intigriti',dest='list_intigriti',help='List Intigriti programs',action='store_true')
parser.add_argument('--list-external',dest='list_external',help='List Self Hosted programs',action='store_true')
parser.add_argument('--list-swags',dest='list_swags',help='List programs Swags Offers',action='store_true')
parser.add_argument('--list-rewards',dest='list_rewards',help='List programs with rewards',action='store_true')
parser.add_argument('--list-norewards',dest='list_norewards',help='List programs with no rewards',action='store_true')
parser.add_argument('--list-new',dest='list_new',help='List new programs',action='store_true')
parser.add_argument('--list-updated',dest='list_updated',help='List updated programs',action='store_true')

parser.add_argument('-download',dest='download',help='Download Specific Program')

parser.add_argument('--download-all',dest='download_all',help='Download all programs',action='store_true')
parser.add_argument('--download-bugcrowd',dest='download_bugcrowd',help='Download BugCrowd programs',action='store_true')
parser.add_argument('--download-hackerone',dest='download_hackerone',help='Download Hackerone programs',action='store_true')
parser.add_argument('--download-intigriti',dest='download_intigriti',help='Download intigriti programs',action='store_true')
parser.add_argument('--download-external',dest='download_external',help='Download external programs',action='store_true')
parser.add_argument('--download-swags',dest='download_swags',help='Download programs Swags Offers',action='store_true')
parser.add_argument('--download-rewards',dest='download_rewards',help='Download programs with rewards',action='store_true')
parser.add_argument('--download-norewards',dest='download_norewards',help='Download programs with no rewards',action='store_true')
parser.add_argument('--download-new',dest='download_new',help='Download new programs',action='store_true')
parser.add_argument('--download-updated',dest='download_updated',help='Download updated programs',action='store_true')

args = parser.parse_args()

os.system('clear')
ls = args.list
list_bugcrowd = args.list_bugcrowd
list_hackerone=args.list_hackerone
list_intigriti=args.list_intigriti
list_external=args.list_external
list_swags=args.list_swags
list_rewards=args.list_rewards
list_norewards=args.list_norewards
list_new=args.list_new
list_updated=args.list_updated

download = args.download

download_all= args.download_all
download_bugcrowd = args.download_bugcrowd
download_hackerone=args.download_hackerone
download_intigriti=args.download_intigriti
download_external=args.download_external
download_swags=args.download_swags
download_rewards=args.download_rewards
download_norewards=args.download_norewards
download_new=args.download_new
download_updated=args.download_updated

print (banner)

def getdata():
    url = "https://chaos-data.projectdiscovery.io/index.json"
    source= requests.get(url)
    return source.json()

def info():
    new = 0
    hackerone = 0
    bugcrowd= 0
    intigriti = 0
    external = 0
    changed = 0
    subdomains = 0
    rewards= 0
    norewards= 0
    swags= 0

    for item in getdata():
        if item['is_new'] is True:
            new += 1
        if item['platform'] == "hackerone":
            hackerone +=1
        if item['platform'] == "bugcrowd":
            bugcrowd += 1
        if item['platform'] == "intigriti":
            intigriti += 1
        else:
            external += 1
        if item['change'] != 0:
            changed +=1
        subdomains = subdomains +item['count']
        if item['bounty'] is True:
            rewards += 1
        else:
            norewards += 1
        if 'swag' in item:
            swags +=1

    print(White+"[!] Programs Last Updated {}".format(item['last_updated'][:10]))
    print(LightGreen+"[!] {} Subdomains.".format(subdomains))
    print(Green+"[!] {} Programs.".format(len(getdata()))+Default)
    print(LightCyan+"[!] {} Programs changed.".format(changed)+Default)
    print(Blue+"[!] {} New programs.".format(new)+Default)
    print(LightGray+"[!] {} HackerOne programs.".format(hackerone)+Default)
    print(Magenta+"[!] {} Intigriti programs.".format(intigriti)+Default)
    print(Yellow+"[!] {} BugCrowd programs.".format(bugcrowd)+Default)
    print(LightGreen+"[!] {} Self hosted programs.".format(external)+Default)
    print(Cyan+"[!] {} Programs With Rewards.".format(rewards)+Default)
    print(Yellow+"[!] {} Programs Offers Swags.".format(swags)+Default)
    print(LightRed+"[!] {} No Rewards programs.".format(norewards)+Default)

def down():
    print(download)
    for item in getdata():
        if item['name'] == download:
            print(LightGreen+"[!] Program Found."+Default)
            print(Cyan+"[!] Downloading",download, "..."+Default)
            url = item['URL']
            resp = requests.get(url)
            zname= download+".zip"
            zfile = open(zname, 'wb')
            zfile.write(resp.content)
            zfile.close()
            print(LightGreen+"[!] {} File successfully downloaded.".format(zname)+Default)

def list_all():
    print(White+"[!] Listing all Programs. \n"+Default)
    for item in getdata():
        print (Blue+item['name']+Default)

def bugcrowd():
    print(Yellow+"[!] Listing Bugcrowd Programs."+Default)
    for item in getdata():
        if item['platform'] == "bugcrowd":
            print (Yellow+item['name']+Default)

def hackerone():
    print(White+"[!] Listing HackerOne Programs."+Default)
    for item in getdata():
        if item['platform'] == "hackerone":
            print (White+item['name']+Default)

def intigriti():
    print(Magenta+"[!] Listing intigriti Programs."+Default)
    for item in getdata():
        if item['platform'] == "hackerone":
            print (Magenta+item['name']+Default)

def external():
    print(Cyan+"[!] Listing External Programs."+Default)
    for item in getdata():
        if item['platform'] == "":
            print (Cyan+item['name']+Default)

def swags():
    print(LightGreen+"[!] Listing Swag Programs."+Default)
    for item in getdata():
        if 'swag' in item:
            print (LightGreen+item['name']+Default)

def rewards():
    print(Cyan+"[!] Listing Rewards Programs."+Default)
    for item in getdata():
        if item['bounty'] == True:
            print (Cyan+item['name']+Default)

def norewards():
    print(Red+"[!] Listing NORewards Programs."+Default)
    for item in getdata():
        if item['bounty'] == False:
            print (Red+item['name']+Default)

def new():
    print(LightGreen+"[!] Listing New Programs."+Default)
    for item in getdata():
        if item['is_new'] == True:
            print (LightGreen+item['name']+Default)

def changed():
    print(Cyan+"[!] Listing Updated Programs."+Default)
    for item in getdata():
        if item['change'] != 0:
            print (Cyan+item['name']+Default)

def all_down():
    for item in getdata():
        print(Blue+"[!] Downloading {}                   ".format(item['name']),end="\r"+Default)
        resp = requests.get(item['URL'])
        zname= item['name']+".zip"
        zfile = open(zname, 'wb')
        zfile.write(resp.content)
        zfile.close()
    print(LightGreen+"[!] All Programs successfully downloaded."+Default)

def bc_down():
    for item in getdata():
        if item['platform'] == "bugcrowd":
            print(Yellow+"[!] Downloading {}                   ".format(item['name']),end="\r"+Default)
            resp = requests.get(item['URL'])
            zname= item['name']+".zip"
            zfile = open(zname, 'wb')
            zfile.write(resp.content)
            zfile.close()
    print(LightGreen+"[!] All BugCrowd programs successfully downloaded."+Default)

def h1_down():
    for item in getdata():
        if item['platform'] == "hackerone":
            print(White+"[!] Downloading {}                   ".format(item['name']),end="\r"+Default)
            resp = requests.get(item['URL'])
            zname= item['name']+".zip"
            zfile = open(zname, 'wb')
            zfile.write(resp.content)
            zfile.close()
    print(LightGreen+"[!] All HackerOne programs successfully downloaded."+Default)

def intigriti_down():
    for item in getdata():
        if item['platform'] == "intigriti":
            print(Magenta+"[!] Downloading {}                   ".format(item['name']),end="\r"+Default)
            resp = requests.get(item['URL'])
            zname= item['name']+".zip"
            zfile = open(zname, 'wb')
            zfile.write(resp.content)
            zfile.close()
    print(LightGreen+"[!] All intigriti programs successfully downloaded."+Default)

def external_down():
    for item in getdata():
        if item['platform'] == "":
            print(White+"[!] Downloading {}                   ".format(item['name']),end="\r"+Default)
            resp = requests.get(item['URL'])
            zname= item['name']+".zip"
            zfile = open(zname, 'wb')
            zfile.write(resp.content)
            zfile.close()
    print(LightGreen+"[!] All External programs successfully downloaded."+Default)

def new_down():
    for item in getdata():
        if item['is_new'] is True:
            print(Cyan+"[!] Downloading {}                   ".format(item['name']),end="\r"+Default)
            resp = requests.get(item['URL'])
            zname= item['name']+".zip"
            zfile = open(zname, 'wb')
            zfile.write(resp.content)
            zfile.close()
    print(LightGreen+"[!] All New programs successfully downloaded."+Default)

def updated_down():
    for item in getdata():
        if item['change'] != 0:
            print(Blue+"[!] Downloading {}                   ".format(item['name']),end="\r"+Default)
            resp = requests.get(item['URL'])
            zname= item['name']+".zip"
            zfile = open(zname, 'wb')
            zfile.write(resp.content)
            zfile.close()
    print(LightGreen+"[!] All Updated programs successfully downloaded."+Default)

def swags_down():
    for item in getdata():
        if 'swag' in item:
            print(LightYellow+"[!] Downloading {}                   ".format(item['name']),end="\r"+Default)
            resp = requests.get(item['URL'])
            zname= item['name']+".zip"
            zfile = open(zname, 'wb')
            zfile.write(resp.content)
            zfile.close()
    print(LightGreen+"[!] All Swags programs successfully downloaded."+Default)

def rewards_down():
    for item in getdata():
        if item['bounty'] is True:
            print(Cyan+"[!] Downloading {}                   ".format(item['name']),end="\r"+Default)
            resp = requests.get(item['URL'])
            zname= item['name']+".zip"
            zfile = open(zname, 'wb')
            zfile.write(resp.content)
            zfile.close()
    print(LightGreen+"[!] All Bounty programs successfully downloaded."+Default)

def norewards_down():
    for item in getdata():
        if item['bounty'] is False:
            print(LightRed+"[!] Downloading {}                   ".format(item['name']),end="\r"+Default)
            resp = requests.get(item['URL'])
            zname= item['name']+".zip"
            zfile = open(zname, 'wb')
            zfile.write(resp.content)
            zfile.close()
    print(LightGreen+"[!] All Norewards programs successfully downloaded."+Default)

def main():
    info()
    if download is not None:
        down()
    if download_all :
        all_down()
    if ls :
        list_all()
    if list_bugcrowd:
        bugcrowd()
    if list_hackerone:
        hackerone()
    if list_external:
        external()
    if list_swags:
    	swags()
    if list_rewards:
    	rewards()
    if list_norewards:
    	norewards()
    if list_new:
        new()
    if list_updated:
        changed()
    if download_bugcrowd:
        bc_down()
    if download_hackerone:
        h1_down()
    if download_intigriti:
        intigriti_down()
    if download_external:
        external_down()
    if download_swags:
        swags_down()
    if download_rewards:
        rewards_down()
    if download_norewards:
        norewards_down()
    if download_new:
        new_down()
    if download_updated:
        updated_down()

if __name__ == '__main__':
    main()
