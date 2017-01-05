import socks

def run(**args):
    s = socks.socksocket()
    s.set_proxy(socks.HTTP,args[0],args[1])
