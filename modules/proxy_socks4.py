import socks

def run(**args):
    s = socks.socksocket()
    s.set_proxy(socks.SOCKS4,args[0],args[1])
