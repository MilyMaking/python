import geocoder as geo
ip_add = geo.ip('me')
print(ip_add)
inp = input('Search Ip:')
ip = geo.ip(inp)
print(ip.city)
print(ip.lating)
