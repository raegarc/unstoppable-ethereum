from urllib.request import Request, urlopen                                                     #Needed to make the requests to the nanopool api
import json                                                                                     #Needed to create json objects with the data from the api
import logging                                                                                  #Needed for the error logs
from sys import argv                                                                            #Needed to manage the user arguments
from subprocess import Popen as popen                                                           #Nedded to manage subprocesses like ethminer.exe ("as popen" with lowercase just for readibility)
from time import sleep                                                                          #Needde to manage pauses


count = 0                                                                                       #Counts the number of times that the nanopool api reports 0 Hashes/s


def getArguments():

    "Manage the arguments that the user inputs on the terminal"
    
    #Arg0 -> Full path to ethminer.exe
    #Arg1 -> Exact name of the process
    #Arg2 -> Ethminer.exe arguments
    #Arg3 -> Ethereum adress
    #Arg4 -> Treshold minutes of the check cicle 

    arguments = argv[1:]                                                                        #Store the arguments on a variable

    path = arguments[0]                                                                         #Store the full path to ethminer.exe on the path variable
    name = arguments[1]                                                                         #Store the exact name of the process on the name variable
    args = arguments[2]                                                                         #Store the ethminer.exe arguments on the args variable
    url = arguments[3]                                                                          #Store the ethereum adress on the url variable
    time = arguments[4]                                                                         #Store the treshold minutes of the check cicle on the time variable

    path = '"' + path + '"'                                                                     #Add quotation marks to the variable path
    url = "https://api.nanopool.org/v1/eth/hashrate/" + url                                     #Adds the api part of the url to the variable url
    time = int(time) * 60                                                                       #Multiplies the time by 60 to turn it into seconds


    return [path,name,args,url,time]                                                            #Returns the treated arguments in a array
    


def getData( url ):

    "Request data from nanopool api"

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})                                   #Requests the url like Mozilla 5.0 to avoid http error 403

    info = json.loads(urlopen(req).read().decode('utf-8'))                                      #Creates the json object "info" with the data from the api

    if info['status']:                                                                          #If didn't occur errors              
        return float(info['data'])                                                              #Returns the hashrate


    else:                                                                                       #If did occur error
        logging.error('Nanopool API: '+ info['error'] + ', trying again in 30 seconds')         #Logs the error

        sleep(30)                                                                               #Waits 30 seconds

        return getData( getArguments()[3] )                                                     #Retry to get the information



def check (count):

    "Check when to restart ethminer.exe"

    hashrate = getData(getArguments()[3])                                                       #Receives the Hashrate data from getData
    
    if hashrate > 0:                                                                            #If the hashrate is more than 0

        count = 0                                                                               #Sets the count variable to 0


    elif hashrate == 0:                                                                         #If the hashrate is 0

        count = count + 1                                                                       #Adds 1 to the count variable

        logging.warning('Nanopool Api: Hashrate seems to be zero')                              #Logs a warning
        

    if count == 2:                                                                              #If the hashrate is 2

        popen('taskkill /f /im ' + getArguments()[1])                                           #Kills ethminer.exe

        sleep(10)                                                                               #Waits 10 seconds

        cmdInput = getArguments()[0] + " " + getArguments()[2]                                  #Creates a string with the command and parameters to ethminer.exe
        popen(cmdInput)                                                                         #Runs the cmdInput string and starts ethminer.exe

        count = 0                                                                               #Sets the count variable to 0


    sleep(getArguments()[4])                                                                    #Waits the time chosed by the user

    check(count)                                                                                #Runs the function check



cmdInput = getArguments()[0] + " " + getArguments()[2]                                          #Creates a string with the command and parameters to ethminer.exe
popen(cmdInput)                                                                                 #Runs the cmdInput string and starts ethminer.exe

sleep(getArguments()[4])                                                                        #Waits the time chosed by the user

check(count)                                                                                    #Runs the function check
