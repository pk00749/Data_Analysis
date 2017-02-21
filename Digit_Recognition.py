import csv
from fs.osfs import OSFS


with open('train.csv') as train_file:
    lines = csv.reader(train_file)

