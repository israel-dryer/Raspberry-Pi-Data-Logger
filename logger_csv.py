import csv
import psutil as ps
from datetime import datetime
from time import sleep

class Logger:
    def __init__(self):
        self.data_dict = {}

    def collect_data(self):
        ''' collect data and assign to class variable '''
        self.data_dict['cpu'] = (datetime.now(), *ps.cpu_times())
        self.data_dict['vmemory'] = (datetime.now(), *ps.virtual_memory())
        
    def print_data(self):
        ''' print select data in nicely formatted string '''
        print("-"*120)
        print("~~ {0:%Y-%m-%d, %H:%M:%S} ~~".format(*self.data_dict['cpu']))
        print("CPU TIME // User: {1:,.0f}, System: {3:,.0f}, Idle: {4:,.0f}".format(*self.data_dict['cpu']))
        print("VIRT MEM // Total: {1:,d}, Available: {2:,d}".format(*self.data_dict['vmemory']))

    def log_data(self):
        ''' log the data into csv files '''
        for file, data in self.data_dict.items():
            with open('data/' + file + '.csv', 'a+', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(data)

def main():
    while True:
        logger = Logger()
        logger.collect_data()
        logger.log_data()
        logger.print_data()
        sleep(5)

main()
