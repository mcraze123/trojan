import socks

def run(**args):
    s = socks.socksocket()
    s.set_proxy(socks.SOCKS5,args[0],args[1])
