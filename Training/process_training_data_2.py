filename = "Training_Data.txt"

fpositive = open("positive.txt","w")
fnegative = open("negative.txt","w")
fneutral = open("neutral.txt","w")

def fixup(): 
    i=1
    rating=-2
    
    with open(filename,'rb') as f:
		while True:
		    line=f.readline()
		    if not line: break
		    if (line.strip()=="2.0"):
		    	line = f.readline()
		    	fnegative.write(line)
		    if (line.strip()=="1.0"):
		    	line = f.readline()
		    	fnegative.write(line)
		    if (line.strip()=="3.0"):
		    	line = f.readline()
		    	fneutral.write(line)
		    if (line.strip()=="4.0"):
		    	line = f.readline()
		    	fpositive.write(line)
		    if (line.strip()=="5.0"):
		    	line = f.readline()
		    	fpositive.write(line)

    fpositive.close()
    fnegative.close()
    fneutral.close()

fixup()

