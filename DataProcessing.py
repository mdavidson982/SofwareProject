import pandas as pd
import numpy as np


def letterTogpa(DataFrame):
    grade = {'A':4.00,'A-':3.67,'B+':3.33,'B':3.00,'B-':2.67,'C+':2.33,'C':2.00,'C-':2.00,'D+':1.33,'D':1.00,'D-':0.67,'F':0.00}
    DataFrame["gradepoint"] = DataFrame["Grade"].apply(lambda x: grade[x] if x in grade else None )
    return DataFrame