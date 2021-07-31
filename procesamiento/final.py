import csv
import json

final = "tablaFinal.csv"
archivoPrediccion = "prediccion2021_2.csv"
json_codcurso_nombrecurso = "codcurso_nombrecurso.json"
json_codcurso_departamento = "codcurso_departamento.json"
codcurso_nombrecurso = {}
codcurso_departamento = {}
with open(json_codcurso_nombrecurso, encoding='UTF8') as jf:
    codcurso_nombrecurso = json.load(jf)

with open(json_codcurso_departamento, encoding='UTF8') as jf:
    codcurso_departamento = json.load(jf)

csv_prediccion = []
with open(archivoPrediccion, encoding='UTF8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',',)
    header = True
    for row in csv_reader:
        if header:
            header = False
        else:
            codcurso = row[0]
            m_normal = int(row[1])
            r2_normal = float(row[2])
            m_nnls = int(row[3])
            r2_nnls = float(row[4])
            pred = 0
            r2 = 0
            if m_normal <= 0:
                pred = m_nnls
                r2 = r2_nnls
            else:
                if r2_nnls > r2_normal:
                    pred = m_nnls
                    r2 = r2_nnls
                else:
                    pred = m_normal
                    r2 = r2_normal
            csv_prediccion.append([codcurso, pred, r2])

id = 1
with open(final, 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(
        ['id', 'codcurso', 'nombrecurso', 'r2', 'area', 'prediccion', ])
    for row in csv_prediccion:
        fila = [id, row[0], codcurso_nombrecurso[row[0]], row[2],
                codcurso_departamento[row[0]], row[1], ]
        print(fila)
        writer.writerow(fila)
        id += 1
