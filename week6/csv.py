import csv

def read(file_path):

  with open(file_path) as file:
    csv_reader = csv.reader(file)

    headings = next(csv_reader)
    print(f"Headings: \n{headings}")

    print("Values:")
    for values in csv_reader:
      print(values)

def run_task1():
  read("test22.csv")

run_task1()