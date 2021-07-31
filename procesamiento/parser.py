import csv
import json
codcurso_nombrecurso = {}
codcurso_departamento = {}
codcurso_dataporciclo = {}
compacto = 'compacto.csv'
with open(compacto, encoding='UTF8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',',)
    header = True
    for row in csv_reader:
        if header:
            header = False
        else:
            codcurso = row[0]
            nombrecurso = row[1]
            departamento = row[2]
            matri = row[3]
            prema = row[4]
            ciclo = row[5]
            if codcurso not in codcurso_nombrecurso:
                codcurso_nombrecurso[codcurso] = nombrecurso
                codcurso_departamento[codcurso] = departamento
                codcurso_dataporciclo[codcurso] = {}
            codcurso_dataporciclo[codcurso][ciclo] = [prema, matri]


header = ['numeroCiclo', 'ciclo', 'esVerano',
          'prematriculados', 'matriculados']


revisarCiclos = ['2021 - 1', '2021 - 0', '2020 - 2', '2020 - 1']
ciclo_numero = {'2012 - 1': 1, '2012 - 2': 2, '2013 - 0': 3, '2013 - 1': 4,
                '2013 - 2': 5, '2014 - 0': 6, '2014 - 1': 7,
                '2014 - 2': 8, '2015 - 0': 9, '2015 - 1': 10, '2015 - 2': 11, '2016 - 0': 12,
                '2016 - 1': 13, '2016 - 2': 14, '2017 - 0': 15,
                '2017 - 1': 16, '2017 - 2': 17, '2018 - 0': 18, '2018 - 1': 19, '2018 - 2': 20,
                '2019 - 0': 21, '2019 - 1': 22, '2019 - 2': 23,
                '2020 - 0': 24, '2020 - 1': 25, '2020 - 2': 26, '2021 - 0': 27, '2021 - 1': 28}

cont = 0
metadata = 'metadata.csv'
headermetadata = ['codcurso', 'path']
with open(metadata, 'a', encoding='UTF8', newline='') as fi:
    writer = csv.writer(fi)
    writer.writerow(headermetadata)

for codcurso in codcurso_dataporciclo:
    filename = "dataCurso/" + codcurso + ".csv"
    allfilas = []
    fila = []
    cantAbiertos = 0
    for ciclo in codcurso_dataporciclo[codcurso]:
        if ciclo in revisarCiclos:
            cantAbiertos += 1
        fila.append(ciclo_numero[ciclo])
        fila.append(ciclo)

        if ciclo.find("- 0") != -1:
            fila.append(1)
        else:
            fila.append(0)
        fila.append(codcurso_dataporciclo[codcurso][ciclo][0])
        fila.append(codcurso_dataporciclo[codcurso][ciclo][1])
        allfilas.append(fila)
        fila = []
    if cantAbiertos < 2:
        continue

    allfilas.sort(key=lambda x: x[0])
    with open(filename, 'w', encoding='UTF8', newline='') as fa:
        writer = csv.writer(fa)
        writer.writerow(header)
        for fila in allfilas:
            writer.writerow(fila)
        cont += 1

    with open(metadata, 'a', encoding='UTF8', newline='') as fo:
        writer = csv.writer(fo)
        row = [codcurso, filename]
        writer.writerow(row)

print("TOTAL:", cont)


json_codcurso_nombrecurso = "codcurso_nombrecurso.json"
json_codcurso_departamento = "codcurso_departamento.json"


with open(json_codcurso_nombrecurso, "w", encoding='UTF8') as of:
    json.dump(codcurso_nombrecurso, of)

with open(json_codcurso_departamento, "w", encoding='UTF8') as of:
    json.dump(codcurso_departamento, of)
