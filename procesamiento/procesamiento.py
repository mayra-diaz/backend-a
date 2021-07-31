import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
from scipy.optimize import nnls
import csv

metadata = 'metadata.csv'
prediccion = 'prediccion2021_2.csv'
file_reader = open(metadata, encoding='UTF8')
csv_reader = csv.reader(file_reader)
header = True

ciclo_numero = {'2012 - 1': 1, '2012 - 2': 2, '2013 - 0': 3, '2013 - 1': 4,
                '2013 - 2': 5, '2014 - 0': 6, '2014 - 1': 7,
                '2014 - 2': 8, '2015 - 0': 9, '2015 - 1': 10, '2015 - 2': 11, '2016 - 0': 12,
                '2016 - 1': 13, '2016 - 2': 14, '2017 - 0': 15,
                '2017 - 1': 16, '2017 - 2': 17, '2018 - 0': 18, '2018 - 1': 19, '2018 - 2': 20,
                '2019 - 0': 21, '2019 - 1': 22, '2019 - 2': 23,
                '2020 - 0': 24, '2020 - 1': 25, '2020 - 2': 26, '2021 - 0': 27, '2021 - 1': 28}
for row in csv_reader:
    if header:
        header = False
        with open(prediccion, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(
                ['codcurso', 'm_normal', 'r2_normal', 'm_nnls', 'r2_nnls'])
    else:
        df = pd.read_csv(row[1])
        prematriculados_siguiente_ciclo = df.iloc[-1].matriculados
        ciclo_prediccion = ciclo_numero['2021 - 1'] + 1
        esVerano = 0

        reg = linear_model.LinearRegression()
        reg.fit(df[['numeroCiclo', 'esVerano', 'prematriculados']],
                df.matriculados)
        aproximacion = reg.predict(
            df[['numeroCiclo', 'esVerano', 'prematriculados']])
        prediction = round(float(reg.predict(
            [[ciclo_prediccion, esVerano, prematriculados_siguiente_ciclo]])))
        r2 = round(r2_score(df[['matriculados']], aproximacion), 3)

        # non negative
        coef_nnls, rnorm = nnls(df[['numeroCiclo', 'esVerano', 'prematriculados']],
                                df.matriculados)
        c1 = np.array(pd.DataFrame(coef_nnls).iloc[0])
        c2 = np.array(pd.DataFrame(coef_nnls).iloc[1])
        c3 = np.array(pd.DataFrame(coef_nnls).iloc[2])
        aproximacion_nnls = np.array(c1*df[['numeroCiclo']]) + np.array(
            c2*df[['esVerano']])+np.array(c3*df[['prematriculados']])
        r2_nnls = round(r2_score(df[['matriculados']], aproximacion_nnls), 3)
        prediction_nnls = c1 * ciclo_prediccion + c2 * \
            esVerano+c3*prematriculados_siguiente_ciclo
        prediction_nnls = round(prediction_nnls[0])

        with open(prediccion, 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow([row[0], prediction, r2, prediction_nnls, r2_nnls])
