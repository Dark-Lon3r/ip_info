import requests
from pyfiglet import Figlet
import folium
import sys

def get_info_by_ip(ip='127.0.0.1'):
	try:
		response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

		data = {
			'[IP]': response.get('query'),
			'[Int prov]': response.get('isp'),
			'[Org]': response.get('org'),
			'[Country]': response.get('country'),
			'[Region Name ]': response.get('regionName'),
			'[City]': response.get('city'),
			'[ZIP]': response.get('zip'),
			'[Lat]': response.get('lat'),
			'[Lon]': response.get('lon'),
		}

		for k, v in data.items():
			print(f'{k} : {v}')

		area = folium.Map(location=[response.get('lat'), response.get('lon')])
		area.save(f'{response.get("query")}_{response.get("city")}.html')

	except requests.exceptions.ConnectionError:
		print('[!] Please check your connection!')


def main():
	preview_text = Figlet(font='slant')
	print(preview_text.renderText('IP INFO'))
	print('\t\t###By_DARK###')
	try:
		ip = input('Please enter a target IP: ')
		get_info_by_ip(ip=ip)
	except KeyboardInterrupt:
		print('\n[+] Cancellation...')


if __name__ == '__main__':
	main()