print('usman farid', 'section A', 'roll # 18B
#taking information from user
name=input('enter the name of the student: ')
father_name=input('enter the fathers name of the student: ')
roll_no=input('enter the roll number of the student: ')
disiplain=input('enter the disiplain of the student: ')
print('SCORES OUT OF HUNDRED')
print('english')
num1=int(input('enter the marks of english: '))
per1=(num1/100)*100
print('the student got', per1, 'percentage in english')
print('physics')
num2=int(input('the score of the physics: '))
per2=(num2/100)*100
print('the student got', per2, 'percentage in physics')
print('chemistry')
num3=int(input('enter the marks of chemistry: '))
per3=(num3/100)*100
print('the student got', per3, 'percentage in chemistry')
print('mathematics')
num4=int(input('enter the marks of maths: '))
per4=(num4/100)*100
print('the student got', per4, 'percentage in maths')
print('urdu')
num5=int(input('enter the marks of urdu: '))
per5=(num5/100)*100
print('the student got', per5, 'percentage in urdu')
#overall percentage
percentage=(per1+per2+per3+per4+per5)/5
print(percentage)
if (percentage>=90):
    print("grade:A")
elif (percentage>=80 and percentage<90):
    print("grade: B")
elif (percentage>=70 and percentage<80):
    print("grade: C")
elif (percentage>=60 and percentage<70):
    print("grade: D")
else:
    print("grade : F")
    print("student", name, "have to reapper in the exams")      
