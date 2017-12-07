import csv
import matplotlib.pyplot as plt
import calendar

with open('csvFile.csv') as myFile:
    daySumEnchanced=[0.0]*31
    read = csv.DictReader(myFile, delimiter=';')
    sumTotal=0
    for row in read:
        # print(row.__class__)
        if (row['Type'] == '1'):
            day, month, year = row['Operation date'].split('-')

            if(day[0]=='0'):
                day=day[1]
            daySumEnchanced[int(day)-1]+=float(row["Amount"])


            #print(day + "  miesiac: " + month + "   rok: " + year)

sum=sum(daySumEnchanced)
print(sum)
names=list(range(1,32)) # do obadania jutro
plt.bar(names,daySumEnchanced)
plt.ylabel('Rampapam')
#plt.show()
print("Changes!")
print("blabla")

