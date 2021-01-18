#! /usr/bin/python3

import csv
import random

lines=30
random_range = 1000

with open ('random_values.csv',mode='w') as rand_val_file:
    random_writer = csv.writer(rand_val_file, delimiter=',')

    random_writer.writerow(['index','range','value'])

with open ('random_values.csv',mode='a') as rand_val_file:
    random_writer = csv.writer(rand_val_file, delimiter=',')

    for i in range (lines):
        u = random.randint(0,random_range)
        random_writer.writerow([1,random_range, u])

with open('random_values.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            """line_count += 1"""
        print(f'\t index {row["index"]} range{row["range"]} value {row["value"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')