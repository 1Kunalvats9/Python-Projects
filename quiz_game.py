#mini quiz project in which computer will ask some questions and if answer is correct you will get 1 point...
print("Welcome to my computer quiz!")
ask = input('Do you want to play the game? ')
if ask.lower() =='no':
    quit()
print("Okay let's play :) \nHere's the first question:- ")
sum = 0
que1= input('What does RAM stand for ')
if que1.lower() =='random access memory':
    print('correct!')
    sum+= 1
else:
    print('incorrect')


que2= input('What does CPU stand for ')
if que2.lower() =='central processing unit':
    print('correct!')
    sum+= 1
else:
    print('incorrect')

que3= input('What does Gpu stand for ')
if que3.lower() =='graphics processing unit':
    print('correct!')
    sum+= 1
else:
    print('incorrect')



que4= input('What does PSU stand for ')
if que4.lower() =='power supply':
    print('correct!')
    sum+= 1
else:
    print('incorrect')


result = 'congrats you got ' + str(sum) + ' questions corrrect out of 4.'
print(result + " Your score was " + str((sum/4)*100) + "%")
