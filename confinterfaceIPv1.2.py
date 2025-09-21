import paramiko
import time

def paramiko_for_sshconfip():

    host = input(str("请输入ssh的ip:"))
    username = input(str("请输入ssh账号:"))
    password = input(str("请输入ssh密码："))
    interface = input(str("请输入需要配置ip的接口，如：g0/0/1："))

    ip = input(str("请输入该接口下要配置的ip mask,必须是三层口："))


    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(hostname=host,username=username,password=password) #进行ssh连接

    print("Successfully connected to",host )

    common = ssh.invoke_shell()
    common.send('sys\n')
    common.send(f'int {interface}\n')
    common.send(f'ip add {ip}\n')
    common.send('dis ip int b\n')
    common.send('quit\n')

    time.sleep(2)

    output = common.recv(65535)
    print(output.decode('ascii'))


    ssh.close()

paramiko_for_sshconfip()