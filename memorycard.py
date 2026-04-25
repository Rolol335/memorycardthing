from random import shuffle, randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QHBoxLayout, QVBoxLayout, 
    QGroupBox, QRadioButton,  
    QPushButton, QLabel,
    QButtonGroup
)

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
question_list = list()    
q1 = Question('Сколько раз этот код не работал?', 'хз','1','9','67')
q2 = Question('Как называется цело-численный тип данных?', 'int', 'num', 'число', 'list')
q3 = Question('Какой город является столицей Франции?', 'Париж','Москва','Удан-Удэ','Мухосранск')
q4 = Question('Как называется самая высокая гора в мире?', 'Эверест', 'Килиманджаро', 'Аконкагуа','не знаю')
#q5 = Question('')
question_list.append(q1)
question_list.append(q2)
question_list.append(q3)
question_list.append(q4)
app = QApplication([])
window = QWidget()
window.resize(400,300)
window.cur_question = -1
window.total = 0
window.score = 0
# Панель вопроса
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')

RadioGroupBox = QGroupBox("Варианты ответов")

rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
#группа кнопок-
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

# Панель результата
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
# RadioGroupBox.hide()
AnsGroupBox.hide()


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
def show_result():

    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def click_ok():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
def show_correct(result):
    lb_Result.setText(result)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        window.score += 1
        print('Количество заданных вопросов: ', window.total)
        print('Количество правильных ответов: ', window.score)
        print('Рейтинг:', window.score / window.total * 100)
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно')
def next_question():
    window.total += 1
    print('Количество заданных вопросов: ', window.total)
    print('Количество правильных ответов: ', window.score)
    cur_question = randint(0, len(question_list) - 1)
    #if window.cur_question >= len(question_list):
        #window.cur_question = 0
    q = question_list[cur_question]
    ask(q)


btn_OK.clicked.connect(click_ok)
next_question()
window.show()
app.exec_()