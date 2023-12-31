from ML_SimpCdg import Colunas
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import tree
import matplotlib.pyplot as plt
def RFC(value,):
    print(value)
    alunos_df = pd.read_csv("1/alunos.csv")
    alunos_df = alunos_df[Colunas()].str.split(';',expand=True)
    alunos_df = pd.DataFrame(alunos_df)
    alunos_df.drop(alunos_df[alunos_df[36] == 'Enrolled'].index,inplace=True)
    alunos_df.ffill()
    X = alunos_df.drop(36,axis=1)
    alunos_df[36]=alunos_df[36].map({'Graduate':1,'Dropout':0})
    y = alunos_df[36]
    Xtre,Xtes,Ytre,Ytes = train_test_split(X,y,test_size=0.4,random_state=10)
    algrtm = RandomForestClassifier(min_samples_leaf=2,random_state=10,n_jobs=1)
    algrtm.fit(Xtre,Ytre)
    dicionario_df = dict()
    coluna = 0
    for c in value:
        dicionario_df[f'{coluna}'] = c
        coluna += 1
    print(dicionario_df)
    dt_pr = pd.DataFrame([dicionario_df])
    prev = algrtm.predict(dt_pr)
    return (prev)
