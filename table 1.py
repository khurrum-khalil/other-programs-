print('khurram khalil')
print('18B-81-CS', 'section A')
print('QUESTION NO 04')
table = [[row*col for row in range(1,10)]for col in range(1,10)]
frst_val= int(input('enter the first value: '))
lst_val=int(input('enter the last value: '))
for row in range(lst_val):
    print("\n")
    for col in range(lst_val):
        print(table[row][col], " ") 
