from thread import start_new_thread
import sys, os, string, thread
import paramiko
import time

def connect_tl1_over_ssh(h):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    query_header_info = "RTRV-HDR:::123:;"
    try:
        ssh.connect(h, username='admin', password='root', port=6252, key_filename='/home/craja/.ssh/id_rsa')
        stdin, stdout, stderr = ssh.exec_command(query_header_info)
    except Exception as err:
        print "err : %s" % err
    print stdout.readlines()
    print stdin.readlines()
    print stderr.readlines()



start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
#start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
#start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
#start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
#start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
#start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
#start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
#start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
#start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
#start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
#start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
#start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
#start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
#start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
#start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
#start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
#start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
#start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
#start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
#start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))
#start_new_thread(connect_tl1_over_ssh,('10.99.99.225',))


c = raw_input("Type something to quit.")
