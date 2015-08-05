'''
A script for checking whether ports are opened, with little to non error checking (will maybe
be added in the future).
It uses the concurrent.futures package to check ports in parallel, so make sure you
use a version of Python that is newer then 3.2.
Written by Ronen K Aug. 2015.
This script is under public domain; feel free to do whatever you want with it.
'''
import sys
import socket
import concurrent.futures

HOSTADDR = socket.gethostbyname(socket.gethostname())

def checkport(port):
    print("Checking port {}...'.format(port), end=' ')
    
    # Create the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    if is_port_opened(sock, port):
        print("Port {} is open.".format(port))
    else:
        print()
        
def is_port_open(sock, port):
    result = sock.connect_ex((HOSTADDR, port))
    
    if result == 0:
        return True
    return False
    
def main():
    # Check arguments
    if len(sys.argv) == 3:
        min_port, max_port = int(sys.argv[1]), int(sys.argv[2])
        
        # Check ports in parallel
        with concurrent.futures.ProcessPoolExecutor() as executor:
            executor.map(checkport, range(min_port, max_port + 1))
    else:
        print("Usage: portchecker.py [min] [max]")
        exit(-1)
        
if __name__ == '__main__':
    main()
