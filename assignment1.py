# Implement a cache that on start-up would load data from a file into the cache. The cache would have an initial size of 20 elements and upon reaching its limit, to add any new element it would remove the least recently accessed element. On shutdown it should store the cached data back to the file. The data should be stored in the cache according to a caching strategy. Provide options for cache CRUD.

# Testing Dataset : records of students. You need to create the test dataset. The student record would have data such as - their ID's, classes enrolled and marks obtained in them. The records should be cached in a sorted manner according to the student marks.

# Document your choice of data structure and implementation strategy. Also the necessary steps to get it running with the test data set. 


import os
ch=0
while ch<3:
	print("\n1) ADD \n2) VIEW \n3) EXIT")
	ch=int(raw_input("Select your choice: "))
	new=[]
	data=[]
	if ch == 1:
		try:
			i=0
			file=open("stud.txt","ab+")
			rec = "1"
			while rec!="":
				rec = file.readline()
				i=i+1
			file.close()
			if i<20:
				no=raw_input("Enter Student Roll no:")
				name=raw_input("Enter Student Name:")
				mark=raw_input("Enter Student Marks:")
				new.insert(0,no)
				new.insert(1,name)
				new.insert(2,mark)
				file=open("stud.txt","ab+")
				file.write(str(new)+"\n")
				file.close()
				print("Record saved...")
			else:
				# print("20 recored already saved")
				file=open("stud.txt","r")
				rec = ""
				cnt=0
				temp=[]
				while cnt<=18 :
					rec = file.readline()
					if rec !="\n":
						temp.insert(cnt,rec)
					cnt=cnt+1
				file.close()
				os.remove("stud.txt")
				file=open("stud.txt","ab+")
				no=raw_input("Enter Student Roll no:")
				name=raw_input("Enter Student Name:")
				mark=raw_input("Enter Student Marks:")
				new.insert(0,no)
				new.insert(1,name)
				new.insert(2,mark)
				file.write(str(new)+"\n")
				for x in temp:
					file.write(str(x))
				file.close()
		except Exception as e:
			print("\n\n     Error ---->"+str(e))

	if ch== 2:
		file=open("stud.txt","r")
		rec = "1"
		i=-1
		while rec!="":
			rec = file.readline()
			i=i+1
			print (rec)
		print (i)