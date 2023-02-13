from config.db import conn

url_base = "https://www.acmicpc.net/problem/"
ps_number = [str(i) for i in range(1001,20000)]

url = ''
for num in ps_number:
    url = url_base + num


mydb = conn.cursor()
querystring = 'insert into url_table (problem_url) values ({});'.format(url)
mydb.execute(querystring)
conn.commit()
mydb.close()

