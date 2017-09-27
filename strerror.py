#!/usr/bin/python3
import sys
import os
import errno

def main():
    # Check arguments
    if len(sys.argv) < 2:
        print('Usage: strerror.py [errno]')
        sys.exit(-1)
    else:
        errno_int = 0
        errno_name = 'INVALID'

        # Check if the value is a valid number
        try:
            errno_int = int(sys.argv[1])
        except:
            print('Error: errno provided is an invalid number.')
            sys.exit(-1)

        # Check if the value is a valid errno value
        try:
            errno_name = errno.errorcode[errno_int]
        except:
            print('Error: errno value provided is invalid.')
            sys.exit(-1)

        # Print errno value
        print('errno %d = %s (%s)' % (errno_int, errno_name, os.strerror(errno_int)))

if __name__ == '__main__':
    main()
