import ips
url_g = ips.urls_fromFile('8080.txt')
count = 0
for i in url_g:
	print i
	print count
	count += 1
