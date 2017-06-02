def ips(start, end):
    import socket, struct
    start = struct.unpack('>I', socket.inet_aton(start))[0]
    end = struct.unpack('>I', socket.inet_aton(end))[0]
    return (socket.inet_ntoa(struct.pack('>I', i)) for i in xrange(start, end))

def urls_fromFile(fileName):
    with open(fileName) as f:
	while True:
            url = f.readline()
	    if url == '':
                break
            yield url[:-1]

