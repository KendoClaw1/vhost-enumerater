#Made By KendoClaw
#Twitter: https://twitter.com/KendoClaw1


from sys import argv
import requests

def main():
	print """
	###############################
	#      vhosts Enumerator      #
	#                             #
	#        By:KendoClaw1        #
	###############################

	"""
	ip = "http://"+argv[1]
	with open('hosts.txt') as h:
		hosts = [line.rstrip('\n') for line in open('hosts.txt')]

	for host in hosts:
		headers = {'Host':host}
		requests.get(ip,headers=headers)
		req = requests.get(ip,headers=headers)
		print "Host: "+host+"\nStatus code: "+str(req.status_code)
try:
	main()
except IndexError:
	print "Usage: "+argv[0]+" IP"

except requests.exceptions.ConnectionError:
	print "Enter IP without http:// or https://"