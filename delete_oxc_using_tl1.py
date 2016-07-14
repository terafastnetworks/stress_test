import socket
import time

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "10.99.99.225"
port = 3082
#var = 1


def socConn():

    while 1:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.connect((host, port))
        try:
            #soc.connect((host, port))
            soc.send('ACT-USER::admin:99999::root;')
            print soc.recv(1024)

            while 1:

                for ingress_port in range(1, 49):
                    soc.send('DLT-PATCH:PolatisOXC:%d:123:;' % ingress_port)
                    print "delete oxc in port %d" % ingress_port
                    print soc.recv(1024)
                    time.sleep(5)
                #for fort in range(1, 25):
                #    soc.send('RLS-PORT-SHUTTER::%d:123:;' % fort)
                #    print "Ports Enabled"
                #    print soc.recv(1024)
                #    time.sleep(10)
        except Exception as err:
            print err
            soc.close()
            time.sleep(30)
            pass

socConn()

