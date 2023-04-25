import pandas as pd
import numpy as np
import FileReading as fr


def letterTogpa(DataFrame):
    grade = {'A':4.00,'A-':3.67,'B+':3.33,'B':3.00,'B-':2.67,'C+':2.33,'C':2.00,'C-':2.00,'D+':1.33,'D':1.00,'D-':0.67,'F':0.00}
    DataFrame["gradepoint"] = DataFrame["Grade"].apply(lambda x: grade[x] if x in grade else None )
    return DataFrame

def listedComboBox(DataFrame):
    grpArray = np.array(DataFrame["Group"].unique())
    secArray = np.array(DataFrame["Section"].unique())
    result = np.concatenate((grpArray,secArray))
    return " ".join(result)

def leftSelect(DataFrame, item_selected):

    mask = DataFrame.applymap(lambda x: x == item_selected)
    rows_with_specific = DataFrame[mask.any(axis = 1)]
    return rows_with_specific

def gradeColor(grade):
   color = {'A':"#2E7F18",'A-':"#2E7F18",'B+':"#45731E",'B':"#45731E",'B-':"#675E24",'C+':"#8D472B",'C':"#8D472B",'C-':"#8D472B",'D+':"#B13433",'D':"#B13433",'D-':"#B13433",'F':"#C82538", 'P':"#a5a8a6",'NP':"#a5a8a6",'I':"#a5a8a6","W":"#a5a8a6","D":"#a5a8a6"}
   return color.get(grade,None)