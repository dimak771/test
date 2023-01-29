
import csv
import socket

csv_test = csv.reader(open('/Users/d_kuzmiankou/Documents/All_hosts_second_wave.csv'), delimiter=',')
outputFile = open('/Users/d_kuzmiankou/Documents/Defender_result.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
test_hostname = 'test'
MDAV_hostname = 'test1'
result = 'Defender not install'

for row1 in csv_test:
    test_hostname = row1[0]
    result = 'Defender not install'
    csv_mdav = csv.reader(open('/Users/d_kuzmiankou/Documents/MDAV.csv'), delimiter=',')
    for row2 in csv_mdav:
        MDAV_hostname = row2[1]
        if test_hostname == MDAV_hostname:
            result = 'Defender install'
    outputWriter.writerow([test_hostname, result])

outputFile.close()
