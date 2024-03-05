import csv



with open("FIOandTelephone.csv",'r', encoding='UTF-8-sig') as r:
    reader = csv.DictReader(r)
    fio = input()
    for row in reader:
        if fio == row['FIO']:
            print("Телефон человека: ", row['Telephone'])
        else:
            continue