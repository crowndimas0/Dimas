#Program to calculate temperature in Jakarta for one mounth.

print("Welcome to program to calculate temperature in Jakarta")

D = int(input("Enter the number of days in a month = ")) #enter the number of days in a month 27<D<=31

#looping
if(27<D<=31) :
    TabFloat = [0 for i in range(D)]
    sum = 0
    print("Enter temperature in days (°Celecius)")
    for i in range(0,D):
        print ("Temperatur in days ",i+1) 
        TabFloat[i] = float(input())
        sum= sum+TabFloat[i]

    #formula
    average = sum/D
    Maximum = max(TabFloat)   
    Minimum = min(TabFloat)

    print ("Based on the data that has been inputted, it is generated : ")
    print ('Average temperature in Jakarta : ', average, "°C")
    print ("The maximum temperature : ", Maximum, "°C" ) 
    print ("The minimum temperature  : ", Minimum, "°C" ) 
    print ("Congrats, the calculating temperature in Jakarta done")
else :
    print ('sorry, please input data very well')
