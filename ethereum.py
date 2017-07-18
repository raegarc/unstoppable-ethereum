from urllib.request import Request, urlopen                                                     		#Needed to make the requests to the nanopool api 
import json                                                                                     		#Needed to create json objects with the data from the api								 
import logging                                                                                  		#Needed for the error logs							  
from sys import argv                                                                  		                #Needed to manage the user arguments						
from subprocess import Popen as popen                                               	                        #Nedded to manage subprocesses like ethminer.exe ("as popen" with lowercase just for readibility)	   
from time import sleep                                                                  		        #Needed to manage pauses					  


def get_hashrate(url):
	while True:												#Repeats the procedure until hashrate is returned
		req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})					#Requests the url like Mozilla 5.0 to avoid http error 403			  
		info = json.loads(urlopen(req).read().decode('utf-8'))						#Creates the json object "info" with the data from the api			 
		if info['status']:										#If didn't occur errors								 
			return int(info['data'])								#Returns the hashrate							 

		else:												#If did occur an error									  
			logging.error('Nanopool API: '+ info['error'] + ', trying again in 30 seconds')		#Logs the error		
			sleep(30)										#Waits 30 seconds
		
		
def check_hashrate(url):
	"""
	insert anything you like here
	it can be on multiple lines. describe 
	the whole function.
	"""
	count = 0												#Sets the count variable to 0
	while True:												#Makes a infinite loop for this function to run all the time
		if get_hashrate(url) == 0:									#If the hashrate is 0				
			count += 1										#Adds 1 to the count variable				 
			logging.warning('Nanopool Api: Hashrate seems to be zero')		 		#Logs a warning
		
		else:												#If the hashrate is not 0
			count = 0										#Sets the count variable to 0
			
		if count == 2:											#If the count variable is 2 (you can change it to 1 if you want to risk false positives)			 
			popen('taskkill /f /im {}'.format(path))						#Kills ethminer.exe			   
			sleep(10)										#Waits 10 seconds
			popen(path + ' ' + args)								#Starts ethminer.exe		   
			count = 0										#Sets the count variable to 0				  

		sleep(delay)											#Waits the time chosed by the user

	
if len(argv) == 6: 												#If there are enough user arguments
	path, name, args, wallet, delay = argv[1:]								#Turns the user arguments into variables
	delay = int(delay) * 60											#Multiplies the time by 60 to turn it into seconds
	popen(path + ' ' + args)										#Starts ethminer.exe
	sleep(delay)												#Waits the time chosed by the user		   
	check_hashrate('https://api.nanopool.org/v1/eth/hashrate/' + wallet) 					#Runs the check_hashrate function

else:														#If there aren't enough user arguments
	logging.critical('not enough arguments')								#Logs the error
	exit(1)													#Exits the script
