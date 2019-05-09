import urllib.request
import csv
with open('Input.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=' ')
    data = []
    url = []
    encoding="utf-8"
    passcount=0
    failcount=0
#To clear a file content
    result=open('API_Test_Results.txt', 'w').close()
    for row in readCSV:
        data = row[0]
        url = row[1]
        binary_data = data.encode(encoding)
        req = urllib.request.Request(url, binary_data, {'Content-Type': 'content/json'})
        try:
          f = urllib.request.urlopen(req)
        except:
          failcount += 1
        for x in f:
            mystring = x.decode(encoding)
#To write to a file in append mode
            result=open("API_Test_Results.txt","a+")
            result.write(data+'\n')
            result.write(url+'\n')
            result.write(mystring+'\n')
            if (mystring.find("\"success\":true")!=-1):
                result.write("API Test - PASS")
                passcount += 1
            else:
                result.write("API Test - FAIL")
                failcount += 1
        result.write("\n\n")
    f.close()

result = open("API_Test_Results.txt", "r")
fline="The pass count is "+str(passcount)+"\n\nThe fail count is "+str(failcount)+"\n\n"
oline=result.readlines()
oline.insert(0,fline)
result.close()
 
result=open("API_Test_Results.txt","w")
result.writelines(oline)
result.close()

