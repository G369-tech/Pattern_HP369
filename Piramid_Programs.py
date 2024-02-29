print('----------- HP369 -----------')

try:
    #take input from user
    r = int(input("Enter raw of piramid:"))
    
    for i in range(0,r):
        star = "*" * (i+1)
        print(star)

    print('--'*i)
    
    for i in range(1,r+1):
        star = "*" * i
        space = " " * (r-i)
        print(space + star)

    print('--'*i)
          
    for i in range(1,r+1):
        star = "*" * i
        star1 = "*" * (i-1)
        space = " " * (r-i)
        print(space + star + star1)

    print('--'*i)
    
    for i in range(0,r):
        star = "*" * (r-i)
        space = " " * i
        print(space + star)

    print('--'*i)

    for i in range(0,r):
        star = "*" * (r-i)
        print(star)

    print('--'*i)
          
    for i in range(0,r):
        star = "*" * (r-i)
        star1 = "*" * (r-i-1)
        space = " " * i
        print(space + star + star1)
        
except:
    print('Enter Valid Input.....')
