import csv
with open('/home/viky/Descargas/FL_insurance_sample.csv/FL_insurance_sample.csv') as csvfile:
    lector = csv.DictReader(csvfile)
    print (lector.fieldnames)
    condado = lector.fieldnames[2]
    print(condado)
    for fila in lector:
        print(fila[condado])



