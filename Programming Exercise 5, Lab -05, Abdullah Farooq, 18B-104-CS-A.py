print('Programming Exercise 5')

def marksheet():
    stu_name =(input("Enter the student's name: "))
    father_name = (input("Enter the father's name: "))
    stu_id = eval(input("Enter the student's id: "))
    sub_eng = eval(input("Enter English marks: "))
    sub_maths = eval(input("Enter Maths marks: "))
    sub_urdu = eval(input("Enter Urdu marks: "))
    sub_comp = eval(input("Enter Computer marks: "))
    sub_isl = eval(input("Enter Islamiat marks: "))
    total_marks =(sub_eng+sub_maths+sub_urdu+sub_comp+sub_isl)
    percentage = (total_marks/500)*100
    if percentage in range(90,100+1):
        grade = "A+"
    elif percentage in range(80,90):
        grade = "A"
    elif percentage in range(70,80):
        grade = "B"
    elif percentage in range(60,70):
        grade = "C"
    elif percentage in range(50,60):
        grade = "D"
    else:
        grade = "F"
    print("Student Name: ",stu_name)
    print("Father's name: ",father_name)
    print("Student ID: ",stu_id)
    print("")
    print("Subject","\t", "Marks Obtained")
    print("Emglish", "\t", sub_eng)
    print("Maths ","\t","\t", sub_maths)
    print("Urdu ","\t","\t", sub_urdu)
    print("Computer", "\t", sub_comp)
    print("Islamiat", "\t", sub_isl)
    print("Final Grade: ","\t",grade)
    print("Percentage:", percentage,"%")
