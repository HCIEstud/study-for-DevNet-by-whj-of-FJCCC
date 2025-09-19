def confSWlo0_IP_for_huawei(hostname,user,password,ip):

    import telnetlib
    import time

    # host = '172.18.0.100'
    # user = "python"
    # password = "huawei@123"

    tn = telnetlib.Telnet(hostname) #连接交换机

    tn.read_until(b'Username:')  #读取终端回显如果是‘Username’执行下一步
    tn.write(user.encode('ascii')+ b"\n") ## 编码：将字符串转换为字节以便通过网络发送

    tn.read_until(b'Password:')
    tn.write(password.encode('ascii') + b"\n")
    tn.write(b"sys\n")
    tn.write(b"int lo 0\n")
    command = f'ip add {ip} 24\n'
    tn.write(command.encode('ascii'))

    tn.write(b'dis ip int b\n')

    time.sleep(1)
    tn.write(b'quit\n')
    print(tn.read_very_eager().decode('ascii'))  #解码：将从网络接收的字节转换为字符串以便显示

    tn.close()

confSWlo0_IP_for_huawei('172.18.0.100','python','huawei@123','100.100.100.100')