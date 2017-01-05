import socks

def run(**args):
    for host, port in args:
        if args[host] == None or args[port] == None:
            host="localhost"
            port="8080"
        else:
            host=args[host]
            port=args[port]

        s = socks.socksocket()
        s.set_proxy(socks.HTTP,host,port)

# run like this:
#run(**{'host': "localhost", 'port': "31337"})
