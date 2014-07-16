import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='neo&trinity',
    db='training_data')
cursor = mydb.cursor()

cursor.execute('select review from positive_reviews;')
rows = cursor.fetchall()
fp = open('positive.csv', 'w')
file = csv.writer(fp)
file.writerows(rows)
fp.close()#close the connection to the database.

cursor.execute('select review from negative_reviews;')
rows = cursor.fetchall()
fp = open('negative.csv', 'w')
file = csv.writer(fp)
file.writerows(rows)
fp.close()#close the connection to the database.

cursor.execute('select review from neutral_reviews;')
rows = cursor.fetchall()
fp = open('neutral.csv', 'w')
file = csv.writer(fp)
file.writerows(rows)
fp.close()#close the connection to the database.

cursor.close()
print ("Done")
