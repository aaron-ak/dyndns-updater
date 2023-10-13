# Dynamic DNS Updater Script

## Introduction
As my router is not performing Dynamic DNS (DynDNS) Updates as it should, I've ended up with this python script. This script is to update Dynamic DNS (DynDNS) records using an external IP service. The script is designed to work with both IPv4 and IPv6 addresses and is intended to help automate the process of keeping your DynDNS hostname up to date with your current IP address.

## Prerequisites
Before using the script, ensure you have the following prerequisites:

- Python 3.x installed on your system.
- - requirements.txt must be installed. You can install it using pip:
  ```bash
  pip install -r requirements.txt
  ````
- Access to a DynDNS service provider that supports updates via HTTP requests.
- Your DynDNS hostname, username, and password from your service provider.

## Configuration
To configure the script, follow these steps:
Copy the config.py.dist file to config.py and enter the following information:

- ipv6Service: The URL of the IPv6 IP service (optional if you don't need IPv6 support).
- ipv4Service: The URL of the IPv4 IP service.
- updateUrl: The URL provided by your DynDNS service provider for updating your DNS records. This URL should contain placeholders for <dynDnsHostName>, <username>, <password>, and <ipAddress>.
- dynDnsHostName: Your DynDNS hostname.
- username: Your DynDNS username.
- password: Your DynDNS password.
- successMessage: a list containing one or more strings that are expected to be returned by the dyndns service in case of a successful update. 


Save the config.py file after making the necessary changes.

## Running the Script
Open a terminal or command prompt. Navigate to the directory where the script is located.
Run the script using the following command:

```bash
python dyndns.py
```

The script will fetch your current IP address from the specified IP services (IPv4 and/or IPv6) and attempt to update your DynDNS hostname with the retrieved IP address. The script will display a success or failure message depending on the outcome of the update.

### CronJob
```bash
0 */6 * * * /usr/bin/python3 /path/to/dyndns.py   
```
