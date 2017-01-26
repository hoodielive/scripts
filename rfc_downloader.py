import sys, urllib.request 

try:
	rfc_number = int(sys.argv[1])
except (IndexError, ValueError):
	print('Must supply an RFC number as first argument')
	sys.exit(2)
template = 'http://ietf.org/rfc/rfc{}.txt'
url = template.format(rfc_number)
rfc_raw = urllib.request.urlopen(url).read()
rfc = rfc_raw.decode()
print(rfc)