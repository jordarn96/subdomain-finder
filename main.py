# NOTE: Please only run this on YOUR OWN servers

import urllib
import ssl

# bypass SSL check
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# open text file of 
f = open("words.txt")
wordLines = f.readlines()
# count the lines, this might not be the most efficient way
lineCount = len(open("words.txt").readlines())

scheme = "http://"
topLevel = ".[yoursitehere].com"

print " -------- " + "Subdomains of " + topLevel + " -------- "

i = 0
while i < lineCount:
    subDomain = wordLines[i]
    try:
        urllib.urlopen(scheme+subDomain+topLevel, context=ctx).getcode()
        print wordLines[i] + " is an active subdomain of " + topLevel
        i += 1
    except:
        print wordLines[i] + " is not a subdomain"
        i += 1
    else:
        print "Finished searching"
