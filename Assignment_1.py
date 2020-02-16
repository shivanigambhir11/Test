import csv
import statistics

Steps = []
RestingHeartRate = []
ActiveHeartRate = []

with open('csv_input.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

        Steps.append(row[1])
        RestingHeartRate.append(row[2])
        ActiveHeartRate.append(row[3])
Steps.pop(0)
Steps = list(map(int, Steps))  # to convert string to int value

RestingHeartRate.pop(0)
RestingHeartRate = list(map(int, RestingHeartRate))

ActiveHeartRate.pop(0)
ActiveHeartRate = list(map(int, ActiveHeartRate))

# print(statistics.mean(Steps))
# print (statistics.mean(RestingHeartRate))
# print(statistics.mean(ActiveHeartRate))

# print(statistics.median(Steps))
# print (statistics.median(RestingHeartRate))
# print(statistics.median(ActiveHeartRate))

# print (max (Steps)- min (Steps))


with open('mycsv.csv', 'w', newline='')as newcsv:
    writer = csv.writer(newcsv)

    writer.writerow(['Activity', 'Mean', 'Median ', 'Range'])
    writer.writerow(['Steps', statistics.mean(Steps), statistics.median(Steps), (max(Steps) - min(Steps))])

    writer.writerow(['RestingHeartRate', statistics.mean(RestingHeartRate), statistics.median(RestingHeartRate),
                     (max(RestingHeartRate) - min(RestingHeartRate))])

    writer.writerow(['ActiveHeartRate', statistics.mean(ActiveHeartRate), statistics.median(ActiveHeartRate),
                     (max(ActiveHeartRate) - min(ActiveHeartRate))])

with open('mycsv.csv') as mycsv:
    reader = csv.reader(mycsv)
    for row in reader:
        print(row)

# Extra Challenge - split the data by each day of the week then write it to a csv in this format:
# Day of the Week | Mean Steps | Median Steps | Range of Steps | etc


# Monday = []
# Tuesday = []
# Wednesday = []
# Thursday = []
# Friday = []
# Saturday = []
# Sunday = []

# print (reader)

# for i in range(1,35,7):
#   Monday.append(reader[i])

# for row in range(1,reader,7):
#     print (row)
