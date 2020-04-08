"""
Function Definitions
"""
def area(length,breadth):
    cal_area=  length * breadth    
    print("Area of Rectangle is :" + str(cal_area))
    pass

def perimeter(length, breadth):
    cal_peri = 2*(length+breadth)
    print("Perimeter of Rectangle is :" + str(cal_peri))
    pass
    
def volume(length,breadth,height):
    cal_vol = length * breadth * height
    print("Volume of Rectangle is :" + str(cal_vol))
    pass
    
def UI():
    print("Welcome to the Calculator!")
    print("I can help you calculate 1. Area 2.Perimeter 3. Volume 4.Exit")
    option = input('Enter your choice : ')
    return option
    
def decode(option):
    action = ''
    if option =='1':
        print("Calculating Area")
        l = int(input('Enter Length'))
        b = int(input('Enter Breadth'))
        area(l,b)
    elif option == '2':
        print("Calculating Perimeter")
        l = int(input('Enter Length'))
        b = int(input('Enter Breadth'))
        perimeter(l,b)
    elif option =='3':
        print("Calculating Volume")
        l = int(input('Enter Length'))
        b = int(input('Enter Breadth'))
        h = int(input('Enter Height'))
        volume(l,b,h)
    elif option =='4':
        action = 'Exit'
    else:
        print("Entered the wrong choice")
        
    return action
        
        
"""
main program / master
"""
todo = ''
while True:    
    var = UI()
    todo = decode(var)  
    if todo == 'Exit':
        break
print("Thank you")




