import pandas as pd
import numpy as np
import FileReading
import DataProcessing as dp
#This is an example of how to use the FileReading object.

#Set the fileName. This is the parameter for creating a FileReading Object
fileName = "TESTRUN.RUN"

#This creates a FileReadingObj, you call the FileReading class, then the constructor (also called FileReading. Sorry if that's confusing). Then provide the object input, The RUN files name
FileReadingObj = FileReading.FileReading(fileName)

#use the openFile included in the FileReadingObj. 
#This could return one of two things. A pandas DataFrame or a Tuple (basicall a list)
#if it's a DataFrame. Great, everything went right and you now have the data you're looking for.
#If it's a tuple. There's a file missing. Luckily the tuple tells you exactly which file is missing.
DataFrame = FileReadingObj.openFile()


#if it's a tuple
if isinstance(DataFrame,tuple):
    print("Error: ", "No such File Found")
    print("Missing File: ", DataFrame[1])
#if it's not a tuple. It's a DataFrame
else:
    #print(DataFrame.to_string())
    DataFrame = dp.letterTogpa(DataFrame)
    gradepoint_mean_by_class = DataFrame.groupby("Section")["gradepoint"].mean()
    gradepoint_mean_by_group = DataFrame.groupby("Group")["gradepoint"].mean()
    grade_counts_by_class = DataFrame.groupby("Section")["Grade"].value_counts()
    grade_counts_by_group = DataFrame.groupby("Group")["Grade"].value_counts()

    print(DataFrame.to_string())
    print(gradepoint_mean_by_class)
    print(gradepoint_mean_by_group)
    print(grade_counts_by_class)
    print(grade_counts_by_group)

    #for index, row in grade_counts_by_class.iterrows():
        #print(row)
    

        
    