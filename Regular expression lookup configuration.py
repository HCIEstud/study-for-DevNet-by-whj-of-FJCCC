import  re
test = 'Test match() function of regular expression'
devnet = 'https://support.huawei.com/enterprise/zh/doc/index.html'
a = re.search(r'function',test)
print(a)
print(a.group())
b = re.search(r'support',devnet)
print(b)
print(b.group())
f = open(r'V:\01_尚硅谷大模型技术之Python基础\1.笔记\尚硅谷大模型技术之Python1.0.docx', 'r')
print(f)

show_ip = '''[Huawei]dis ip int b 
*down: administratively down
^down: standby
(l): loopback
(s): spoofing
The number of interface that is UP in Physical is 1
The number of interface that is DOWN in Physical is 3
The number of interface that is UP in Protocol is 1
The number of interface that is DOWN in Protocol is 3

Interface                         IP Address/Mask      Physical   Protocol  
GigabitEthernet0/0/0              1.1.1.1/24           down       down      
GigabitEthernet0/0/1              2.2.2.2/24           down       down      
GigabitEthernet0/0/2              3.3.3.3/24           down       down      
NULL0                             unassigned           up         up(s)     
[Huawei]'''
ip_print = re.findall(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b',show_ip)
print(type(ip_print))
print(ip_print)

show_arp = '''<Huawei>dis arp
IP ADDRESS      MAC ADDRESS     EXPIRE(M) TYPE        INTERFACE   VPN-INSTANCE 
                                          VLAN/CEVLAN PVC                      
------------------------------------------------------------------------------
1.1.1.1         00e0-fc2c-6347            I -         GE0/0/0
2.2.2.2         00e0-fc2c-6348            I -         GE0/0/1
3.3.3.3         00e0-fc2c-6349            I -         GE0/0/2
------------------------------------------------------------------------------
Total:3         Dynamic:0       Static:0     Interface:3    
<Huawei>'''

print_arp = re.sub(r'\w{4}\-\w{4}\-\w{4}','1234.4567.abcd',show_arp,1)
print(print_arp)