# Unstoppable Ethereum
A python script for nanopool that don't allow your rig to stop

<b>Requirements</b>

<ul>
<li>A Windows machine (tested on Win10 x64)</li>
<li>An Ethereum miner (tested on <a href="https://github.com/Genoil/cpp-ethereum">Genoil miner</a>)</li>
<li><a href="https://eth.nanopool.org/">Nanopool</a></li>
<li><a href="https://www.python.org/downloads/release/python-362/">Python 3.6</a></li>
</ul>

<b>How it works</b>

The script gets the hashrate of your rig from the nanopool api, if the hashrate is zero that means the miner is not working and it restarts.

If you want a more in depth explanation see the source code that is all commented.

<b>How to install</b>


<ul>
<li>Install Python 3.6</li>
<li>Download this files to your miner folder</li>
<li>Edit the batch file like is explained in the comments</li>
<li>Create a shortcut of the batch file on where you want</li>
</ul>

<b>This helped you?</b>

If this helped you fell free to return the favor by donating some <a href="https://eth.nanopool.org/account/0xc5c5A034db718cE4Abb6971c860D10AeD74833aC">Ethereum</a> or <a href="https://etherscan.io/address/0xc5c5a034db718ce4abb6971c860d10aed74833ac">Bitcoin</a> to me.

You can also help by improving the code, all help is appreciated!

And please upvote the<a href="https://www.reddit.com/r/EtherMining/comments/6nuuay/an_automatic_python_script_that_restarts_the/">Reddit thread</a> so more people can be helped
