#!/usr/bin/env python
import commands
package = 'git'

def query_package(package):
    status = commands.getstatusoutput("git --version " + package)
    if not status[0]:
        print(status[1]) # package is installed
        print "Proceed"
    else:
        print "Build fail"

    status = commands.getstatusoutput("python --version " + package)
    if not status[0]:
        print(status[1]) # package is installed
        print "Proceed"
    else:
        print "Build fail"

def main():
	query_package(package)

if __name__ == '__main__':
	main()