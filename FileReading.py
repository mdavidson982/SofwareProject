import numpy as np
import pandas as pd

with open('TESTRUN.run', 'r') as main:

  # Create an empty array to store the lines
  runFileArray = []

  # Read each line in the file and append it to the array
  for line in main:
    runFileArray.append(line.strip())

# Print the contents of the array
print(runFileArray)


group2dArray = []
for i in range(len(runFileArray)):
 
  if i > 0:
   grp = "Opening {group} file".format(group = runFileArray[i])
   print(grp)
   with open(runFileArray[i], 'r') as group:
     secFiles = []
     for line in group:
      secFiles.append(line.strip())

     group2dArray.append(secFiles)

print(group2dArray)

section2dArray = []


sectionData = pd.DataFrame(columns=["Group","Section","First Name","Last Name","Student ID", "Grade"])
for i in range(len(group2dArray)):
  print("Prininting Current Class, {section}".format(section = group2dArray[i][0]))
  section2dArray.append(group2dArray[i][0])
  for j in range(len(group2dArray[i])):
    if j > 0:
      with open(group2dArray[i][j], 'r') as section:
        classData = np.genfromtxt(section,skip_header=1,delimiter=",",deletechars="~!@#$%^&*()-=+~\|]}[{'; /?.><", dtype = str)
        print(classData)
        for y in range(len(classData)):
            sectionData = sectionData.append({"Group":group2dArray[i][0],"Section":group2dArray[i][j],"First Name":classData[y][0],"Last Name":classData[y][1],"Student ID":classData[y][2],"Grade":classData[y][3]},ignore_index=True)

print(sectionData.to_string())

 
      

  


