import csv

from matplotlib import pyplot as plt
from datetime import datetime

file_1 = '.\project2\death_valley_2014.csv'
with open(file_1) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates_1, highs_1, lows_1 = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])        
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates_1.append(current_date)
            highs_1.append(high)
            lows_1.append(low)
    
    print("dates in death_valley: " + str(len(dates_1)))

file_2 = '.\project2\sitka_weather_2014.csv'
with open(file_2) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates_2, highs_2, lows_2 = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])        
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates_2.append(current_date)
            highs_2.append(high)
            lows_2.append(low)
    
    print("dates in sitka: " + str(len(dates_2)))

#plot data
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates_1, highs_1, c='red', alpha=0.5)
plt.plot(dates_2, highs_2, c='red', alpha=0.5)
#plt.fill_between(dates_1, highs_1, highs_2, facecolor='blue', alpha=0.1)

plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA", fontsize = 24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()