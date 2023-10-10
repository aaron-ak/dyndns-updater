import requests
from config import *

def main():
    if "ipv6Service" in globals():
        ipv6 = getIp(ipv6Service)
        updateDynDns(updateUrl,ipv6,dynDnsHostName,username,password)
    if "ipv4Service" in globals(): 
        ipv4 = getIp(ipv4Service)
        updateDynDns(updateUrl,ipv4,dynDnsHostName,username,password)

def getIp(ipService):
    return(requests.get(ipService).text) 

def updateDynDns(updateUrl,ipAddress,dynDnsHostName,username,password):
    updateUrl = updateUrl.replace("<dynDnsHostName>",dynDnsHostName).replace("<username>",username).replace("<password>",password).replace("<ipAddress>",str(ipAddress)).replace("\n","").replace(" ","")
    updateResponse = requests.get(updateUrl).text
    if "good" or "nochg" in updateResponse:
        print("Update successful: " + updateResponse)
    else:
        print("Update unsuccessful: " + updateResponse)

if __name__ == "__main__":
    main()