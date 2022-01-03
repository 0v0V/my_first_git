import csv

fileMatrix = []

with open('Step_13_SampleFile_score.csv', 'r') as fileRead:
    myReader = csv.reader(fileRead)
    for lineContent in myReader: 
        fileMatrix.append(lineContent) 

print("[Before]")
print(fileMatrix)          
        
fileMatrix[0].extend(["HTML5", "CSS3"])
  
lenFileMatrix = len(fileMatrix)
   
for i in range(lenFileMatrix - 1):
    i = i + 1
    fileMatrix[i].extend(["_", "_"])
    
print("[After]")
print(fileMatrix) 

with open('Step_13_SampleFile_newScore.csv', 'w') as fileWrite:
    myWriter = csv.writer(fileWrite)
    for i in range(lenFileMatrix): 
        myWriter.writerow(fileMatrix[i]) 