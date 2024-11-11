##importing libraries
import csv
import re
from datetime import *

##declaring variables
Student_Name = []
Students_Majors_List = []
GPA_List = []
Graduation_Dates_List = []
global major
major = ""
global gpa
gpa = 0

##########################################################
######           get_Students_Majors_List           ######
##########################################################

def get_Students_Majors_List():
    fn = "StudentsMajorsList.csv"
    Input_File=open(fn,'r')
    csvreader=csv.reader(Input_File)
    rows=[]
    for row in csvreader:
        rows.append(row)
        
    global Students_Majors_List
    Students_Majors_List = rows

    Input_File.close()
    #print("*get_Students_Majors_List_DONE*")
    #return

##########################################################
######                 get_GPA_List                 ######
##########################################################

def get_GPA_List():
    fn = "GPAList.csv"
    Input_File=open(fn,'r')
    csvreader=csv.reader(Input_File)
    rows=[]
    for row in csvreader:
        rows.append(row)
        
    global GPA_List
    GPA_List = rows

    Input_File.close()
    #print("*get_GPA_List_DONE*")
    #return

##########################################################
######          get_Graduation_Dates_List           ######
##########################################################

def get_Graduation_Dates_List():
    fn = "GraduationDatesList.csv"
    Input_File=open(fn,'r')
    csvreader=csv.reader(Input_File)
    rows=[]
    for row in csvreader:
        rows.append(row)
        
    global Graduation_Dates_List
    Graduation_Dates_List = rows

    Input_File.close()
    #print("*get_Graduation_Dates_List_DONE*")
    #return



##########################################################
######                save_Full_Roster              ######
##########################################################

def save_Full_Roster():

    s_Students_Majors_List = sorted(Students_Majors_List, key=lambda x: x[1])

    Output_File= open('FullRoster.csv',"w+",newline='')
    csv_Writer = csv.writer(Output_File)
    
    for i in range(len(s_Students_Majors_List)):
        for j in range(len(GPA_List)):
            if GPA_List[j][0] == s_Students_Majors_List[i][0]:
                for k in range(len(Graduation_Dates_List)):
                    if Graduation_Dates_List[k][0] == s_Students_Majors_List[i][0]:
                        Data = [s_Students_Majors_List[i][0], s_Students_Majors_List[i][3], s_Students_Majors_List[i][2], s_Students_Majors_List[i][1], GPA_List[j][1], Graduation_Dates_List[k][1], s_Students_Majors_List[i][4]]  
                        csv_Writer.writerow(Data)
    Output_File.close()
   
    print("*save_Full_Roster_DONE*")

    #return

##########################################################
######             save_List_Per_Major              ######
##########################################################

def save_List_Per_Major():
    
    s_Students_Majors_List = sorted(Students_Majors_List, key=lambda x: x[0])

    major_List = []
    for i in range(len(s_Students_Majors_List)):
        if s_Students_Majors_List[i][3] not in major_List:
            major_List.append(s_Students_Majors_List[i][3])

    for record in major_List:
        s_record = record.replace(" ", "")
        Output_File= open(s_record+'.csv',"w+",newline='')
        csv_Writer = csv.writer(Output_File)
        for i in range(len(s_Students_Majors_List)):
            for j in range(len(Graduation_Dates_List)):
                if Graduation_Dates_List[j][0] == s_Students_Majors_List[i][0]:
                    if record == s_Students_Majors_List[i][3]:
                        Data = [s_Students_Majors_List[i][0], s_Students_Majors_List[i][1], s_Students_Majors_List[i][2], Graduation_Dates_List[j][1], s_Students_Majors_List[i][4]]  
                        csv_Writer.writerow(Data)
        Output_File.close()
   
    print("*save_List_Per_Major_DONE*")

    #return

##########################################################
######        save_Scholarship_Candidates           ######
##########################################################

def save_Scholarship_Candidates():

    s_GPA_List = sorted(GPA_List, key=lambda x: x[1], reverse=True)

    Output_File= open('ScholarshipCandidates.csv',"w+",newline='')
    csv_Writer = csv.writer(Output_File)

    for i in range(len(s_GPA_List)):
        if float(s_GPA_List[i][1]) > (3.8):
            for j in range(len(Students_Majors_List)):
                if s_GPA_List[i][0] == Students_Majors_List[j][0]:
                    if Students_Majors_List[j][4] != 'Y':
                        for k in range(len(Graduation_Dates_List)):
                            if  s_GPA_List[i][0] == Graduation_Dates_List[k][0]:
                                d1, m1, y1 = [int(x) for x in Graduation_Dates_List[j][1].split('/')]
                                b1 = date(y1, m1, d1)
                                b2 = date.today()
                                if b1>b2:
                                    Data = [Students_Majors_List[j][0], Students_Majors_List[j][1], Students_Majors_List[j][2], Students_Majors_List[j][3], s_GPA_List[i][1]]  
                                    csv_Writer.writerow(Data)
    Output_File.close()
   
    print("*save_Scholarship_Candidates_DONE*")

    #return


