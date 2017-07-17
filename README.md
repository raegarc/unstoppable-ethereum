# Unstoppable Ethereum
A python script for your ethereum miner and nanopool that don't allow your rig to stop

<b>Requirements</b>

<ul>
<li>A Windows machine (only tested on Win10 x64)</li>
<li><a href="https://github.com/Genoil/cpp-ethereum">An Ethereum miner (tested on genoil)</a></li>
<li><a href="https://eth.nanopool.org/">Nanopool</a></li>
<li><a href="https://www.python.org/downloads/release/python-362/">Python 3.6</a></li>
</ul>

<b>How it works</b>

The script gets the hashrate of your rig from the nanopool api, if the hashrate is zero that means the miner is not working and it restarts.
If you want a more in depth explanation see the source code that is all commented.

<b>How to install</b>


<ul>
<li>Install Python 3.6</li>
<li>Drop the two scripts on your miner folder</li>
<li>Edit the batch file like is explained in the comments</li>
<li>Create a shortcut of the batch file on where you want</li>
</ul>
