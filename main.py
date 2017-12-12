import csv
import matplotlib.pyplot as plt
import calendar

sumOfDays= [0.0] * 31
sumTotal=0.0
averageExpenses=0.0
months=list(range(1,13))

listOfMonths=[]


class ChartData:
    def __init__(self):
        self.sumOfDays = [0.0] * 31
        self.sumTotal = 0.0
        self.averageExpenses = 0.0
        self.months = list(range(1, 13))

    def DayConverter(self,dayCopy,row):
        if (dayCopy[0] == '0'):
            dayCopy = dayCopy[1]  # nie rozumiem
        self.sumOfDays[int(dayCopy) - 1] += float(row["Amount"])

for i in list(range(1,13)):
    listOfMonths.append(ChartData() )
    print(str(i))


def DayConverter(dayCopy):
    if (dayCopy[0] == '0'):
        dayCopy = dayCopy[1] # nie rozumiem
    sumOfDays[int(day) - 1] += float(row["Amount"])


with open('csvFile.csv') as myFile:
    read = csv.DictReader(myFile, delimiter=';')
    print(months)

    #Wydobywanie informacji z pliku csv
    for row in read:
        if (row['Type'] == '1'):
            day, month, year = row['Operation date'].split('-')
            if(str(month)=='11'):
                print(str(day),str(month))
                #Liczenie wydatków przypadający na kolejne dni
                DayConverter(day)
            elif(str(month)=='12'):
                print(str(day), str(month))
                DayConverter(day)



#Wyniki
sumTotal=sum(sumOfDays)
averageExpenses=sumTotal/len(sumOfDays)
print("Suma: "+str(sumTotal))
print("Średnia: "+str(averageExpenses))
names=list(range(1,32)) # do obadania jutro
plt.bar(names, sumOfDays)
plt.ylabel('Rampapam')
#plt.show()




