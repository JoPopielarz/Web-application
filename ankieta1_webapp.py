from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import statistics

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///formdata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'True'

db = SQLAlchemy(app)

class Formdata(db.Model):
    __tablename__ = 'formdata'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    #plec = db.Column(db.Integer, nullable=False)
    plec = db.Column(db.String)
    wyksztalcenie = db.Column(db.Integer)
    wiek = db.Column(db.Integer)
    grupaw = db.Column(db.Integer)
    pytanie = db.Column(db.Integer)
    q1 = db.Column(db.Integer)
    q2 = db.Column(db.Integer)
    q3 = db.Column(db.Integer)
    q4 = db.Column(db.Integer)
    q5 = db.Column(db.Integer)
    q6 = db.Column(db.Integer)
    q7 = db.Column(db.Integer)
    q8 = db.Column(db.Integer)
    q9 = db.Column(db.Integer)
    q10 = db.Column(db.Integer)
    q11 = db.Column(db.Integer)
    q12 = db.Column(db.Integer)
    q13 = db.Column(db.Integer)
    q14 = db.Column(db.Integer)
    q15 = db.Column(db.Integer)
    q16 = db.Column(db.Integer)

    def __init__(self, plec, wyksztalcenie, wiek, grupaw, pytanie, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16):
        self.plec = plec
        self.wyksztalcenie = wyksztalcenie
        self.wiek = wiek
        self.grupaw = grupaw
        self.pytanie = pytanie
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5
        self.q6 = q6
        self.q7 = q7
        self.q8 = q8
        self.q9 = q9
        self.q10 = q10
        self.q11 = q11
        self.q12 = q12
        self.q13 = q13
        self.q14 = q14
        self.q15 = q15
        self.q16 = q16


db.create_all()


@app.route("/")
def welcome():
    return render_template('welcome.html')


@app.route("/form")
def show_form():
    return render_template('form.html')


@app.route("/raw")
def show_raw():
    fd = db.session.query(Formdata).all()
    return render_template('raw.html', formdata=fd)


