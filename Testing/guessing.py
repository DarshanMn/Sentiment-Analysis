import sys
import MySQLdb
import re

class insertReview:
	
	review = ""
	count = 0
	set = 0

	def __init__(self):

		self.mydb = MySQLdb.connect(host='localhost',
		 	user='root',
		 	passwd='neo&trinity',
		 	db='training_data')
		self.mydb1 = MySQLdb.connect(host='localhost',
		 	user='root',
		 	passwd='neo&trinity',
		 	db='phone_reviews')
		self.cursor = self.mydb.cursor()
		self.cursor1 = self.mydb1.cursor()
		self.frequency=0
		self.getData()
		self.calAccuracy()

	def getReview(self):

		self.phone=raw_input("Enter phone\n");
		self.cursor1.execute("select review from raw_reviews where phone_id='"+self.phone+"';")
		result = self.cursor1.fetchall()

		for data in result:
			self.review = data
			self.review = self.review[0].replace(".","")

			self.review = self.review.lower() 
			self.review = re.sub('[.,;/<>+:_=!\\\'\"?~$^*|`]', "", self.review)
			self.review = re.sub('[0-9]', "", self.review)
		 	self.review = self.review.replace(")","")
		 	self.review = self.review.replace("(","")
		 	self.review = self.review.replace("]","")
		 	self.review = self.review.replace("[","")
		 	self.review = self.review.replace("-","")
			print self.review

			self.pxcPos = 1.0
			self.pxcNeg = 1.0

			words = self.review.strip().split(" ") # prints each row

			for word in words:
				if self.set:
					word = "!" + word
					print word
					self.set=0
				if word=="not":
					self.set=1
				
				if self.pxcPos * (float(self.getFeatures(word,"positive")+1)/float(self.totalWords)) == 0.0:
					break
				else:
					self.pxcPos = self.pxcPos * (float(self.getFeatures(word,"positive")+1)/float(self.totalWords))
					self.pxcNeg = self.pxcNeg * (float(self.getFeatures(word,"negative")+1)/float(self.totalWords))

			self.pcdPos = float(self.pc) * float(self.pxcPos);
			self.pcdNeg = float(self.pc) * float(self.pxcNeg);

			if self.pcdPos >= self.pcdNeg:
				self.posPer=self.pcdPos/float(self.pcdPos + self.pcdNeg) * 100
				print "positive"
				print self.posPer
				print ""
			else:
				self.negPer=self.pcdNeg/float(self.pcdPos + self.pcdNeg) * 100
				print "negative"
				print self.negPer
		return
			
	def getData(self):

		self.cursor.execute("select SUM(total) from doc_frequency")
		result = self.cursor.fetchone()
		for data in result:
			self.docCount = int(data) + 1

		self.cursor.execute("select total from doc_frequency where words='positive';")
		result = self.cursor.fetchone()
		for data in result:
			self.posCount = int(data) + 1

		self.cursor.execute("select total from doc_frequency where words='negative';")
		result = self.cursor.fetchone()
		for data in result:
			self.negCount = int(data) + 1

		self.cursor.execute("select SUM(frequency) from positive_words");
		result = self.cursor.fetchone()
		for data in result:
			self.totalPosWords = int(data) + 1

		self.cursor.execute("select SUM(frequency) from negative_words");
		result = self.cursor.fetchone()
		for data in result:
			self.totalNegWords = int(data) + 1

		self.totalWords = self.totalPosWords + self.totalNegWords
		
		self.pc = float(self.posCount) / self.docCount


	def getFeatures(self,word,var):

		try:
			self.cursor.execute("select frequency from "+var+"_words where words='"+ word+"';")
			result = self.cursor.fetchone()
			for data in result:
				return int(data) + 1
		except Exception as err:
			return 1
			
	def calAccuracy(self):

		self.getReview()

def main():
	obj = insertReview()
		
if __name__ == "__main__":
    main()