##########################################################
######          save_Disciplined_Students           ######
##########################################################

def save_Disciplined_Students():

    s_Graduation_Dates_List = sorted(Graduation_Dates_List, key = lambda x:datetime.strptime(x[1], '%d/%m/%Y'))

    Output_File= open('DisciplinedStudents.csv',"w+",newline='')
    csv_Writer = csv.writer(Output_File)

    for i in range(len(s_Graduation_Dates_List)):
        for j in range(len(Students_Majors_List)):
            if s_Graduation_Dates_List[i][0] == Students_Majors_List[j][0]:
                Data = [Students_Majors_List[j][0], Students_Majors_List[j][1], Students_Majors_List[j][2],  s_Graduation_Dates_List[i][1]]  
                csv_Writer.writerow(Data)
    Output_File.close()
   
    print("*save_Disciplined_Students_DONE*")

    #return

##########################################################
######                print_Students                ######
##########################################################

def print_Students(r):

    f=0
    for i in range(len(GPA_List)):
        if float(GPA_List[i][1]) >= (gpa-r) and float(GPA_List[i][1]) <= (gpa+r):
            for j in range(len(Students_Majors_List)):
                if GPA_List[i][0] == Students_Majors_List[j][0]:
                    if Students_Majors_List[j][4] != 'Y' and Students_Majors_List[j][3]==major:
                        for k in range(len(Graduation_Dates_List)):
                            if  GPA_List[i][0] == Graduation_Dates_List[k][0]:
                                d1, m1, y1 = [int(x) for x in Graduation_Dates_List[j][1].split('/')]
                                b1 = date(y1, m1, d1)
                                b2 = date.today()
                                if b1<b2:
                                    Data = [Students_Majors_List[j][0], Students_Majors_List[j][2], Students_Majors_List[j][1], GPA_List[i][1]]  
                                    print(Data)
                                    f=1
   
    if f==0 and r ==0.1:
        print("No such student")
    if f==0 and r ==0.25:
        print_Closest_Student()
    
    #print("*print_Students_DONE*")

    #return


##########################################################
######         print_Closest_Student                ######
##########################################################

def print_Closest_Student():

    f=0
    m_List = []
    for j in range(len(Students_Majors_List)):
        if Students_Majors_List[j][3] == major:
            for i in range(len(GPA_List)):
                if GPA_List[i][0] == Students_Majors_List[j][0]:
                    m_List.append(GPA_List[i])

    near_GPA = m_List[min(range(len(m_List)), key = lambda i: abs(float(m_List[i][1])-gpa))]

    for i in range(len(GPA_List)):
        if GPA_List[i][1] == near_GPA[1]:
            for j in range(len(Students_Majors_List)):
                if GPA_List[i][0] == Students_Majors_List[j][0]:
                    if Students_Majors_List[j][4] != 'Y' and Students_Majors_List[j][3]==major:
                        for k in range(len(Graduation_Dates_List)):
                            if  GPA_List[i][0] == Graduation_Dates_List[k][0]:
                                d1, m1, y1 = [int(x) for x in Graduation_Dates_List[j][1].split('/')]
                                b1 = date(y1, m1, d1)
                                b2 = date.today()
                                if b1<b2:
                                    Data = [Students_Majors_List[j][0], Students_Majors_List[j][2], Students_Majors_List[j][1], GPA_List[i][1]]  
                                    print(Data)
                                    f=1

    if f==0:
        print("No such student")
    #print("*print_Closest_Student_DONE*")

    #return

##########################################################
######                       MAIN                   ######
##########################################################

get_Students_Majors_List()
get_GPA_List()
get_Graduation_Dates_List()
save_Full_Roster()
save_List_Per_Major()
save_Scholarship_Candidates()
save_Disciplined_Students()

major_List = []
for i in range(len(Students_Majors_List)):
    if Students_Majors_List[i][3] not in major_List:
        major_List.append(Students_Majors_List[i][3])

while True:
    userQuery = input("Enter major and GPA:")

    for i in range(len(major_List)):
        if major_List[i] in userQuery:
            newQuery = userQuery.replace(major_List[i],"",1)
            major = major_List[i]
            break
                
        elif i+1==len(major_List):
            print("No such student")

    for i in range(len(major_List)):
        if major_List[i] in newQuery:
            print("No such student")
            break
               
        elif i+1==len(major_List):
            result = re.findall(r"[-+]?\d*\.\d+|\d+", userQuery)
            if len(result)!=1:
                print("No such student")
            else:
                gpa = float(result[0])
                print("Your student(s): ")
                print_Students(0.1)
                print("You may, also, consider:")
                print_Students(0.25)

    again = input("Another Query:")
    if again=="q":
        break

