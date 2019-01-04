print('khurram khalil')
print('18B-81-CS', 'section A')
print('QUESTION NO 2')
#getting user information
name = input('enter your name: ')
father_name = input('enter your fathers name: ')
roll_no = input('enter your roll number: ')
subject = input('enter the subject name: ')
if subject=='enlish':
    marks = (input('enter marks obtained in english: ')
    #marks will be out of 150
    percentage =(marks/150)*100
    if percentage=>50
        print('the student', name, 'is passed in english subject')
    else:
        print('the student', name, 'is fail in english subject)
        print(name,'onlt got', percentage, '%')
                      
else:
    user=input('look for another subject: ')
    if subject=='urdu':
        marks = (input('enter marks obtained in urdu: ')
        #marks will be out of 150
        percentage =(marks/150)*100
        if percentage=>50
            print('the student', name, 'is passed in urdu subject')
        else:
            print('the student', name, 'is fail in urdu subject)
            print(name,'onlt got', percentage, '%')
     else:
        user=input('look for another subject: ')
        if subject=='islamiyt':
            marks = (input('enter marks obtained in islamiyt: ')
            #marks will be out of 150
            percentage=(marks/150)*100
            if percentage=>50
                print('the student', name, 'is passed in islamiyt subject')
            else:
                print('the student', name, 'is fail in islamiyt subject)
                print(name,'onlt got', percentage, '%')
        else:
            user=input('look for another subject: ')
            if subject=='maths':
                marks = input('enter marks obtained in maths: ')
                #marks will be out of 150
                percentage =(marks/150)*100
                if percentage=>50
                    print('the student', name, 'is passed in maths subject')
                else:
                    print('the student', name, 'is fail in maths subject)
                    print(name,'onlt got', percentage, '%')
            else:
                user=input('look for another subject: ')
                if subject=='history':
                    marks = (input('enter marks obtained in history: ')
                    #marks will be out of 150
                    percentage =(marks/150)*100
                    if percentage=>50
                        print('the student', name, 'is passed in history subject')
                    else:
                        print('the student', name, 'is fail in history subject)
                        print(name,'onlt got', percentage, '%')
               else:
                    print('we dont have results other then these subjects, bubye!') 
                                  
