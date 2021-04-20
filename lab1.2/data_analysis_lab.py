#!//usr/bin/python3

from matplotlib import pyplot
from openpyxl import load_workbook

def getvalue (x):
    return x.value

xlsx_file = load_workbook('data_analysis_lab.xlsx')

data_list = xlsx_file['Data']

#
#data_list['A'][1:]

years_list = list(map(lambda x: x.value, data_list['A'][1:]))
#debug
#print(years_list_value)

temperature_list = list(map(getvalue, data_list['C'][1:]))

#debug
#print(temperature_list)

sun_activity_list = list(map(getvalue, data_list['D'][1:]))

#debug
#print(sun_activity_list)

pyplot.plot(years_list, temperature_list)
pyplot.plot(years_list, sun_activity_list)


pyplot.show()