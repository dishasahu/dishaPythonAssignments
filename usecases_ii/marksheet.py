# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 19:26:11 2019

@author: abc
"""
#inputing the informatino
name_of_student = input("enter the name of the student")
name_of_father = input("enter the name of your father")
roll_number = input("enter your roll number")
course_name = input("enter the course name")
sub1 = int(input("enter the marks of 1st subject"))
sub2 = int(input("enter the marks of 2nd subject"))
sub3 = int(input("enter the marks of 3rd subject"))
sub4 = int(input("enter the marks of 4th subject"))
sub5 = int(input("enter the marks of 5th subject"))
sub1_name="SUBJECT1"
sub2_name="SUBJECT2"
sub3_name="SUBJECT3"
sub4_name="SUBJECT4"
sub5_name="SUBJECT5"
#calculating the values
total = (sub1+sub2+sub3+sub4+sub5)
percent= (total*100)/500

#displaying the information
print( "|" + " " * 24 + "~" * 5 + "*" * 20 + "~" * 5 + " " * 24 + "|" )
print( "|" + "-" * 78 + "|" )
print( "|" + " " * 78 + "|" )
print("|" + " " * 15 + "RAJIV GANDHI PROUDYOGIKI VISHWAVIDYALAYA,BHOPAL" + " " * 15 + " " + "|")
print( "|" + " " * 78 + "|" )
print( "|" + "-" * 30 + "STATEMENT OF GRADE" + "-" * 30 + "|" )
print("|" + " " * 9 + "Bachelor's Of Technology," +  "{:^35}".format(course_name) + " " * 9 + "|")
print( "|" + " " * 78 + "|" )
print("|" + " " + "ROLL NO." + " " * 2 + ":" + "{:^12}".format(roll_number) + " " * 54 + "|")
print("|" + " " + "NAME OF STUDENT" + " " * 2 + ":" + "{:<20}".format(name_of_student) + " " * 39 + "|")
print("|" + " "* 18 + ":" + "S/D/W" + " " + "{:<20}".format(name_of_father) + " " * 33 + "|")
print( "|" + "-" * 78 + "|" )
print( "|" + " " * 78 + "|" )
print("|" + "{:<18}".format("SUBJECT CODE") + "|" + "{:^40}".format("STUDENT NAME") + "|" + "{:>18}".format("MARKS OBTAINED") + "|")
print("|" + " " * 18 + "|" + " " * 40 + "|" + " " * 18 + "|")
print("|" + "{:^18}".format("S01") + "|" + "{:^40}".format(sub1_name) + "|" + "{:>18}".format(sub1) + "|")
print("|" + " " * 18 + "|" + " " * 40 + "|" + " " * 18 + "|")
print("|" + "{:^18}".format("S02") + "|" + "{:^40}".format(sub2_name) + "|" + "{:>18}".format(sub2) + "|")
print("|" + " " * 18 + "|" + " " * 40 + "|" + " " * 18 + "|")
print("|" + "{:^18}".format("S03") + "|" + "{:^40}".format(sub3_name) + "|" + "{:>18}".format(sub3) + "|")
print("|" + " " * 18 + "|" + " " * 40 + "|" + " " * 18 + "|")
print("|" + "{:^18}".format("S04") + "|" + "{:^40}".format(sub4_name) + "|" + "{:>18}".format(sub4) + "|")
print("|" + " " * 18 + "|" + " " * 40 + "|" + " " * 18 + "|")
print("|" + "{:^18}".format("S05") + "|" + "{:^40}".format(sub5_name) + "|" + "{:>18}".format(sub5) + "|")
print("|" + " " * 18 + "|" + " " * 40 + "|" + " " * 18 + "|")
print("|" + " " * 18 + "|" + " " * 40 + "|" + " " * 18 + "|")
print( "|" + "-" * 78 + "|" )
print( "|" + " " * 78 + "|" )
print("|" + " " * 60 + "{:<10}".format("TOTAL") + "" + ":" + "{:>7}".format(total) + "|")
print("|" + " " * 60 + "{:<10}".format("PERCENT") + "" + ":" + "{:>7}".format(percent) + "|")
print( "|" + "-" * 78 + "|" )




