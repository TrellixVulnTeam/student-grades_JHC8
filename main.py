import tensorflow
import keras
import pandas as pd
import numpy as np
import sklearn
from tkinter import *
from tkinter import messagebox
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit


class my_window(QMainWindow):
    def __init__(self):
        super(my_window, self).__init__()
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("Predict Grade")

        self.score_label = QtWidgets.QLabel(self)
        self.score_label.resize(150, 15)
        self.score_label.setText('Projected Score: ')
        self.score_label.move(50, 350)

        self.score_int = QtWidgets.QLabel(self)
        self.score_int.resize(150 , 15)
        self.score_int.move(175, 350)

        self.button = QtWidgets.QPushButton(self)
        self.button.move(100, 300)
        self.button.setText('Submit')
        self.button.clicked.connect(self.clicked)

        self.G1_label = QtWidgets.QLabel(self)
        self.G1_label.setText('Exam 1 (/15):')
        self.G1_label.move(50, 50)

        self.G1_text = QLineEdit(self)
        self.G1_text.move(155, 50)

        self.G2_label = QtWidgets.QLabel(self)
        self.G2_label.setText('Exam 2 (/15):')
        self.G2_label.move(50, 100)

        self.G2_text = QLineEdit(self)
        self.G2_text.move(155, 100)

        self.studytime_label = QtWidgets.QLabel(self)
        self.studytime_label.setText('Study Time:')
        self.studytime_label.move(50, 150)

        self.studytime_text = QLineEdit(self)
        self.studytime_text.move(155, 150)

        self.failures_label = QtWidgets.QLabel(self)
        self.failures_label.setText('# of Failures:')
        self.failures_label.move(50, 200)

        self.failures_text = QLineEdit(self)
        self.failures_text.move(155, 200)

        self.absences_label = QtWidgets.QLabel(self)
        self.absences_label.setText('# of Absences:')
        self.absences_label.move(50, 250)

        self.absences_text = QLineEdit(self)
        self.absences_text.move(155, 250)


    def clicked(self):

        self.val1 = int(self.G1_text.text())
        self.val2 = int(self.G2_text.text())
        self.val3 = int(self.studytime_text.text())
        self.val4 = int(self.failures_text.text())
        self.val5 = int(self.absences_text.text())
        self.play()

    def play(self):
        data = pd.read_csv("student-mat-new.csv", sep=";")

        data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

        predict = "G3"

        x = np.array(data.drop([predict], 1))
        y = np.array(data[predict])

        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)


        pickle_in = open("studentmodel.pickle", "rb")
        linear = pickle.load(pickle_in)

        # print('co: \n', linear.coef_)
        # print('intercept: \n', linear.intercept_)

        # val1 = input('G1: ')
        # val2 = input('G2: ')
        # val3 = input('studytime: ')
        # val4 = input('failures: ')
        # val5 = input('absences: ')

        # arr = np.array([[val1, val2, val3, val4, val5]])

        array = np.array([[self.val1, self.val2, self.val3, self.val4, self.val5]])
        # print(array)

        p = linear.predict(array)

        rounded_score = round(p[0])

        if rounded_score < 0:
            rounded_score = 0

        text = str(rounded_score) + '/15'
        self.score_int.setText(text)



def window():
    app = QApplication(sys.argv)
    win = my_window()


    win.show()
    sys.exit(app.exec_())

window()

def click():
    prediction.delete(1.0, END)
    entered_text=text_entry.get()
    prediction.insert(END, entered_text)

data = pd.read_csv("student-mat-new.csv", sep=";")

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G3"

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

'''
best = 0
for _ in range(10000000):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)


    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)

    acc = linear.score(x_test, y_test)
    print(_, acc)

    if acc > best:
        best = acc
        with open("studentmodel.pickle", "wb") as f:
            pickle.dump(linear, f)
'''

pickle_in = open("studentmodel.pickle", "rb")
linear = pickle.load(pickle_in)

# print('co: \n', linear.coef_)
# print('intercept: \n', linear.intercept_)

# val1 = input('G1: ')
# val2 = input('G2: ')
# val3 = input('studytime: ')
# val4 = input('failures: ')
# val5 = input('absences: ')

# arr = np.array([[val1, val2, val3, val4, val5]])

arr = np.array([[1, 2, 3, 4, 5]])
print(arr)

predictions = linear.predict(x_test)

window = Tk()
window.title("testtot;e")
window.configure(background='green')
# window.withdraw()
Label(window, text='mytext', bg='black', fg='white', font='none 12 bold') .grid(row=0, column=0, sticky=W)
text_entry = Entry(window, width=20, bg='white')
text_entry.grid(row=1, column=0, sticky=W)

Button(window, text='submit', width=6, command=click) .grid(row=2, column=0, sticky=W)

prediction = Text(window, width=75, height=6, wrap=WORD, background='white')
prediction.grid(row=4, column=0, columnspan=2, sticky=W)

# messagebox.showinfo("Prediction", "hellow")
# window.destroy()
window.mainloop()

# print(type(x_test))
# print(x_test)
# print(x_test[2])
# print(x_test[2][2])

print('prediction: ', predictions[0])

# for x in range(len(predictions)):
#     print('prediction: ', predictions[x], ' | x_test: ',  x_test[x], ' | y_test: ', y_test[x])

# p = 'absences'
# style.use("ggplot")
# pyplot.scatter(data[p], data['studytime'])
# pyplot.xlabel(p)
# pyplot.ylabel("Final grade")
# pyplot.show()