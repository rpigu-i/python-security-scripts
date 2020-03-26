import threading
import paramiko
import subprocess

def ssh_command(ip, user, passwd, command, keys, port):

    client = paramiko.SSHClient()

    if keys:
        client.load_host_keys(keys)
    
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port, username=user, password=passwd)
    ssh_session = client.get_transport().open_session()

    if ssh_session.active:
        ssh_session.exec_command(command)
        print(ssh_session.recv(1024))
    return


ssh_command('localhost', 'admin', 'admin', 'id', False, '5000')

     
