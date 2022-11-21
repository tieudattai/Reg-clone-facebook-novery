import requests
from random import choice

def cre_ip():
	text = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=5000&country=all&ssl=all&anonymity=all').text
	list_ip = text.split('\r\n')
	return choice(list_ip)

# print(cre_ip())