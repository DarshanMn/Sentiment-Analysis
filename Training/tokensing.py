import csv
import sys
import MySQLdb
import re

class tokeniser:
	i=0
	set=0
	list=dict()

	def __init__(self):
		self.mydb = MySQLdb.connect(host='localhost',
		 	user='root',
		 	passwd='neo&trinity',
		 	db='training_data')
		self.cursor = self.mydb.cursor()
		self.frequency=0

	def tokenise(self):
		f = open('/home/darshan-ubuntu/Project/Sentiment Analysis/Training Data/positive.txt', 'rb') # opens the csv file
		try:
			 for ele in f.readlines():   # iterates the rows of the file in orders
				self.i = self.i+1
				if self.i==20000:
					break
				ele = ele.lower()
				ele = re.sub('[.,;/<>+:_=!\\\'\"?~$^*|`]', "", ele)
				ele = re.sub('[0-9]', "", ele)
			 	ele = ele.replace(")","")
			 	ele = ele.replace("(","")
			 	ele = ele.replace("]","")
			 	ele = ele.replace("[","")
			 	ele = ele.replace("-","")
				words = ele.strip().split(" ") # prints each row
				for word in words:
					self.incrementCount(word)
		finally:
			for ele in self.list.keys():
				self.cursor.execute("INSERT INTO positive_words(words, frequency) VALUES(%s,%s)", (ele, self.list[ele]))
			self.mydb.commit()
			f.close()  	

	def incrementCount(self, word):
		if self.set:
			word="!" + word
			self.set=0
		if word=="not":
			self.set=1
		try:
			self.list[word]+=1
		except Exception as err:
			self.list[word]=1

def main():
	obj = tokeniser()
	obj.tokenise()
		
if __name__ == "__main__":
    main()
