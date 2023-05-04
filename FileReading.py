import numpy as np
import pandas as pd
import os
#Developed By Matthew Davidson
#This class reads the RUN file and creates a dataframe that consist of all the students.


#THIS IS A PYTHON OBJECT CLASS: The comments within the openFile function explains how the selected RUN file returns
                                #a DataFrame about all the information for each student.




#Here is how the object functions:
#First, create the class. Similar to Java, the class holds everything relavent to the object
class FileReading:
  #This is the constructor. A FileReading Object requires only 1 input (self is similar to how 'this' functioins in Java)
  #input: runFile, runFile is the name of the RUN file you're looking to run.
  def __init__(self,runFile):
    #self.runFile is basically saying this.runFile in Java.
    self.runFile = runFile
    self.directory = os.path.dirname(self.runFile)
    #this is the dataFrame that will be returned in the openFile function
    #Its an empty dataframe that has 6 columns. 
    self.sectionData = pd.DataFrame(columns=["Group","Section","First Name","Last Name","Student ID", "Grade"])

  
  #openFile function uses the runFile provided in the constuctor.
  #RETURNS A DATAFRAME OR A TUPLE
  #The DataFrame is what you're looking for. This contains the data of all the students
  #If a file was not found, then it will return a tuple consisting of the error and the File Name that wasn't found.
  def openFile(self):
    try:
      with open(self.runFile, 'r') as main:

        # Create an empty array to store the lines
        runFileArray = []

        # Read each line in the file and append it to the array
        for line in main:
          runFileArray.append(line.strip())
    except FileNotFoundError as e:
      return e, self.runFile
    # Print the contents of the array
    #print(runFileArray)

    #a 2d array where every row index represents a new group and every colum index represents an SEC file.
    #The first index of every row is the group associated with the sec files.
    group2dArray = []
    
    for i in range(len(runFileArray)):
      
      #Must be when i is greater the 0, because the first index of the runFileArray is the name of the runfile.
      if i > 0:
        self.directory = os.path.dirname(self.runFile)
        self.directory = self.directory +"/"+ runFileArray[i]
        #debugging lines. Prints the current group being added to the group2dArray
        #grp = "Opening {group} file".format(group = runFileArray[i])
        #print(grp)

        #opens the current group file
        try:
          with open(self.directory, 'r') as group:
            secFiles = []
            #For everyline in the groupfile we list the sec files that need to be opened and appened them to secFiles
            for line in group:
              secFiles.append(line.strip())

            group2dArray.append(secFiles)
        except FileNotFoundError as e:
          return e,self.directory
    #prints the list of all sec files for each group. Look at the initialization of group2dArray to better understand it's content.
    #print(group2dArray)


    #Dataframe represents all of the information of every student included in the RUN file. This will be the dataframe used throughout the project for data analysis.
    #The dataframe is structured with 6 columns. Listed below.

    #Loop through each ROW in the group2dArray. Remember, each row represents a list of SEC files and the first index of each row is the name of the group.
    for i in range(len(group2dArray)):
      #print("Prininting Current Class, {section}".format(section = group2dArray[i][0]))
      #Loop through each COLUMN for each ROW in group2dArray. Except when J = 0 (because that would be the group name). This gets the file name for each SEC file included in RUN
      for j in range(len(group2dArray[i])):
        if j > 0:
          self.directory = os.path.dirname(self.runFile)
          self.directory = self.directory +"/"+ group2dArray[i][j]
          #print(group2dArray)
          #print(self.directory)
          #open the SEC file. Read only. Name that opened file 'section'
          try:
            with open(self.directory, 'r') as section:
              #section includeds four values when seperated by the delimiter ",". This would be the first name, last name, student id, and grade of each student in the class.
              #classData is a 2d array where each row represents a student and each column for each row is data about the student.
              classData = np.genfromtxt(section,skip_header=1,delimiter=",", dtype = str)

              #Debuging. See how ClassData is formated
              #print(classData)
              
              #for each row in classData, we add the data of each student to a tempFrame
              for y in range(len(classData)):
                  #Time to tie everything together
                  #We list the group for each student using group2dArray
                  #we do the same thing for section
                  #Using classdata, we list the remaining data for the students.
                  tempFrame = pd.DataFrame({"Group":group2dArray[i][0],"Section":group2dArray[i][j],"First Name":classData[y][0].replace("\"",""),"Last Name":classData[y][1].replace("\"",""),"Student ID":classData[y][2].replace("\"",""),"Grade":classData[y][3].replace("\"","")},index=range(1))
                  #Once the tempFrame is done. Add it to the sectionData DataFrame.
                  
                  self.sectionData = pd.concat([self.sectionData, tempFrame], ignore_index=True)
          except FileNotFoundError as e:
            return e,self.directory
    #print(self.sectionData)
    return self.sectionData