@app.route("/result")
def show_result():
    fd_list = db.session.query(Formdata).all()

    # Some simple statistics for sample questions
    plec = []
    wyksztalcenie = []
    grupaw = []
    pytanie = []
    q1 = []
    q2 = []
    q3 = []
    q4 = []
    q5 = []
    q6 = []
    q7 = []
    q8 = []
    q9 = []
    q10 = []
    q11 = []
    q12 = []
    q13 = []
    q14 = []
    q15 = []
    q16 = []

    # wykres płeć
    women = 0
    men = 0
    for el in fd_list:
        plec.append(str(el.plec))
        if el.plec == 'kobieta':
            women += 1
        elif el.plec == 'mężczyzna':
            men += 1
    # Prepare data for google charts
    plec_data = [['Kobiety', women], ['Meżczyźni', men]]

    # wykres wykształcenie
    podstawowe = 0
    srednie = 0
    wyzsze = 0
    student = 0
    for el in fd_list:
        wyksztalcenie.append(str(el.wyksztalcenie))
        if el.wyksztalcenie == 'Podstawowe':
            podstawowe += 1
        elif el.wyksztalcenie == 'Średnie':
            srednie += 1
        elif el.wyksztalcenie == 'Wyższe':
            wyzsze += 1
        elif el.wyksztalcenie == 'Student':
            student += 1
    # Prepare data for google charts
    wyksztalcenie_data = [['Podstawowe', podstawowe], ['Średnie', srednie], ['Wyższe', wyzsze], ['Student', student]]

    # wykres grupa wiekowa
    licealisci = 0
    studenci = 0
    pracujacy = 0
    for el in fd_list:
        grupaw.append(str(el.grupaw))
        if el.grupaw == 'Licealiści':
            licealisci += 1
        elif el.grupaw == 'Studenci':
            studenci += 1
        elif el.grupaw == 'Pracujący (nie student)':
            pracujacy += 1
    # Prepare data for google charts
    grwiek_data = [['Licealiści', licealisci], ['Studenci', studenci], ['Pracujący (nie student)', pracujacy]]

    # wykres udzielania pomocy
    yes = 0
    no = 0
    for el in fd_list:
        pytanie.append(str(el.pytanie))
        if el.pytanie == 'Tak':
            yes += 1
        elif el.pytanie == 'Nie':
            no += 1
    # Prepare data for google charts
    pomoc_data = [['Tak', yes], ['Nie', no]]

    # wykres porównania odpowiedzi wg płci
    dobrze_k = 0
    dobrze_m = 0
    for el in fd_list:
        plec.append(str(el.plec))
        q1.append(int(el.q1))
        q2.append(int(el.q2))
        q3.append(int(el.q3))
        q4.append(int(el.q4))
        q5.append(int(el.q5))
        q6.append(int(el.q6))
        q7.append(int(el.q7))
        q8.append(int(el.q8))
        q9.append(int(el.q9))
        q10.append(int(el.q10))
        q11.append(int(el.q11))
        q12.append(int(el.q12))
        q13.append(int(el.q13))
        q14.append(int(el.q14))
        q15.append(int(el.q15))
        q16.append(int(el.q16))
        if el.plec == 'kobieta':
            if int(el.q1) == 3:
                dobrze_k = dobrze_k + 1
            if int(el.q2) == 3:
                dobrze_k = dobrze_k + 1
            if int(el.q3) == 2:
                dobrze_k = dobrze_k + 1
            if int(el.q4) == 1:
                dobrze_k = dobrze_k + 1
            if int(el.q5) == 3:
                dobrze_k = dobrze_k + 1
            if int(el.q6) == 3:
                dobrze_k = dobrze_k + 1
            if int(el.q7) == 1:
                dobrze_k = dobrze_k + 1
            if int(el.q8) == 4:
                dobrze_k = dobrze_k + 1
            if int(el.q9) == 1:
                dobrze_k = dobrze_k + 1
            if int(el.q10) == 3:
                dobrze_k = dobrze_k + 1
            if int(el.q11) == 2:
                dobrze_k = dobrze_k + 1
            if int(el.q12) == 1:
                dobrze_k = dobrze_k + 1
            if int(el.q13) == 1:
                dobrze_k = dobrze_k + 1
            if int(el.q14) == 1:
                dobrze_k = dobrze_k + 1
            if int(el.q15) == 3:
                dobrze_k = dobrze_k + 1
            if int(el.q16) == 3:
                dobrze_k = dobrze_k + 1
        else:
            if int(el.q1) == 3:
                dobrze_m = dobrze_m + 1
            if int(el.q2) == 3:
                dobrze_m = dobrze_m + 1
            if int(el.q3) == 2:
                dobrze_m = dobrze_m + 1
            if int(el.q4) == 1:
                dobrze_m = dobrze_m + 1
            if int(el.q5) == 3:
                dobrze_m = dobrze_m + 1
            if int(el.q6) == 3:
                dobrze_m = dobrze_m + 1
            if int(el.q7) == 1:
                dobrze_m = dobrze_m + 1
            if int(el.q8) == 4:
                dobrze_m = dobrze_m + 1
            if int(el.q9) == 1:
                dobrze_m = dobrze_m + 1
            if int(el.q10) == 3:
                dobrze_m = dobrze_m + 1
            if int(el.q11) == 2:
                dobrze_m = dobrze_m + 1
            if int(el.q12) == 1:
                dobrze_m = dobrze_m + 1
            if int(el.q13) == 1:
                dobrze_m = dobrze_m + 1
            if int(el.q14) == 1:
                dobrze_m = dobrze_m + 1
            if int(el.q15) == 3:
                dobrze_m = dobrze_m + 1
            if int(el.q16) == 3:
                dobrze_m = dobrze_m + 1
    if women != 0:
        dobrze_k = dobrze_k / women
    if men != 0:
        dobrze_m = dobrze_m / men
    # Prepare data for google charts
    por1_data = [['Kobiety', dobrze_k],
               ['Mężczyźni', dobrze_m]]

    # wykres porównania odpowiedzi wg wykształcenia
    dobrze_pod = 0
    dobrze_sr = 0
    dobrze_wyz = 0
    dobrze_stu = 0
    for el in fd_list:
        wyksztalcenie.append(str(el.wyksztalcenie))
        q1.append(int(el.q1))
        q2.append(int(el.q2))
        q3.append(int(el.q3))
        q4.append(int(el.q4))
        q5.append(int(el.q5))
        q6.append(int(el.q6))
        q7.append(int(el.q7))
        q8.append(int(el.q8))
        q9.append(int(el.q9))
        q10.append(int(el.q10))
        q11.append(int(el.q11))
        q12.append(int(el.q12))
        q13.append(int(el.q13))
        q14.append(int(el.q14))
        q15.append(int(el.q15))
        q16.append(int(el.q16))
        if el.wyksztalcenie == 'Podstawowe':
            if int(el.q1) == 3:
                dobrze_pod = dobrze_pod + 1
            if int(el.q2) == 3:
                dobrze_pod = dobrze_pod + 1
            if int(el.q3) == 2:
                dobrze_pod = dobrze_pod + 1
            if int(el.q4) == 1:
                dobrze_pod = dobrze_pod + 1
            if int(el.q5) == 3:
                dobrze_pod = dobrze_pod + 1
            if int(el.q6) == 3:
                dobrze_pod = dobrze_pod + 1
            if int(el.q7) == 1:
                dobrze_pod = dobrze_pod + 1
            if int(el.q8) == 4:
                dobrze_pod = dobrze_pod + 1
            if int(el.q9) == 1:
                dobrze_pod = dobrze_pod + 1
            if int(el.q10) == 3:
                dobrze_pod = dobrze_pod + 1
            if int(el.q11) == 2:
                dobrze_pod = dobrze_pod + 1
            if int(el.q12) == 1:
                dobrze_pod = dobrze_pod + 1
            if int(el.q13) == 1:
                dobrze_pod = dobrze_pod + 1
            if int(el.q14) == 1:
                dobrze_pod = dobrze_pod + 1
            if int(el.q15) == 3:
                dobrze_pod = dobrze_pod + 1
            if int(el.q16) == 3:
                dobrze_pod = dobrze_pod + 1
        elif el.wyksztalcenie == 'Średnie':
            if int(el.q1) == 3:
                dobrze_sr = dobrze_sr + 1
            if int(el.q2) == 3:
                dobrze_sr = dobrze_sr + 1
            if int(el.q3) == 2:
                dobrze_sr = dobrze_sr + 1
            if int(el.q4) == 1:
                dobrze_sr = dobrze_sr + 1
            if int(el.q5) == 3:
                dobrze_sr = dobrze_sr + 1
            if int(el.q6) == 3:
                dobrze_sr = dobrze_sr + 1
            if int(el.q7) == 1:
                dobrze_sr = dobrze_sr + 1
            if int(el.q8) == 4:
                dobrze_sr = dobrze_sr + 1
            if int(el.q9) == 1:
                dobrze_sr = dobrze_sr + 1
            if int(el.q10) == 3:
                dobrze_sr = dobrze_sr + 1
            if int(el.q11) == 2:
                dobrze_sr = dobrze_sr + 1
            if int(el.q12) == 1:
                dobrze_sr = dobrze_sr + 1
            if int(el.q13) == 1:
                dobrze_sr = dobrze_sr + 1
            if int(el.q14) == 1:
                dobrze_sr = dobrze_sr + 1
            if int(el.q15) == 3:
                dobrze_sr = dobrze_sr + 1
            if int(el.q16) == 3:
                dobrze_sr = dobrze_sr + 1
        elif el.wyksztalcenie == 'Wyższe':
            if int(el.q1) == 3:
                dobrze_wyz = dobrze_wyz + 1
            if int(el.q2) == 3:
                dobrze_wyz = dobrze_wyz + 1
            if int(el.q3) == 2:
                dobrze_wyz = dobrze_wyz + 1
            if int(el.q4) == 1:
                dobrze_wyz = dobrze_wyz + 1
            if int(el.q5) == 3:
                dobrze_wyz = dobrze_wyz + 1
            if int(el.q6) == 3:
                dobrze_wyz = dobrze_wyz + 1
            if int(el.q7) == 1:
                dobrze_wyz = dobrze_wyz + 1
            if int(el.q8) == 4:
                dobrze_wyz = dobrze_wyz + 1
            if int(el.q9) == 1:
                dobrze_wyz = dobrze_wyz + 1
            if int(el.q10) == 3:
                dobrze_wyz = dobrze_wyz + 1
            if int(el.q11) == 2:
                dobrze_wyz = dobrze_wyz + 1
            if int(el.q12) == 1:
                dobrze_wyz = dobrze_wyz + 1
            if int(el.q13) == 1:
                dobrze_wyz = dobrze_wyz + 1
            if int(el.q14) == 1:
                dobrze_wyz = dobrze_wyz + 1
            if int(el.q15) == 3:
                dobrze_wyz = dobrze_wyz + 1
            if int(el.q16) == 3:
                dobrze_wyz = dobrze_wyz + 1
        elif el.wyksztalcenie == 'Student':
            if int(el.q1) == 3:
                dobrze_stu = dobrze_stu + 1
            if int(el.q2) == 3:
                dobrze_stu = dobrze_stu + 1
            if int(el.q3) == 2:
                dobrze_stu = dobrze_stu + 1
            if int(el.q4) == 1:
                dobrze_stu = dobrze_stu + 1
            if int(el.q5) == 3:
                dobrze_stu = dobrze_stu + 1
            if int(el.q6) == 3:
                dobrze_stu = dobrze_stu + 1
            if int(el.q7) == 1:
                dobrze_stu = dobrze_stu + 1
            if int(el.q8) == 4:
                dobrze_stu = dobrze_stu + 1
            if int(el.q9) == 1:
                dobrze_stu = dobrze_stu + 1
            if int(el.q10) == 3:
                dobrze_stu = dobrze_stu + 1
            if int(el.q11) == 2:
                dobrze_stu = dobrze_stu + 1
            if int(el.q12) == 1:
                dobrze_stu = dobrze_stu + 1
            if int(el.q13) == 1:
                dobrze_stu = dobrze_stu + 1
            if int(el.q14) == 1:
                dobrze_stu = dobrze_stu + 1
            if int(el.q15) == 3:
                dobrze_stu = dobrze_stu + 1
            if int(el.q16) == 3:
                dobrze_stu = dobrze_stu + 1
    if podstawowe !=0:
        dobrze_pod = dobrze_pod / podstawowe
    if srednie != 0:
        dobrze_sr = dobrze_sr / srednie
    if wyzsze != 0:
        dobrze_wyz = dobrze_wyz / wyzsze
    if student != 0:
        dobrze_stu = dobrze_stu / student
    # Prepare data for google charts
    por2_data = [['Podstawowe', dobrze_pod],
                 ['Średnie', dobrze_sr],
                 ['Wyższe', dobrze_wyz],
                 ['Student', dobrze_stu]]

    # wykres porównania odpowiedzi wg grupy wiekowej
    dobrze_lic = 0
    dobrze_stud = 0
    dobrze_prac = 0
    for el in fd_list:
        grupaw.append(str(el.grupaw))
        q1.append(int(el.q1))
        q2.append(int(el.q2))
        q3.append(int(el.q3))
        q4.append(int(el.q4))
        q5.append(int(el.q5))
        q6.append(int(el.q6))
        q7.append(int(el.q7))
        q8.append(int(el.q8))
        q9.append(int(el.q9))
        q10.append(int(el.q10))
        q11.append(int(el.q11))
        q12.append(int(el.q12))
        q13.append(int(el.q13))
        q14.append(int(el.q14))
        q15.append(int(el.q15))
        q16.append(int(el.q16))
        if el.grupaw == 'Licealiści':
            if int(el.q1) == 3:
                dobrze_lic = dobrze_lic + 1
            if int(el.q2) == 3:
                dobrze_lic = dobrze_lic + 1
            if int(el.q3) == 2:
                dobrze_lic = dobrze_lic + 1
            if int(el.q4) == 1:
                dobrze_lic = dobrze_lic + 1
            if int(el.q5) == 3:
                dobrze_lic = dobrze_lic + 1
            if int(el.q6) == 3:
                dobrze_lic = dobrze_lic + 1
            if int(el.q7) == 1:
                dobrze_lic = dobrze_lic + 1
            if int(el.q8) == 4:
                dobrze_lic = dobrze_lic + 1
            if int(el.q9) == 1:
                dobrze_lic = dobrze_lic + 1
            if int(el.q10) == 3:
                dobrze_lic = dobrze_lic + 1
            if int(el.q11) == 2:
                dobrze_lic = dobrze_lic + 1
            if int(el.q12) == 1:
                dobrze_lic = dobrze_lic + 1
            if int(el.q13) == 1:
                dobrze_lic = dobrze_lic + 1
            if int(el.q14) == 1:
                dobrze_lic = dobrze_lic + 1
            if int(el.q15) == 3:
                dobrze_lic = dobrze_lic + 1
            if int(el.q16) == 3:
                dobrze_lic = dobrze_lic + 1
        elif el.grupaw == 'Studenci':
            if int(el.q1) == 3:
                dobrze_stud = dobrze_stud + 1
            if int(el.q2) == 3:
                dobrze_stud = dobrze_stud + 1
            if int(el.q3) == 2:
                dobrze_stud = dobrze_stud + 1
            if int(el.q4) == 1:
                dobrze_stud = dobrze_stud + 1
            if int(el.q5) == 3:
                dobrze_stud = dobrze_stud + 1
            if int(el.q6) == 3:
                dobrze_stud = dobrze_stud + 1
            if int(el.q7) == 1:
                dobrze_stud = dobrze_stud + 1
            if int(el.q8) == 4:
                dobrze_stud = dobrze_stud + 1
            if int(el.q9) == 1:
                dobrze_stud = dobrze_stud + 1
            if int(el.q10) == 3:
                dobrze_stud = dobrze_stud + 1
            if int(el.q11) == 2:
                dobrze_stud = dobrze_stud + 1
            if int(el.q12) == 1:
                dobrze_stud = dobrze_stud + 1
            if int(el.q13) == 1:
                dobrze_stud = dobrze_stud + 1
            if int(el.q14) == 1:
                dobrze_stud = dobrze_stud + 1
            if int(el.q15) == 3:
                dobrze_stud = dobrze_stud + 1
            if int(el.q16) == 3:
                dobrze_stud = dobrze_stud + 1
        elif el.grupaw == 'Pracujący (nie student)':
            if int(el.q1) == 3:
                dobrze_prac = dobrze_prac + 1
            if int(el.q2) == 3:
                dobrze_prac = dobrze_prac + 1
            if int(el.q3) == 2:
                dobrze_prac = dobrze_prac + 1
            if int(el.q4) == 1:
                dobrze_prac = dobrze_prac + 1
            if int(el.q5) == 3:
                dobrze_prac = dobrze_prac + 1
            if int(el.q6) == 3:
                dobrze_prac = dobrze_prac + 1
            if int(el.q7) == 1:
                dobrze_prac = dobrze_prac + 1
            if int(el.q8) == 4:
                dobrze_prac = dobrze_prac + 1
            if int(el.q9) == 1:
                dobrze_prac = dobrze_prac + 1
            if int(el.q10) == 3:
                dobrze_prac = dobrze_prac + 1
            if int(el.q11) == 2:
                dobrze_prac = dobrze_prac + 1
            if int(el.q12) == 1:
                dobrze_prac = dobrze_prac + 1
            if int(el.q13) == 1:
                dobrze_prac = dobrze_prac + 1
            if int(el.q14) == 1:
                dobrze_prac = dobrze_prac + 1
            if int(el.q15) == 3:
                dobrze_prac = dobrze_prac + 1
            if int(el.q16) == 3:
                dobrze_prac = dobrze_prac + 1
    if licealisci != 0:
        dobrze_lic = dobrze_sr / licealisci
    if studenci != 0:
        dobrze_stud = dobrze_stud / studenci
    if pracujacy != 0:
        dobrze_prac = dobrze_prac / pracujacy
    # Prepare data for google charts
    por3_data = [['Licealiści', dobrze_lic],
                 ['Studenci', dobrze_stud],
                 ['Pracujący (nie student)', dobrze_prac]]

    # wykres porównania odpowiedzi wg udzielenia pomocy
    dobrze_y = 0
    dobrze_n = 0
    for el in fd_list:
        pytanie.append(str(el.pytanie))
        q1.append(int(el.q1))
        q2.append(int(el.q2))
        q3.append(int(el.q3))
        q4.append(int(el.q4))
        q5.append(int(el.q5))
        q6.append(int(el.q6))
        q7.append(int(el.q7))
        q8.append(int(el.q8))
        q9.append(int(el.q9))
        q10.append(int(el.q10))
        q11.append(int(el.q11))
        q12.append(int(el.q12))
        q13.append(int(el.q13))
        q14.append(int(el.q14))
        q15.append(int(el.q15))
        q16.append(int(el.q16))
        if el.pytanie == 'Tak':
            if int(el.q1) == 3:
                dobrze_y = dobrze_y + 1
            if int(el.q2) == 3:
                dobrze_y = dobrze_y + 1
            if int(el.q3) == 2:
                dobrze_y = dobrze_y + 1
            if int(el.q4) == 1:
                dobrze_y = dobrze_y + 1
            if int(el.q5) == 3:
                dobrze_y = dobrze_y + 1
            if int(el.q6) == 3:
                dobrze_y = dobrze_y + 1
            if int(el.q7) == 1:
                dobrze_y = dobrze_y + 1
            if int(el.q8) == 4:
                dobrze_y = dobrze_y + 1
            if int(el.q9) == 1:
                dobrze_y = dobrze_y + 1
            if int(el.q10) == 3:
                dobrze_y = dobrze_y + 1
            if int(el.q11) == 2:
                dobrze_y = dobrze_y + 1
            if int(el.q12) == 1:
                dobrze_y = dobrze_y + 1
            if int(el.q13) == 1:
                dobrze_y = dobrze_y + 1
            if int(el.q14) == 1:
                dobrze_ = dobrze_y + 1
            if int(el.q15) == 3:
                dobrze_y = dobrze_y + 1
            if int(el.q16) == 3:
                dobrze_y = dobrze_y + 1
        else:
            if int(el.q1) == 3:
                dobrze_n = dobrze_n + 1
            if int(el.q2) == 3:
                dobrze_n = dobrze_n + 1
            if int(el.q3) == 2:
                dobrze_n = dobrze_n + 1
            if int(el.q4) == 1:
                dobrze_n = dobrze_n + 1
            if int(el.q5) == 3:
                dobrze_n = dobrze_n + 1
            if int(el.q6) == 3:
                dobrze_n = dobrze_n + 1
            if int(el.q7) == 1:
                dobrze_n = dobrze_n + 1
            if int(el.q8) == 4:
                dobrze_n = dobrze_n + 1
            if int(el.q9) == 1:
                dobrze_n = dobrze_n + 1
            if int(el.q10) == 3:
                dobrze_n = dobrze_n + 1
            if int(el.q11) == 2:
                dobrze_n = dobrze_n + 1
            if int(el.q12) == 1:
                dobrze_n = dobrze_n + 1
            if int(el.q13) == 1:
                dobrze_n = dobrze_n + 1
            if int(el.q14) == 1:
                dobrze_n = dobrze_n + 1
            if int(el.q15) == 3:
                dobrze_n = dobrze_n + 1
            if int(el.q16) == 3:
                dobrze_n = dobrze_n + 1
    if yes != 0:
        dobrze_y = dobrze_y / yes
    if no != 0:
        dobrze_n = dobrze_n / no
    # Prepare data for google charts
    por4_data = [['Tak', dobrze_y], ['Nie', dobrze_n]]

    # wykresy pytań
    q1_1 = 0
    q1_2 = 0
    q1_3 = 0
    q1_4 = 0
    for el in fd_list:
        q1.append(int(el.q1))
        if int(el.q1) == 1:
            q1_1 = q1_1 + 1
        elif int(el.q1) == 2:
            q1_2 = q1_2 + 1
        elif int(el.q1) == 3:
            q1_3 = q1_3 + 1
        elif int(el.q1) == 4:
            q1_4 = q1_4 + 1
    # Prepare data for google charts
    q1_data = [['997', q1_1],
               ['998', q1_2],
               ['999', q1_3],
               ['112', q1_4]]

    q2_1 = 0
    q2_2 = 0
    q2_3 = 0
    q2_4 = 0
    for el in fd_list:
        q2.append(int(el.q2))
        if int(el.q2) == 1:
            q2_1 = q2_1 + 1
        elif int(el.q2) == 2:
            q2_2 = q2_2 + 1
        elif int(el.q2) == 3:
            q2_3 = q2_3 + 1
        elif int(el.q2) == 4:
            q2_4 = q2_4 + 1
    # Prepare data for google charts
    q2_data = [['Udrożnić drogi oddechowe i sprawdzić oddech', q2_1],
               ['Ułożyć poszkodowanego w pozycji bocznej', q2_2],
               ['Zadbać o w bezpieczeństwo', q2_3],
               ['Wezwać pomoc', q2_4]]

    q3_1 = 0
    q3_2 = 0
    q3_3 = 0
    q3_4 = 0
    for el in fd_list:
        q3.append(int(el.q3))
        if int(el.q3) == 1:
            q3_1 = q3_1 + 1
        elif int(el.q3) == 2:
            q3_2 = q3_2 + 1
        elif int(el.q3) == 3:
            q3_3 = q3_3 + 1
        elif int(el.q3) == 4:
            q3_4 = q3_4 + 1
    # Prepare data for google charts
    q3_data = [['Pozostawić w pozycji zastanej,\n gdyż możemy zaburzyć jej częstotliwość oddechów.', q3_1],
               ['Ułożyć w pozycji bezpiecznej\n ustalonej na boku kontrolując oddech.', q3_2],
               ['Ułożyć na wznak i obserwować\n unoszenie się klatki piersiowej.', q3_3],
               ['Ułożyć w pozycji bezpiecznej\n ustalonej na plecach kontrolując oddech.', q3_4]]

    q4_1 = 0
    q4_2 = 0
    q4_3 = 0
    q4_4 = 0
    for el in fd_list:
        q4.append(int(el.q4))
        if int(el.q4) == 1:
            q4_1 = q4_1 + 1
        elif int(el.q4) == 2:
            q4_2 = q4_2 + 1
        elif int(el.q4) == 3:
            q4_3 = q4_3 + 1
        elif int(el.q4) == 4:
            q4_4 = q4_4 + 1
    # Prepare data for google charts
    q4_data = [['Uniesienie nóg oraz rąk do góry.', q4_1],
               ['Uniesienie rąk do góry.', q4_2],
               ['Ułożenie poszkodowanego w pozycji\n bocznej ustalonej na plecach.', q4_3],
               ['Ułożenie poszkodowanego w pozycji\n bocznej ustalonej na boku.', q4_4]]

    q5_1 = 0
    q5_2 = 0
    q5_3 = 0
    q5_4 = 0
    for el in fd_list:
        q5.append(int(el.q5))
        if int(el.q5) == 1:
            q5_1 = q5_1 + 1
        elif int(el.q5) == 2:
            q5_2 = q5_2 + 1
        elif int(el.q5) == 3:
            q5_3 = q5_3 + 1
        elif int(el.q5) == 4:
            q5_4 = q5_4 + 1
    # Prepare data for google charts
    q5_data = [['Szybko wkładam mu coś do buzi,\n by zabezpieczyć jego język przed odgryzieniem, staram się powstrzymać drgawki przytrzymując jego ręce i nogi.', q5_1],
               ['Układam poszkodowanego w pozycji\n bocznej bezpiecznej.', q5_2],
               ['Zabezpieczam głowę poszkodowanego,\n by zapobiec powstaniu urazów nie powstrzymuje drgawek.', q5_3],
               ['Zabezpieczam głowę poszkodowanego\n oraz powstrzymuje drgawki, aby zapobiec powstaniu urazów.', q5_4]]

    q6_1 = 0
    q6_2 = 0
    q6_3 = 0
    q6_4 = 0
    for el in fd_list:
        q6.append(int(el.q6))
        if int(el.q6) == 1:
            q6_1 = q6_1 + 1
        elif int(el.q6) == 2:
            q6_2 = q6_2 + 1
        elif int(el.q6) == 3:
            q6_3 = q6_3 + 1
        elif int(el.q6) == 4:
            q6_4 = q6_4 + 1
    # Prepare data for google charts
    q6_data = [['Akronim medyczny służący do segregowania poszkodowanych.', q6_1],
               ['Lek podawany w przypadku zawału.', q6_2],
               ['Automatyczny defibrylator zewnętrzny.', q6_3],
               ['Urządzenie służące do pomiaru tętna.', q6_4]]

    q7_1 = 0
    q7_2 = 0
    q7_3 = 0
    q7_4 = 0
    for el in fd_list:
        q7.append(int(el.q7))
        if int(el.q7) == 1:
            q7_1 = q7_1 + 1
        elif int(el.q7) == 2:
            q7_2 = q7_2 + 1
        elif int(el.q7) == 3:
            q7_3 = q7_3 + 1
        elif int(el.q7) == 4:
            q7_4 = q7_4 + 1
    # Prepare data for google charts
    q7_data = [['Zachęcić poszkodowanego do kaszlu,\n jeśli nie przynosi to oczekiwanego rezultatu wykonaj 5 uderzeń w okolicy między łopatkowej, jeśli wcześniej wykonane czynności nie pomogą zastosuj 5 uciśnięć nadbrzusza.', q7_1],
               ['Z całej siły uderz poszkodowanego\n w plecy, uderzenia wykonuj do momentu, gdy poszkodowany przestanie się krztusić lub straci przytomność.', q7_2],
               ['Z całej siły uciśnij nadbrzusze\n poszkodowanego, uciśnięcia wykonuj do momentu, gdy poszkodowany przestanie się krztusić lub straci przytomność.', q7_3],
               ['Jedynie wykonuje uderzenia w plecy\n do momentu, gdy poszkodowany przestanie się krztusić lub straci przytomność.', q7_4]]

    q8_1 = 0
    q8_2 = 0
    q8_3 = 0
    q8_4 = 0
    for el in fd_list:
        q8.append(int(el.q8))
        if int(el.q8) == 1:
            q8_1 = q8_1 + 1
        elif int(el.q8) == 2:
            q8_2 = q8_2 + 1
        elif int(el.q8) == 3:
            q8_3 = q8_3 + 1
        elif int(el.q8) == 4:
            q8_4 = q8_4 + 1
    # Prepare data for google charts
    q8_data = [['Każę pochylić głowę poszkodowanego\n do przodu, a na kark zastosuje zimny okład', q8_1],
               ['Każę pochylić głowę poszkodowanego\n do tyłu, na czole zastosuje zimny okład.', q8_2],
               ['Każę trzymać głowę poszkodowanego\n prosto i uciskać nos.', q8_3],
               ['Każę pochylić głowę poszkodowanego\n do przodu i uciskać nos.', q8_4]]

    q9_1 = 0
    q9_2 = 0
    q9_3 = 0
    q9_4 = 0
    for el in fd_list:
        q9.append(int(el.q9))
        if int(el.q9) == 1:
            q9_1 = q9_1 + 1
        elif int(el.q9) == 2:
            q9_2 = q9_2 + 1
        elif int(el.q9) == 3:
            q9_3 = q9_3 + 1
        elif int(el.q9) == 4:
            q9_4 = q9_4 + 1
    # Prepare data for google charts
    q9_data = [['Odchylić głowę poszkodowanego,\n nachylić się nad poszkodowanym i obserwując ruch klatki liczyć ilość oddechów i wsłuchiwać się w oddech poszkodowanego przez 10 sekund.', q9_1],
               ['Do ust poszkodowanego przyłożyć lusterko\n czekać na pojawienie się pary na lusterku około 20 sekund.', q9_2],
               ['Nachylić się nad poszkodowanym\n i obserwując ruch klatki liczyć ilość oddechów i wsłuchiwać się w oddech poszkodowanego przez 15 sekund.', q9_3],
               ['Odchylić głowę poszkodowanego,\n nachylić się nad poszkodowanym oraz liczyć ilość oddechów przez 25 sekund.', q9_4]]

    q10_1 = 0
    q10_2 = 0
    q10_3 = 0
    q10_4 = 0
    for el in fd_list:
        q10.append(int(el.q10))
        if int(el.q10) == 1:
            q10_1 = q10_1 + 1
        elif int(el.q10) == 2:
            q10_2 = q10_2 + 1
        elif int(el.q10) == 3:
            q10_3 = q10_3 + 1
        elif int(el.q10) == 4:
            q10_4 = q10_4 + 1
    # Prepare data for google charts
    q10_data = [['2:15', q10_1],
                ['15:2', q10_2],
                ['30:2', q10_3],
                ['2:30', q10_4]]

    q11_1 = 0
    q11_2 = 0
    q11_3 = 0
    q11_4 = 0
    for el in fd_list:
        q11.append(int(el.q11))
        if int(el.q11) == 1:
            q11_1 = q11_1 + 1
        elif int(el.q11) == 2:
            q11_2 = q11_2 + 1
        elif int(el.q11) == 3:
            q11_3 = q11_3 + 1
        elif int(el.q11) == 4:
            q11_4 = q11_4 + 1
    # Prepare data for google charts
    q11_data = [['200-300 uciśnięć na minutę oraz głębokość 2-3 cm', q11_1],
                ['100-120 uciśnięć na minutę oraz głębokość 5-6 cm', q11_2],
                ['90-80 uciśnięć na minutę oraz głębokość 6-10cm', q11_3],
                ['80-70 uciśnięć na minutę oraz głębokość 4-7 cm', q11_4]]

    q12_1 = 0
    q12_2 = 0
    q12_3 = 0
    q12_4 = 0
    for el in fd_list:
        q12.append(int(el.q12))
        if int(el.q12) == 1:
            q12_1 = q12_1 + 1
        elif int(el.q12) == 2:
            q12_2 = q12_2 + 1
        elif int(el.q12) == 3:
            q12_3 = q12_3 + 1
        elif int(el.q12) == 4:
            q12_4 = q12_4 + 1
    # Prepare data for google charts
    q12_data = [['Schładzamy miejsce oparzenia zimną\n bieżącą wodą przez około 20 min.', q12_1],
                ['Przykładamy do miejsca oparzenia lód.', q12_2],
                ['Polewamy miejsce oparzenia wodą utlenioną.', q12_3],
                ['Schładzamy oparzenie do momentu,\n gdy poszkodowany przestanie odczuwać ból.', q12_4]]

    q13_1 = 0
    q13_2 = 0
    q13_3 = 0
    q13_4 = 0
    for el in fd_list:
        q13.append(int(el.q13))
        if int(el.q13) == 1:
            q13_1 = q13_1 + 1
        elif int(el.q13) == 2:
            q13_2 = q13_2 + 1
        elif int(el.q13) == 3:
            q13_3 = q13_3 + 1
        elif int(el.q13) == 4:
            q13_4 = q13_4 + 1
    # Prepare data for google charts
    q13_data = [['Zaburzenie widzenia i mowy,\n asymetria twarzy, osłabnięcie kończyny po jednej stronie.', q13_1],
                ['Bladość skóry, zimne poty, spowolniony oddech.', q13_2],
                ['Wysoka temperatura ciała,\n przyspieszony oddech, biegunka.', q13_3],
                ['Ściskający ból w okolicy mostka.', q13_4]]

    q14_1 = 0
    q14_2 = 0
    q14_3 = 0
    q14_4 = 0
    for el in fd_list:
        q14.append(int(el.q14))
        if int(el.q14) == 1:
            q14_1 = q14_1 + 1
        elif int(el.q14) == 2:
            q14_2 = q14_2 + 1
        elif int(el.q14) == 3:
            q14_3 = q14_3 + 1
        elif int(el.q14) == 4:
            q14_4 = q14_4 + 1
    # Prepare data for google charts
    q14_data = [['Ściskający ból w okolicy mostka.', q14_1],
                ['Bladość skóry, zimne poty,\n przyspieszony oddech.', q14_2],
                ['Wysoka temperatura ciała,\n przyspieszony oddech, biegunka.', q14_3],
                ['Zaburzenie widzenia, mowy i\n osłabnięcie kończyny po jednej stronie.', q14_4]]

    q15_1 = 0
    q15_2 = 0
    q15_3 = 0
    q15_4 = 0
    for el in fd_list:
        q15.append(int(el.q15))
        if int(el.q15) == 1:
            q15_1 = q15_1 + 1
        elif int(el.q5) == 2:
            q15_2 = q15_2 + 1
        elif int(el.q15) == 3:
            q15_3 = q15_3 + 1
        elif int(el.q15) == 4:
            q15_4 = q15_4 + 1
    # Prepare data for google charts
    q15_data = [['Nastawić kości w osi kończyny.', q15_1],
                ['Obandażować kończynę w celu zmniejszenia obrzęku.', q15_2],
                ['Unieruchomić w zastanej pozycji.', q15_3],
                ['Podać doustnie lek przeciwbólowy o silnym działaniu.', q15_4]]

    q16_1 = 0
    q16_2 = 0
    q16_3 = 0
    q16_4 = 0
    for el in fd_list:
        q16.append(int(el.q16))
        if int(el.q16) == 1:
            q16_1 = q16_1 + 1
        elif int(el.q16) == 2:
            q16_2 = q16_2 + 1
        elif int(el.q16) == 3:
            q16_3 = q16_3 + 1
        elif int(el.q16) == 4:
            q16_4 = q16_4 + 1
    # Prepare data for google charts
    q16_data = [['Opuścić kończynę wzdłuż ciała.', q16_1],
                ['Powyżej krwawienia założyć opaskę uciskową.', q16_2],
                ['Zastosować opatrunek uciskowy.', q16_3],
                ['Nałożyć na ranę jałową gazę.', q16_4]]

    return render_template('result.html', plec_data=plec_data, wyksztalcenie_data=wyksztalcenie_data, grwiek_data=grwiek_data,
                           pomoc_data=pomoc_data, por1_data=por1_data, por2_data=por2_data, por3_data=por3_data, por4_data=por4_data,
                           q1_data=q1_data, q2_data=q2_data, q3_data=q3_data, q4_data=q4_data, q5_data=q5_data,
                           q6_data=q6_data, q7_data=q7_data, q8_data=q8_data, q9_data=q9_data, q10_data=q10_data, q11_data=q11_data,
                           q12_data=q12_data, q13_data=q13_data, q14_data=q14_data, q15_data=q15_data, q16_data=q16_data)


@app.route("/save", methods=['POST'])
def save():
    # Get data from FORM
    plec = request.form['plec']
    wyksztalcenie = request.form['wyksztalcenie']
    wiek = request.form['wiek']
    grupaw = request.form['grupaw']
    pytanie = request.form['pytanie']
    q1 = request.form['q1']
    q2 = request.form['q2']
    q3 = request.form['q3']
    q4 = request.form['q4']
    q5 = request.form['q5']
    q6 = request.form['q6']
    q7 = request.form['q7']
    q8 = request.form['q8']
    q9 = request.form['q9']
    q10 = request.form['q10']
    q11 = request.form['q11']
    q12 = request.form['q12']
    q13 = request.form['q13']
    q14 = request.form['q14']
    q15 = request.form['q15']
    q16 = request.form['q16']


    # Save the data
    fd = Formdata(plec, wyksztalcenie, wiek, grupaw, pytanie, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16)
    db.session.add(fd)
    db.session.commit()

    return redirect('/result')
@app.route("/group")
def show_group():
    return render_template('group.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
