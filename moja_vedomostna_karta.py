#pripoj knižnice
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import shuffle

class Question:
    def __init__(self, otazka1, spr_odp, wrong1, wrong2, wrong3):
        self.otazka1 = otazka1
        self.spr_odp = spr_odp
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question("Aký chemický prvok má protónové číslo 8?", "kyslík", "síra", "hélium", "železo"))
question_list.append(Question("Čo je najlepšia videohra na svete?", "Minecraft", "Roblox", "Fortnite", "FNAF"))
question_list.append(Question("Na akom hudobnom nástroji hrám?", "klavír", "gitara", "flauta", "saxofón"))
question_list.append(Question("Je toto ten najlepší kvíz na svete?", "áno", "nie", "možno", "určite nie"))







#vytvor aplikáciu a okno
app = QApplication([])

my_win = QWidget()
my_win.setWindowTitle('Vedomostna karta') # meni nadpis okna
otazka = QLabel('Ktorá z národností neexistuje?')

button = QPushButton('Vyhodnotiť')


# okno s odpovedami
moznosti = QGroupBox('Odpovede')

btn_answer1 = QRadioButton('Slovenská')
btn_answer2 = QRadioButton('Československá')
btn_answer3 = QRadioButton('Česká')
btn_answer4 = QRadioButton('Maďarská')

moznosti_group = QButtonGroup()
moznosti_group.addButton(btn_answer1)
moznosti_group.addButton(btn_answer2)
moznosti_group.addButton(btn_answer3)
moznosti_group.addButton(btn_answer4)



h_line = QHBoxLayout()
v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()

v_line1.addWidget(btn_answer1)
v_line1.addWidget(btn_answer3)
v_line2.addWidget(btn_answer2)
v_line2.addWidget(btn_answer4)

h_line.addLayout(v_line1)
h_line.addLayout(v_line2)

moznosti.setLayout(h_line)






# okno s vysledkami
vysledky_skup = QGroupBox("Výsledky")
vysledok = QLabel("Správne/Nesprávne")
spravna_odp = QLabel("Československá")

vysledok_v = QVBoxLayout()
vysledok_v.addWidget(vysledok, alignment=(Qt.AlignLeft | Qt.AlignTop))
vysledok_v.addWidget(spravna_odp, alignment=Qt.AlignHCenter, stretch = 2)

vysledky_skup.setLayout(vysledok_v)


# okno so skore
skore_skup = QGroupBox("Skóre")

body = QLabel("Body: 0")

percenta = QLabel("Percentá: 0.0 %")


score_layout_v = QVBoxLayout()
score_layout_v.addWidget(body, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
score_layout_v.addWidget(percenta, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

skore_skup.setLayout(score_layout_v)

# layouty
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()

h_line1.addWidget(otazka, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

h_line2.addWidget(moznosti)
h_line2.addWidget(vysledky_skup)
h_line2.addWidget(skore_skup)
vysledky_skup.hide()

h_line3.addStretch(1)
h_line3.addWidget(button, stretch = 2)
h_line3.addStretch(1)

v_line = QVBoxLayout()

v_line.addLayout(h_line1, stretch = 2)
v_line.addLayout(h_line2, stretch = 8)
v_line.addStretch(1)
v_line.addLayout(h_line3, stretch = 2)
v_line.addStretch(1)
v_line.setSpacing(5)

def show_result():
    moznosti.hide()
    vysledky_skup.show()
    button.setText("Ďalšia otázka")

def next_question():
    vysledky_skup.hide()
    moznosti.show()
    button.setText("Vyhodnotiť")

    moznosti_group.setExclusive(False)#prikaz, vdaka ktoremu vieme resetovat radio buttons
    btn_answer1.setChecked(False) #nastavuje, ci je button zaskrnuty
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    moznosti_group.setExclusive(True)#vdaka tomuto, vieme znovu zaznacit iba jeden radiobutton


answers = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]

def ask(q):
    shuffle(answers)
    answers[0].setText(q.spr_odp)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    otazka.setText(q.otazka1)
    spravna_odp.setText(q.spr_odp)
    next_question()

def show_spr_odp(result):
    vysledok.setText(result)
    show_result()

def check_ans():
    if answers[0].isChecked():
        show_spr_odp("Správne")
        my_win.score += 1
    else:
        show_spr_odp("Nesprávne")
    body.setText("Body:" + str(my_win.score))
    percenta.setText("Percentá: " + str(my_win.score/my_win.total*100) + "%")

def show_end():
    percenta_premm = my_win.score/my_win.total*100
    moznosti.hide()
    vysledky_skup.hide()
    otazka.hide()
    if percenta_premm == 100:
        body.setText("WOW 100%!")
        percenta.setText("Klobúk dole!")
    elif percenta_premm >= 50:
        body.setText("Máš viac ako polovicu!  (" + str(my_win.score) + "/5, " + str(percenta_premm) + "%)")
        percenta.setText("Gratulujem!")
    else:
        body.setText("Máš menej ako polovicu :(  (" + str(my_win.score) + "/5, " + str(percenta_premm) + "%)")
        percenta.setText("Nevadí")
    button.setText("Koniec")

def next_question1():
    my_win.cur_question = my_win.cur_question + 1
    if my_win.cur_question >= len(question_list):
        show_end()
    else:
        my_win.total += 1
        q = question_list[my_win.cur_question]
        ask(q)

my_win.cur_question = -1
my_win.score = 0
my_win.total = 1

def click_ok():
    if button.text() == "Vyhodnotiť":
        check_ans()
    elif button.text() == "Koniec":
        exit()
    else:
        next_question1()
q = Question("Aká je moja najobľúbenejšia farba?", "zelená", "modrá", "červená", "žltá")

ask(q)



button.clicked.connect(click_ok)

my_win.move(700, 400) # meni kde sa okno nachadza na obrazovke
my_win.resize(400, 200) # meni rozmery okna
#vytvor miniaplikácie hlavného okna


my_win.setLayout(v_line)
my_win.show() # bez tohto sa nám okno nezobrazí
app.exec_() # bez tohto sa naša appka ani nespustí

