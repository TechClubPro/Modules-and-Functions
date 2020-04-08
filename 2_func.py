"""
Importing Libraries
"""
import pyttsx3 


"""
Global Variables
"""
todo = ''
engine = pyttsx3.init() # object creation
msg_list = ['Hello How are you!', 
            'Thank you very much',
            'I can calculate the area for you']
"""
Function Definitions
"""
def speech_init():
    
    engine.setProperty('rate', 125)     # setting up new voice rate
    engine.setProperty('volume',1)    # setting up volume level  between 0 and 1 
    
    voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female

def speakOut(msg):
    engine.say(msg)
    engine.runAndWait()
    
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

speech_init()
while True:    
    var = UI()
    todo = decode(var)  
    if todo == 'Exit':
        break
print("Thank you")
speakOut(msg_list[0])



