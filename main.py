import csv
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt


class ChartData:
    def __init__(self):
        self.sumOfDays = [0.0] * 31  # do poprawy - nie każdy miesiąc ma 31 dni!!!!!!!!!!!!
        self.sumTotal = 0.0
        self.averageExpenses = 0.0

    def day_converter(self, daycopy, rowcopy):
        if daycopy[0] == '0':          # kasowanie pierwszej cyferki (format [00])
            daycopy = daycopy[1]

        self.sumOfDays[int(daycopy) - 1] += float(rowcopy["Amount"])
        self.sumTotal += float(rowcopy["Amount"])

    def sum_total(self):
        self.sumTotal = sum(self.sumOfDays)

    def average_expenses(self):
        self.average_expenses = self.sumTotal/len(self.sumOfDays)

# Obiekt zapisujący wykresy
pp = PdfPages("charts.pdf")
# Lista miesięcy
listOfMonths = []
for i in range(1, 14):
    listOfMonths.append(ChartData())

# Ciało programu
with open('csvFile.csv') as myFile:
    read = csv.DictReader(myFile, delimiter=';')

    # Wydobywanie informacji z pliku csv
    for row in read:
        if row['Type'] == '1':
            day, month, year = row['Operation date'].split('-')

            # Na razie tylko dwa miesiące
            if str(month) == '11':
                # Liczenie wydatków przypadający na kolejne dni
                listOfMonths[11].day_converter(str(day), row)
            else:
                listOfMonths[12].day_converter(str(day), row)


# Generowanie średniej oraz sumy
for i in listOfMonths:
    i.SumTotal()
    i.AverageExpenses()

# Prezentacja wyników
plt.subplot()
plt.bar(range(1, 32), listOfMonths[11].sumOfDays)
plt.ylabel('Rampapam')
plt.title("Listopad")
plt.gcf().text(0.2, 0.03, 'Sum:'+str(round(listOfMonths[11].sumTotal, 2))+' zł,'+'  Average expenses: ' +
               str(round(listOfMonths[11].averageExpenses, 2))+' zł', fontsize=14)
pp.savefig()
plt.show()
plt.bar(range(1, 32), listOfMonths[12].sumOfDays)
plt.title("Grudzień")
plt.gcf().text(0.2, 0.03, 'Sum:'+str(round(listOfMonths[12].sumTotal, 2) )+' zł,'+'  Average expenses: ' +
               str(round(listOfMonths[12].averageExpenses, 2))+' zł', fontsize=14)
pp.savefig()
plt.show()

pp.close()
