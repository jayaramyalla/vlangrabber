import commands
command="ping %s -c 1"
ip="172.20.%s.1"
w=open("output.txt","a")
for i in range(255):
    try:
		uip= ip % str(i)
        d = command % uip
        pp=commands.getoutput(d)
        if "received, 0% packet loss," in pp:
			uip=uip+"\n"
            w.writelines(uip)
        else:
            pass
    except Exception:
        pass

w.close()

#JayaramYalla
#https://twitter.com/jayaramyalla
#https://in.linkedin.com/in/jayaramyalla
