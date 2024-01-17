#!/usr/bin/env python
# coding: utf-8

# In[48]:


def mind_game():
    # Mind game
    import time

    #welcome user
    print('Welcome To Mind Guessing AI!')
    time.sleep(3)

    #Ask to user guess a number
    print('Guess number in your mind')
    time.sleep(3)

    # Ask user to double the number
    print('Ok now double whichever number you have guess')
    time.sleep(3)

    import random
    num=0

    for i in range(4):
        # Ask usr to add 50 in it
        temp_num=random.randrange(1,100)
        num=num+temp_num
        print('Alright! Now add', temp_num,'in it!')
        time.sleep(3)


    # Ask user to divide the number by 2
    print('ok now divide the number by 2')
    time.sleep(3)

    #Ask user to Minus the original guess number
    print('Finally minus the number which you guessed erlier')
    time.sleep(3)

    #ask user to minus the which you guessed erlier
    print('minus the which you guessed erlier')
    time.sleep(3)

    #Show final asswer
    print('Im thinking...')
    time.sleep(3)

    #
    print('Answer might be...')
    time.sleep(3)

    print('Yes! Found It!')
    print('The asnwer is',num/2)
    

def travel_budget():
    # THANE TO AIRPORT BOT
    #WELCOME USER
    print('Welcome to Travel Recomendation Bot(Mumbai Airport)')
    #Ask user its name
    user_name=input('Please enter youre name here')
    #Greet User
    print('Hello:',user_name.title())
    #Ask user its budget
    budget=int(input('Please enter youre budget here: '))
    #500 ola se ja
    if budget>=500:
        print('Ola se ja')
    #100-500 then auto se ja
    elif budget>=100 and budget<=100:
        print('auto se ja')
    #50-100 then bus se ja
    elif budget>=50 and budget<=100:
        print('bus se ja')
    #10-50 train se ja
    elif budget>=10 and budget<=50:
        print('train se ja')
    #10 ghrar pe ja
    else:
        print('Ghar pe ja')
        
        

def password_generator():
    #password generator
    #Welcome user
    print('welcome t password genrator!')
    #take len of password as an input
    num=int(input('Enter number of character of your password'))
    #password should contain lowercse, uppercase,symbols and numerical values
    import random
    import string
    password=''
    char=string.ascii_letters+string.digits+string.punctuation
    for i in range(num):
        password=password+(random.choice(char))
        print(password)



def countdown():        
    #Crete a countdown
    from countdown import countdown
    user_input_mins=int(input('Enter a minute'))
    user_input_secs=int(input('Enter a seconds'))
    countdown(mins=user_input_mins, secs=user_input_secs)

    print('Times Up!')


    
def gk_quiz():    
    # Nettech Bot
    #Welcome user
    print('Welcome to India GK Quiz')
    user_location=input('What is a nationa animal of India')
    if user_location=='Tiger':
        print('Yes you are correct')
    else:
        print('Sorry your answer is incorrect')
    



def chai_recommandation():   
    #mumbai based chai recommandation bot
    #welcome use to mumbai
    print('Welcome to mumbai city')
    #ask user to name
    user_name=input("What's your good name? ")
    #greaing user# ask user to its bugedet
    print('hello',user_name.title())
    # ask user to its budget
    budget=int(input('Please enter your budget:'))
    #500--- go to taj hotel
    if budget>=500:
        print('Go to Taj hotel')
    #100-500---starbucks
    elif budget>=100 and budget<500:
        print('Please go to starbucks')
    #50-100----udipi
    elif budget>=50 and budget<100:
        print('Please go to udipi')
    #10-50------tapari
    elif budget>=100 and budget<500:
        print('Please go to tapari')
    #<10 n hotes available
    else:
        print('No hotes available')    
        


def trip_recommndation():        
    #make my trip recommandation hotels
    #welcome user in 
    print('welcome to make my trip')
    #Ask user its details
    user_name=input('please enter your good name:')
    mobile_no=input('please enter your mobile number: ')
    age=input('please enter your age:  ')
    members=input('please enter how many members: ')
    print('hello',user_name.title(),mobile_no,age,members)
    #please enter city
    city=input('please enter city are you interested:  ')
    #please ask user budget plan
    budget=int(input('please enter your budget'))
    if budget>=5000:
        print('please go to 5 star hotels')
    elif budget>=4000 and budget<5000:
        print('please go to 3 star hotels')
    elif budget>=2000 and budget<4000:
        print('please go to 2 star hotels')
    elif budget>=1000 and budget<2000:
        print('please go to normal hotels')    
    else:
        print('no hotels available')
        
        
        
         
#Library
import tkinter as tk


#Main Window
window=tk.Tk()


#Window size
window.geometry('600x460')


#Window Title
window.title("Nitesh's Python Portfolio")



#lable UI
tk.Label(window,text='PYTHON PROJECTS',font=('Halvetica',18,'bold')).place(x=200,y=20)
tk.Label(window,text='Made By: Nitesh C',font=('Halvetica',12)).place(x=245,y=70)



#Buttons--Start
tk.Button(window,text='Mind Game',command=mind_game,).place(x=30,y=140,width=160,height=40)
tk.Button(window,text='Travel Budget',command=travel_budget).place(x=220,y=140,width=160,height=40)
tk.Button(window,text='Password Generator',command=password_generator).place(x=410,y=140,width=160,height=40)
tk.Button(window,text='Countdown',command=countdown).place(x=30,y=210,width=160,height=40)
tk.Button(window,text='GK Quiz',command=gk_quiz).place(x=220,y=210,width=160,height=40)
tk.Button(window,text='Chai Recommandation',command=chai_recommandation).place(x=410,y=210,width=160,height=40)
tk.Button(window,text='Trip Recomandation',command=trip_recommndation).place(x=220,y=280,width=160,height=40)






#Main Loop ye agar nahi likhoge to UI nahi dikhega
window.mainloop()


# In[ ]:




