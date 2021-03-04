birthday = [int(input("Day (Integer):")), int(input("Month (Integer):")), int(input("Year (Integer):"))]
week_ref = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] #index corresponds to h value

#haven't bothered with input validation as not neccessary

q = birthday[0] #q is the day of birth

if (0 < birthday[1] <= 2): #if month is jan or feb
    m = 12 + birthday[1] #january = 13, feb = 14
    year = birthday[2]-1 #year is previous year
else:
    m = birthday[1] #if other month
    year = birthday[2] #year is the same as input

K =int(str(year)[2:4]) #K is the year within century
J=int(str(year)[0:2])   #J is the century

h = (q + ((((m+1)*26))//10)+ K +(K//4) + (J//4) -2*J)%7 #zeller's equation to calc. integer relating to day

print(str(birthday[0])+"/"+str(birthday[1])+"/"+str(birthday[2])+" is a "+week_ref[h])  #output the weekday which corresponds to h 
