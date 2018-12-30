
import RPi.GPIO as GPIO 
import SimpleMFRC522
import sys
from collections import namedtuple
import datetime
import time
#****************************************************************************************
#PROGRAM BY:    Krishaay J and Sahej A                                                  *
#SECTION:       Stemrobotics                                                            *
#DATE:          28 December 2018                                                        *            
#****************************************************************************************
GPIO.setwarnings(False)
reader = SimpleMFRC522.SimpleMFRC522()
# FUNCTION TO RETRIEVE STUDENT RECORD FROM THE DATABASE
def GetRecord(UID):
    with open("Student_Database.csv","r") as f:
         for line in f:
             line = line.rstrip()
             Myid,Nm,Std,RollNo,AdmNo,Lvl = line.split(",")
             if (Myid == str(UID)):
                 return(Nm,Std)

                
#END OF FUNCTION DEFINITION
#FUNCTION TO GET UID FROM RFID READER               
def GetUID():
    print("getting UID")
    Id,text=reader.read()
    print("UID is",Id)
    return(Id)

#END OF FUNCTION DEFINITION
#FUNCTION TO SAVE ATTENDANCE TO LOG
def SaveAtt(Att):
    f = open("Attendance_Log.csv","a+")
    f.write(Att[0] + ',' + Att[1] + ',' + Att[2] + ',' + Att[3] + ',' + Att[4]+ '\n')
    f.close()
    
#END OF FUNCTION DEFINITION
#  FUNCTION TO ADD AN ENTRY IN THE ATTENDANCE LOG
def AddAtt():
    print(" Entered att")
    Att = namedtuple("Att", "UID Name Std Dt Tm")
    UID = GetUID()
    Nm,Std = GetRecord(UID)
    Dt = datetime.datetime.now().strftime("%d/%m/%y")
    Tm = datetime.datetime.now().strftime("%H:%M:%S")
    newAtt = Att(str(UID), Nm, Std, Dt, Tm)
    SaveAtt(newAtt)
    print("data Written To Log")
    
#END OF FUNCTION DEFINITION
#***************************Main Program********************************#
while(1):
        AddAtt()
        time.sleep(5)
        
