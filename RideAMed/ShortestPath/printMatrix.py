from ExtractData import ExtractData
extractData = ExtractData("E:\\anul III\\AI\\date_proiect\\easy\PTP-RAND-1_4_2_16.json")
matrix=extractData.getDistanceMatrix()
a_file = open("test.txt", "a+")
a_file.write(" ")
for i in range(0 ,len(matrix)):
    a_file.write(str(i))
    a_file.write(" ")
a_file.write("\n")
for j in range(0,len(matrix[0])):
    a_file.write(str(j))
    a_file.write(" ")
    a_file.write(str(matrix[j]))
    a_file.write("\n")
a_file.close()
