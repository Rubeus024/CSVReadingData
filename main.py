import csv
import matplotlib.pyplot as plt
import calendar

with open('csvFile.csv') as myFile:
    sumOfDays= [0.0] * 31
    read = csv.DictReader(myFile, delimiter=';')
    sumTotal=0.0
    averageExpenses=0.0

    #Wydobywanie informacji z pliku csv
    for row in read:
        if (row['Type'] == '1'):
            day, month, year = row['Operation date'].split('-')
            #Liczenie wydatków przypadający na kolejne dni
            if(day[0]=='0'):
                day=day[1]
            sumOfDays[int(day) - 1]+=float(row["Amount"])


#Wyniki
sumTotal=sum(sumOfDays)
averageExpenses=sumTotal/len(sumOfDays)
print("Suma: "+str(sumTotal))
print("Średnia: "+str(averageExpenses))
names=list(range(1,32)) # do obadania jutro
plt.bar(names, sumOfDays)
plt.ylabel('Rampapam')
plt.show()


