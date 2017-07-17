python 'Path to ethereum.py' 'Path to ethminer.exe' 'Exact name of the ethminer process' 'Ethminer parameters' 'Ethereum adress' 'Time between checks'
pause


:: EXAMPLE

:: python "C:\Program Files\Ethminer\ethereum.py" "C:\Program Files\Ethminer\ethminer.exe" ethminer.exe "--farm-recheck 1000 -U -S eth-eu1.nanopool.org:9999 -FS eth-eu2.nanopool.org:9999 -O 0xc5c5a034db718ce4abb6971c860d10aed74833aC" 0xc5c5a034db718ce4abb6971c860d10aed74833aC 10
:: pause

:: IMPORTANT

:: If there is any space between a parameter QUOTATION MARKS ARE NEEDED
:: If any of the parameters is not filled the script will not work properly

:: RECOMENDED PARAMETERS

:: Path to ethereum.py - Is recommended to write the full path always with quotation marks
:: Path to ethminer.exe - Is recommended to write the full path always with quotation marks, if your miner don't have a ethminer.exe you can try to change to the program you normally have in your batch file (but it's not guaranteed that it will work, so i recommend genoil miner)
:: Exact name of the ethminer process - Is normally the name of the executable but make sure searching for the process on the task manager
:: Ethminer parameters - YOU NEED TO PUT QUOTATION MARKS, these are just the parameters you use on your miner make sure you're mining on nanopool
:: Ethereum adress - Is just your ethereum adress make sure that it's right or you will be mining for another person
:: Time between checks - Is recommended 10 for normal users, but if you like you can find your perfect time, remember that are to checks before restarting to avoid false positives
