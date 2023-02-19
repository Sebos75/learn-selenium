import csv

with open('dane.csv', newline='') as f:
    reader = csv.reader(f,delimiter=';')
    for row in reader:
        # print(' '.join(row))
        name = row[0].strip()
        time = row[1][0:20].strip()
        score = row[2][0:6]
        sql = "insert into webapp (event_time, app_name, score, test) \
            values ('"+str(time)+"', '"+name+"', "+score+", 1); \n "

        outpupFile = 'data.sql'
        f = open(outpupFile, 'a')
        f.write(sql)
        f.close()

