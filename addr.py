import geoip2.database
reader = geoip2.database.Reader('./GeoLite2-City.mmdb')
ip = input("输入你要查询的IP:\n")
response = reader.city(ip)
# 有多种语言，我们这里主要输出英文和中文
print("你查询的IP的地理位置是:")

print("国家：{}({}) ，简称:{}".format(response.country.name,
                                response.country.names["zh-CN"],
                                response.country.iso_code))

