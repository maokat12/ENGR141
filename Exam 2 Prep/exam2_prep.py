i = open(input("Data file name: "), 'r')
o = open(input("Results file name: "), 'w')
lines = i.readlines()
i.close()

original = []
final = []
for x in lines:
	y = x.split()
	original.append(y[0])
	final.append(y[1])
	
error_line = []
for a in range(0, len(original)-1):
	i = original[a]
	j = final[a]
	for b in range(0, len(i)-1):
		if i[b] != j[b]:
			error_line.append(a+1)
			break
				
error_rate = len(error_line)/len(original)
					
o.write("Error rate: " + str(error_rate) + "\n")
for line in error_line:
	o.write(str(line))
o.close()

			
