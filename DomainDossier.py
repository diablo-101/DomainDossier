import sys
import whois
import requests
import socket
from ipwhois import IPWhois
import argparse
from prettytable import PrettyTable

# ASCII Art for "DomainDossier"
print("""
  _____                        _       _____                _           
 |  __ \                      (_)     |  __ \              (_)          
 | |  | | ___  _ __ ___   __ _ _ _ __ | |  | | ___  ___ ___ _  ___ _ __ 
 | |  | |/ _ \| '_ ` _ \ / _` | | '_ \| |  | |/ _ \/ __/ __| |/ _ \ '__|
 | |__| | (_) | | | | | | (_| | | | | | |__| | (_) \__ \__ \ |  __/ |   
 |_____/ \___/|_| |_| |_|\__,_|_|_| |_|_____/ \___/|___/___/_|\___|_|   
                                                      𝕓𝕪 𝕕𝕚𝕒𝕓𝕝𝕠
                                                      
""")

def get_domain_info(domain_name):
    try:
        w = whois.whois(domain_name)
        response = requests.get(f"http://{domain_name}")
        ip_address = socket.gethostbyname(domain_name)
        obj = IPWhois(ip_address)
        asn_info = obj.lookup_rdap(depth=1)
        hosting_provider = asn_info['asn_description']
        real_hostname = socket.gethostbyaddr(ip_address)[0]

        domain_info = {
            "nameservers": w.name_servers,
            "creation_date": w.creation_date,
            "expiration_date": w.expiration_date,
            "http_status_code": response.status_code,
            "ip_address": ip_address,
            "web_server": response.headers['Server'] if 'Server' in response.headers else 'Unknown',
            "hosting_provider": hosting_provider,
            "real_hostname": real_hostname
        }

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    return domain_info

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get domain information.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d', '--domain', help='The domain to get information for.')
    group.add_argument('-w', '--wordlist', help='A file containing a list of domains to get information for.')
    parser.add_argument('-o', '--output', help='The file to save the output to.')
    args = parser.parse_args()

    if args.domain:
        domain_info = get_domain_info(args.domain)
        if domain_info is not None:
            x = PrettyTable()
            x.field_names = ["Information", "Value"]
            for key, value in domain_info.items():
                x.add_row([key, value])
                x.add_row(["-", "-"])  # Add a separator row
            print(x)
            if args.output:
                with open(args.output, 'w') as f:
                    f.write(str(x))
        else:
            print("Could not get domain information.")
    elif args.wordlist:
        with open(args.wordlist, 'r') as f:
            for line in f:
                domain_name = line.strip()
                print(f"\nGetting info for {domain_name}...")
                domain_info = get_domain_info(domain_name)
                if domain_info is not None:
                    x = PrettyTable()
                    x.field_names = ["Information", "Value"]
                    for key, value in domain_info.items():
                        x.add_row([key, value])
                        x.add_row(["-", "-"])  # Add a separator row
                    print(x)
                    if args.output:
                        with open(args.output, 'a') as f:
                            f.write(f"\nGetting info for {domain_name}...\n")
                            f.write(str(x))
                else:
                    print("Could not get domain information.")
