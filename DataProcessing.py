import pandas as pd
import numpy as np
import FileReading as fr
import matplotlib.pyplot as plt
import os, io
from PIL import Image as IG
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.utils import ImageReader

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
    rows_with_specific_sorted = rows_with_specific.sort_values('gradepoint').reset_index(drop = True)
    #print(rows_with_specific_sorted)
    return rows_with_specific_sorted

def gradeColor(grade):
   color = {'A':"#2E7F18",'A-':"#2E7F18",'B+':"#45731E",'B':"#45731E",'B-':"#675E24",'C+':"#8D472B",'C':"#8D472B",'C-':"#8D472B",'D+':"#B13433",'D':"#B13433",'D-':"#B13433",'F':"#C82538", 'P':"#a5a8a6",'NP':"#a5a8a6",'I':"#a5a8a6","W":"#a5a8a6"}
   return color.get(grade,None)

def averageLetter(DataFrame):
    grade_ranges = [("A",(3.68),(4.00)),("A-",(3.34),(3.67)),("B+",(3.01),(3.33)),("B",(2.68),(3.00)),("B-",(2.34),(2.67)),("C+",(2.01),(2.33)), ("C",(1.34),(2.00)),("D+",(1.01),(1.33)),("D",(0.01),(1.00)), ("F",(0.00),(0.00))]
    average_gpa = DataFrame["gradepoint"].mean()
    #print(average_gpa)
    for letter_grade, min_grade, max_grade in grade_ranges:
        if min_grade <= average_gpa <= max_grade:
            return letter_grade
        
def averageGPA(DataFrame):
    averageGPA = DataFrame["gradepoint"].mean()
    averageGPA = round(averageGPA,2)
    return averageGPA

def standardDeviation(DataFrame):
    std = DataFrame["gradepoint"].std()
    std = round(std, 4)
    return std

def mad(series):
    median = series.median()
    absolute_deviations = (series - median).abs()
    absolute_deviations = round(absolute_deviations, 4)
    return absolute_deviations.median()

def zscore(DataFrame):
    mean = DataFrame["gradepoint"].mean()
    std = DataFrame["gradepoint"].std()
    DataFrame["Zscore"] = (DataFrame["gradepoint"] - mean)/std
    DataFrame["Zscore"] = DataFrame["Zscore"].round(4)
    return DataFrame

def distributionGraph(DataFrame):
    grade_counts = DataFrame["Grade"].value_counts().sort_index()
    plt.clf()
    plt.rcParams["figure.figsize"] = [8.50, 5.50]
    plt.rcParams["figure.autolayout"] = True
    plt.bar(grade_counts.index, grade_counts.values)
    plt.xlabel('Letter Grades')
    plt.ylabel('Frequency')
    plt.title('Histogram of Letter Grades')
    plt.xticks(range(len(grade_counts.index)), grade_counts.index)
    #plt.show()
    img_buf = io.BytesIO()
    plt.savefig(img_buf, format = "jpg")
    img_buf.seek(0)
    reportlab_image = ImageReader(img_buf)
    image = Image(img_buf, width = 450, height = 350)
    return image

    


def makePDF(DataFrame, selection, file_path):

    
    pdf_file = selection.split(".")[0] + ".pdf"
    output_file_path = os.path.join(file_path, pdf_file)
    doc = SimpleDocTemplate(output_file_path, pagesize = letter)
    styles = getSampleStyleSheet()
    style = styles["Normal"]
    flowables = []
    table = PDFTable(DataFrame)
    flowables.append(table)
    histogram = distributionGraph(DataFrame)
    flowables.append(histogram)


    doc.build(flowables)



def PDFTable(DataFrame):
    selected_columns = ["First Name", "Last Name", "Student ID", "Grade", "Zscore"]
    pdf_frame = DataFrame[selected_columns]
    table_data = [list(pdf_frame.columns)] + pdf_frame.values.tolist()
    table = Table(table_data)
    table_style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 14),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])

    table.setStyle(table_style)
    return table


def sectionZScore(WholeFrame, SelectedFrame):
    Specific_Group = SelectedFrame["Group"].unique()
    GroupedFrame = WholeFrame.loc[WholeFrame["Group"] == Specific_Group[0]]

    Specific_Sections = GroupedFrame["Section"].unique()
    mean = GroupedFrame["gradepoint"].mean()
    std = GroupedFrame["gradepoint"].std()

    zScores = []
    for section in Specific_Sections:
        students = WholeFrame.loc[WholeFrame["Section"] == section]
        section_z_score = ((students["gradepoint"].mean() - mean) / std).round(4)
        zScores.append([section, section_z_score])

    zScores = np.array(zScores)
    return zScores 

def zScoreColor(z_score):
    z_color_range = [("#2E7F18",(0),(.5)),("#2E7F18",(-.5),(0)),("#8D472B",(.51),(1)),("#8D472B",(-1),(-.51)),("#B13433",(1.1),(1.9)),("#B13433",(-1.9),(-1.01)), ("#C82538",(2.00),(4.00)),("#C82538",(-4.0),(-2.0))]
    for color, min_score, max_score in z_color_range:
        if min_score <= z_score.astype(float) <= max_score:
            return color
    
    