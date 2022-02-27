# -*- coding: utf-8 -*-

#Importing Modules
import socket
import subprocess
import sys

#Importing a particular class from module
from datetime import datetime

"""
What we’re doing here is — we want to be able to know what the current date and time is. 
The reason for that is we’re going to have the script tell us how long it took to execute.
For it to be able to do that, it’s going to need to know, here’s where I started, here’s when I ended.
"""
#Blank your screen
subprocess.call('clear', shell=True)

"""
 Next, we want to blank the screen. 
 If there’s anything on the screen, you want to make that go away. 
 We’re doing that here with basically a clear-screen-type function.
"""

#Ask for input
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

"""
We’re defining remoteServer here as this particular function, and then we say, enter a remote host to scan.
The remoteServerIP is going to be the result of what you enter when it asks you to enter the remote host to scan. 
This could be in the form of an IP address or URL or whatever it is you happen to be wanting to scan.
"""

#Print a nice banner with information on which host we are about to scan
print("_" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("_" *60)

"""
Next, we’re going to print a banner for us or give us some information about what we’re doing.
We basically just say, please wait as we scan the 
remote host and then whatever the IP is we entered when we first started the scan.
"""
#Check the date and time the scan was started
t1 = datetime.now()

"""
Next, we’re going to check the date and time again because we need to know when the scan actually started.
We’re defining t1 as the current date and time. 
That way, at any point in our code, we can say t1 and it will actually tell us
what the current date and time is without us having to type out that long function again. 
That’s the purpose of doing that.
"""

#Using the range function to specify ports
#Also we will do error handling

try:
    for port in range (1,5000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
    if result ==0:
        print("Port {}:        Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

"""
We say, for port in range. 
This is what we call a for loop. In other words, it’s a way to repeat something over and over again. 
That’s what a loop is, for the range in 1–5,000. What we’re doing here is we’re going to scan all 
ports between one and 5,000. So we’re going to check that on each IP address we scan.
The next part of this is using socket. Remember that earlier we said import socket. 
Now we’re actually using that module we imported. 
Basically, we say, let’s use that to connect to something. 
The something that we’re going to connect to is whatever IP address 
it is we entered when we started this. Once we get a connection, 
we need to tell our script what to do with that connection.

In this particular example, we’re going to say Ctrl+C if we want to end the script or
stop the script from running. Or if the script is unsuccessful in connecting — maybe you
 gave it an IP address that’s not really there — then we need to tell the script 
 how to respond to us. In other words, we call that error control. We can see that 
 we’re telling it if you get a connection, go ahead and print the information 
 about that — the IP and the ports — or if you can’t connect, tell us, 
 I couldn’t connect to that IP or that server. That’s all we’re doing here.
"""

#Checking time again
t2 = datetime.now()

#Calculate the difference in time to now how long the scan took
total = t2 - t1

#Printing the information on the screen
print('Scanning Completed in in ', total)

"""
After the script is completed, we’re going to call our date function again.
We’re defining date and time now as t2. So we’re going to call t1 and t2 and say, 
take t1, whatever the date and time was, then subtract that from t2, 
which is what the date and time is now, and that will tell us how long it took 
for the script to run.

We’re going to take that number and print that in a message that says, 
scanning completed in however many seconds. 
That’s the basic functionality of the script.
"""

"""
Now, let me show you what happens when we actually run the script and give it a target.
What we see is it’s coming back and telling us specifically that this particular machine 
at this IP or URL has exactly these ports open.

That’s what a basic port scanner looks like in Python. 
If you really want to challenge yourself, what I’d like to see you do in your own time 
is see if you can figure out how to make the script not only tell us the open ports, 
but tell us what’s actually running in those ports.
"""
























