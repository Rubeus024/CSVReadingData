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
        self.averageExpenses = self.sumTotal/len(self.sumOfDays)

# Obiekt zapisujący wykresy
pp = PdfPages("charts.pdf")


monthDict = { 0 : 'Styczeń', 1 : 'Luty', 2 : 'Marzec', 3 : 'Marzec', 4 : 'Kwiecień', 5 : 'Maj', 6 : 'Czerwiec', 7 : 'Lipiec',
              8: 'Sierpień',
              9: 'Wrzesień',
              10: 'Październik',
              11: 'Listopad',
              12: 'Grudzień',
              }


# Lista miesięcy
listOfMonths = []
for obj in range(1, 14):
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


# Generowanie średniej, sumy oraz zapisywanie wyników
counter = 0 # można to poprawić?
for obj in listOfMonths:
    obj.sum_total()
    obj.average_expenses()
    if obj.sumTotal != 0:
        plt.bar(range(1, 32), listOfMonths[counter].sumOfDays)
        plt.ylabel('zł')
        plt.title(monthDict[counter])
        plt.gcf().text(0.2, 0.03, 'Sum:' + str(round(obj.sumTotal, 2)) + ' zł,' + '  Average expenses: ' +
                       str(round(obj.averageExpenses, 2)) + ' zł', fontsize=14)
        pp.savefig()
        plt.show()
    counter += 1

pp.close()
