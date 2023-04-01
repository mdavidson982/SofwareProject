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
for i in range(len(group2dArray)):
  print("Prininting Current Class, {section}".format(section = group2dArray[i][0]))
  section2dArray.append(group2dArray[i][0])
  for j in range(len(group2dArray[i])):
    if j > 0:
      with open(runFileArray[i][j], 'r') as section:
        #This Opens the Sections Files. This is about as far as I got before I had to leave
        
    
      

  


