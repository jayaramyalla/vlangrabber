import commands
p="ping 172.20.%s.1 -c 1"
w=open("output.txt","a")
for i in range(255):
    try:
        d = p % str(i)
        print d
        pp=commands.getoutput(d)
        print pp
        if "received, 0% packet loss," in pp:
            pp=pp+"\n"
            w.writelines(d)
        else:
            pass
    except Exception:
        pass

w.close()
