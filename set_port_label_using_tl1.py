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
            soc.send('ACT-USER::admin:99999::root;')
            print soc.recv(1024)

            while 1:

                for prt in range(1, 97):
                    print "set port label for port %d" % prt
                    prt_label = 'port'+str(prt)
                    soc.send('ED-PORT-LABEL::%d:123:::LABEL=%s;' % (prt, prt_label))
                    print soc.recv(1024)
                    time.sleep(5)
        except Exception as err:
            print err
            soc.close()
            time.sleep(30)
            pass

socConn()

