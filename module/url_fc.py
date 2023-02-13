import pymysql 


url_base = "https://www.acmicpc.net/problem/"
ps_number = [str(i) for i in range(1001,20000)]


for num in ps_number:
    url = url_base + num


