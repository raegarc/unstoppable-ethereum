from urllib.request import Request, urlopen 
import json								 
import logging							  
from sys import argv						
from subprocess import Popen as popen	   
from time import sleep					  


def get_hashrate(url):
	while True:
		req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})								  
		info = json.loads(urlopen(req).read().decode('utf-8'))									 
		if info['status']:																		 
			return int(info['data'])															 

		else:																					  
			logging.error('Nanopool API: '+ info['error'] + ', trying again in 30 seconds')		
			sleep(30)
		
		
def check_hashrate(url):
	"""
	insert anything you like here
	it can be on multiple lines. describe 
	the whole function.
	"""
	count = 0
	while True:											
		if get_hashrate(url) == 0:													
			count += 1														 
			logging.warning('Nanopool Api: Hashrate seems to be zero')		 
		
		else:
			count = 0
			
		if count == 2:														 
			popen('taskkill /f /im {}'.format(path))									   
			sleep(10)
			popen(path + ' ' + args)										   
			count = 0														  

		sleep(delay)

	
if len(argv) == 6: 
	path, name, args, wallet, delay = argv[1:]
	delay *= 60
	popen(path + ' ' + args)
	sleep(delay)														   
	check_hashrate('https://api.nanopool.org/v1/eth/hashrate/' + wallet) 

else:
	logging.critical('not enough arguments')
	exit(1)
