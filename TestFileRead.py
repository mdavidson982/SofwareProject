import pandas as pd
import numpy as np
import FileReading
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
    print(DataFrame.to_string())