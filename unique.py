# calculate unique visitors & faq readers

import sys, os

f = sys.argv[1]
f = open(f)
r = f.readlines()
f.close()

ips = {}
faqs = {}
last = {}
hits = 0
dates = {}

for line in r:
    line = line.strip()
    if "tracking" in line:
        w = line.split()
        date = w[1] + " " + w[2] + " " + w[4][:-1]
        if date not in dates:
            dates[date] = 0
        dates[date] += 1
##        print line
        i = line.find('[client ') + 8
        j = line[i:].find(']')
##        print i, j
        ip = line[i:i+j]
##        print ip
        if ip not in ips:
            ips[ip] = 0
            faqs[ip] = 0
        last[ip] = date + " " + w[3]
        ips[ip] += 1
        if "tracking_faq" in line:
            faqs[ip] += 1
        hits += 1

for ip in ips:
    print ips[ip], "page hits for", ip, "faq hits:", faqs[ip], "recent:", last[ip]

print
print "dates:"
keys = list(dates)
keys.sort()
for date in keys:
    print date, dates[date]
print
print "total page hits:", hits
print "total unique visitors:", len(ips)

    
