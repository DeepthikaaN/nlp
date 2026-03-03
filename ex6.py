def subnet(ip_addr):
    ip_str = ip_addr.split('.')[0]
    ip_num = int(ip_str)
    if 1 <= ip_num <= 126:
        return "Subnet mask : 255.0.0.0 - Class A"
    elif 128 <= ip_num <= 191:
        return "Subnet mask : 255.255.0.0 - Class B"
    elif 192 <= ip_num <= 223:
        return "Subnet mask : 255.255.255.0 - Class C"
    else:
        return "Invalid or unsupported IP class"
data = input("Enter the IP Address: ")
result = subnet(data)
print(result)  

