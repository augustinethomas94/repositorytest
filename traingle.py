def loadData():
	source  = []
	source.append(int(input("Enter side 1")))
	source.append(int(input("Enter side 2")))
	source.append(int(input("Enter side 3")))	
	return source


def checkTriangle(a,b,c):	
	d=0
	if (a+b >=c): 
		d=d+1
	if (b+c >=a):
		d=d+1
	if (c+a >=b):
		d=d+1
 		if (d >=2):
			return("traingle can be formed")
		else:
			return("triangle cannot be formed")
		


def main():
	source = loadData()
	checkTriangle(source[0],source[1],source[2])
	

