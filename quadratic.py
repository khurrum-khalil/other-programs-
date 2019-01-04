print('fatima ilyas')
print('18B-059-CS, section A','QUESTION NO 01' )

#user input values of A B and C
a = int(input('enter the value of a: '))
b = int(input('enter the value of b: '))
c = int(input('enter the value of c: '))
#for denominator
den = 2*a
if den==0:
    print ('the equation cannot solve because it has zero division')
else:
    print ('this equation can be solved and the answer are given below')
    #formula
    #import complex math module   
    import cmath    
    x1=(-b+cmath.sqrt((b**2)-4*a*c)/2*a)
    x2=(-b+cmath.sqrt((b**2)-4*a*c)/2*a)
    print ('following are the answers of the given Quadratic Equation:', x1, 'and', x2)
    
                  
          
