# NOTE: Please only run this on YOUR OWN servers

import urllib
import ssl

subs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
        "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
        "w", "x", "y", "z"]

# bypass SSL check
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

i = 0
scheme = "http://"
topLevel = ".[yoursitehere].com"
print " -------- " + "Subdomains of " + topLevel + " -------- "

while i < 26:
    subDomain = subs[i]
    try:
        urllib.urlopen(scheme+subDomain+topLevel, context=ctx).getcode()
        print subs[i] + " is an active subdomain of " + topLevel
        i += 1
    except:
        print subs[i] + " is not a subdomain"
        i += 1
