import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='neo&trinity',
    db='training_data')
cursor = mydb.cursor()

pos = "/home/darshan-ubuntu/Sentiment Analysis/Training Data/positive.txt"
neg = "/home/darshan-ubuntu/Sentiment Analysis/Training Data/negative.txt"
neu = "/home/darshan-ubuntu/Sentiment Analysis/Training Data/neutral.txt"

with open(pos,"rb") as f:
	for line in f.readlines():
		try:
			cursor.execute('INSERT INTO positive_reviews(review) VALUES(%s)', (line))
		except Exception as err:
			print err
	
	mydb.commit()

with open(neg,"rb") as f:
	for line in f.readlines():
		try:
			cursor.execute('INSERT INTO negative_reviews(review) VALUES(%s)', (line))
		except Exception as err:
			print err
	
	mydb.commit()

with open(neu,"rb") as f:
	for line in f.readlines():
		try:
			cursor.execute('INSERT INTO neutral_reviews(review) VALUES(%s)', (line))
		except Exception as err:
			print err
	
	mydb.commit()

