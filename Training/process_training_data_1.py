sourcefile = "Cell_Phones_&_Accessories.txt"
filename2 = "training_data.txt"

offending = ["review/text","review/score"]

def fixup( filename ): 
    fin = open( filename ) 
    fout = open( filename2 , "w")
    for line in fin: 
        if True in [item in line for item in offending]:
        	fout.write(line)
    fin.close() 
    fout.close() 

fixup(sourcefile)
