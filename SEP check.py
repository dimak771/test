
import csv
import socket

csv_test = csv.reader(open('/Users/d_kuzmiankou/Documents/All_hosts_second_wave.csv'), delimiter=',')
outputFile = open('/Users/d_kuzmiankou/Documents/SEP_result.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
test_hostname = 'test'
for row1 in csv_test:
    test_hostname = row1[0]
    csv_SEP = csv.reader(open('/Users/d_kuzmiankou/Documents/total_endpoint.csv'), delimiter=',')
    result = 'SEP not install'
    for row2 in csv_SEP:
        SEP_hostname = row2[0]
        if test_hostname == SEP_hostname:
            result = 'SEP install'
            
    outputWriter.writerow([test_hostname, result])

outputFile.close()

















