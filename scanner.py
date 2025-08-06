import socket #module is  used for creating network sockets, allowing the script to establish TCP connections to each port and see if they open or closed
import sys
import pyfiglet
from datetime import datetime

# This is a basic network scanner using Python's socket library to perform scans.
ascii_banner = pyfiglet.figlet_format("RIGBY SCANNER")
print(ascii_banner)

# Define target based on user input.
if len(sys.argv) == 2:
    
    #get target from cmd arguments.... hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
    
else:
    print("Invalid arguments")
    print("Syntax: python scanner.py <ip address or hostname>")
    sys.exit()


print("-" * 50)
print(f"Scanning target: {target}")
print(f"Time started: {str(datetime.now())}")
print("-" * 50)

# Code to loop through ports:
try:
   
   for port in range(1, 200 ):#socket is an endpoint for sending and receiving data over a network
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket for each port
      socket.setdefaulttimeout(1)  # Set timeout for the socket to 1s to prevent looping in a closed port

      result = s.connect_ex((target, port))#connect target IP on current port number
      if result == 0:
          print(f"Port {port} is open".format(port))
      s.close()
      
except KeyboardInterrupt:
   print("\nExiting program")
   sys.exit()
except socket.gaierror:
     print("\n Hostname Could Not Be Resolved !!!!")
     sys.exit()
except socket.error:
    print("Could not connect to server")
    sys.exit()
      