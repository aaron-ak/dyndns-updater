import requests
from config import *
import logging
from logging.handlers import RotatingFileHandler


def initiateLogger():
    logging.basicConfig(
        handlers=[RotatingFileHandler('/tmp/dyndns.log', maxBytes=100000, backupCount=2)],
        level=logging.DEBUG,   # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Create a logger
    logger = logging.getLogger('dyndns-updater')
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
    successful = False
    for message in successMessage:
        if message in updateResponse:
            logging.info("Update successful: " + updateResponse)
            successful = True
    if successful != True:
        logging.error("Update unsuccessful: " + updateResponse)

if __name__ == "__main__":
    initiateLogger()
    main()