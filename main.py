import csv
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt


class CategoryData:

    def __init__(self):
        self.categoryAmount=0.0;

    def add(self,categoryamount):
        self.categoryAmount+=categoryamount

class ChartData:
    def __init__(self, monthstring='', numberofdays=30):
        self.categoryList = {'Jedzenie': 0.0, 'Czynsz': 0.0, 'Transport': 0.0, 'Odzież': 0.0,
                             'Buty': 0.0, 'Zabawa': 0.0}
        self.numberOfDays = numberofdays
        self.monthString = monthstring
        self.sumOfDays = [0.0] * self.numberOfDays
        self.sumTotal = 0.0
        self.averageExpenses = 0.0

    def day_converter(self, daycopy, rowcopy):
        if daycopy[0] == '0':          # kasowanie pierwszej cyferki (format [00])
            daycopy = daycopy[1]

        self.sumOfDays[int(daycopy) - 1] += float(rowcopy["Amount"])
        self.sumTotal += float(rowcopy["Amount"])

    def sum_total(self):
        self.sumTotal = sum(self.sumOfDays)

    def average_expenses(self):  # do przerobienia
        self.averageExpenses = self.sumTotal / self.numberOfDays

    def add(self,categoryamount, string):
        self.categoryList[string] += categoryamount

# Obiekt zapisujący wykresy
pp = PdfPages("charts.pdf")

# Lista miesięcy
listOfMonths = {'00': ChartData('Styczeń', 31), '01': ChartData('Styczeń', 31), '02': ChartData('Luty', 28),
                '03': ChartData('Marzec', 31),
                '04': ChartData('Kwiecień', 30),'05': ChartData('Maj', 31),
                '06': ChartData('Czerwiec', 30), '07': ChartData('Lipiec', 31),
                '08': ChartData('Sierpień', 31), '09': ChartData('Wrzesień', 30), '10': ChartData('Październik', 31),
                '11': ChartData('Listopad', 30), '12': ChartData('Grudzień', 31)}

#for obj in range(1, 14):
#    listOfMonths.append(ChartData())


# Ciało programu
with open('csvFile.csv') as myFile:
    read = csv.DictReader(myFile, delimiter=';')

    # Wydobywanie informacji z pliku csv
    for row in read:
        if row['Type'] == '1':
            day, month, year = row['Operation date'].split('-')
            #print(row['Category name'])
            # Na razie tylko dwa miesiące

                # Liczenie wydatków przypadający na kolejne dni
            listOfMonths[month].day_converter(str(day), row)
            if row['Category'] in listOfMonths[month].categoryList:
                listOfMonths[month].add(float(row['Amount']), row['Category'])



# Generowanie średniej, sumy oraz zapisywanie wyników
counter = 0 # można to poprawić?
for key,value in listOfMonths.items():
    for key1,value1 in value.categoryList.items():
        print(key,value1)
    value.sum_total()
    value.average_expenses()
    if value.sumTotal != 0:
        plt.bar(range(1, value.numberOfDays+1), value.sumOfDays)
        plt.ylabel('zł')
        plt.title(value.monthString+' - dzienne wydatki')
        plt.gcf().text(0.2, 0.03, 'Sum:' + str(round(value.sumTotal, 2)) + ' zł,' + '  Average expenses: ' +
                       str(round(value.averageExpenses, 2)) + ' zł', fontsize=12)
        pp.savefig()
        plt.show()
        plt.close()

        plt.bar(value.categoryList.keys(), value.categoryList.values())
        plt.ylabel('zł')
        plt.title('{} - podział na kategorie'.format(value.monthString))
        pp.savefig()
        plt.show()
    counter += 1

pp.close()
