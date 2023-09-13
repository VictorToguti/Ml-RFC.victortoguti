from flask import Flask,render_template,redirect
from flask.globals import request
import ML_Projeto120923
app = Flask(__name__)
app.config['SECRET_KEY'] =  'VOT120923'
"""Página principal(Home)"""
@app.route("/")
def Homepage():
    return render_template("homepage.html",)
"""Página de previsões"""
@app.route("/previsoes",methods=['POST'])
def Graficos():
    Estado_civil = request.form.get('estado-civil')
    Mododeap_curso = request.form.get('mdacurso')
    qual_mae = request.form.get('qualmae')
    qual_pai = request.form.get('qualpai')
    Nacionalidade = request.form.get('Nacionalidade')
    profissaomae = request.form.get('profissaomae')
    profissaopai = request.form.get('profissaopai')
    curso = request.form.get('curso')
    neducacao = request.form.get('neducacao')
    ordemapl = request.form.get('OrdemApl')
    idadedurantecurso = request.form.get('idadedurantecurso')
    nivelqualificacao = request.form.get('nivelqual')
    taxadeadmissao = request.form.get('taxadeadmissao')
    creditosprmrsem = request.form.get('creditosprmrsem')
    nmrmavaprmrsem = request.form.get('nmravaprmrsem')
    Enrolledprmrsem = request.form.get('enrolledprmrsem')
    nmruniprmrsem = request.form.get('nmruniprmrsem')
    notasprmrse = request.form.get('notasprmrsem')
    unisemprmrsem = request.form.get('unisemprmrsem')
    creditossegsem = request.form.get('creditossegsem')
    unienrolledsegsem = request.form.get('unienrolledsegsem')
    nmravasegsem = request.form.get('nmravasegsem')
    uniaprovsegsem = request.form.get('uniaprovsegsem')
    notassegsem = request.form.get('notassegsem')
    unisemsegsem = request.form.get('unisemsegsem')
    taxadedesaprovacao = request.form.get('taxadedesaprovacao')
    taxadeinflacao = request.form.get('taxadeinflacao')
    GDP = request.form.get('gdp')
    checkbox1 = request.form.get('checkbox1')
    if not checkbox1:
        checkbox1 = 0
    checkbox2 = request.form.get('checkbox2')
    if not checkbox2:
        checkbox2 = 0
    checkbox3 = request.form.get('checkbox3')
    if not checkbox3:
        checkbox3 = 0
    checkbox4 = request.form.get('checkbox4')
    if not checkbox4:
        checkbox4 = 0
    checkbox5 = request.form.get('checkbox5')
    if not checkbox5:
        checkbox5 = 0
    checkbox6 = request.form.get('checkbox6')
    if not checkbox6:
        checkbox6 = 0
    checkbox7 = request.form.get('checkbox7')
    if not checkbox7:
        checkbox7 = 0
    checkbox8 = request.form.get('checkbox8')
    if not checkbox8:
        checkbox8 = 0
    xtes = [Estado_civil,Mododeap_curso,ordemapl,curso,checkbox1,neducacao,nivelqualificacao,Nacionalidade,qual_mae,qual_pai,profissaomae,profissaopai,taxadeadmissao,checkbox2,checkbox3,checkbox4,checkbox5,checkbox7,checkbox6,idadedurantecurso,checkbox8,creditosprmrsem,Enrolledprmrsem,nmrmavaprmrsem,nmruniprmrsem,notasprmrse,unisemprmrsem,creditossegsem,unienrolledsegsem,nmravasegsem,uniaprovsegsem,notassegsem,unisemsegsem,taxadedesaprovacao,taxadeinflacao,GDP]
    prev = ML_Projeto120923.RFC(xtes)
    if prev == 1:
        prev = "Concluirá"
    else:
        prev = "Não Concluirá"
    return render_template("previsoes.html", prev = prev)
if __name__ == "__main__":
    app.run(debug=True)