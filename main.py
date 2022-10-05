from math import sqrt, cos
from UI import *
import math
import csv
import sys

wl = 0
wr = 0


def functions():
    show_db()
    ui.calculate.clicked.connect(lambda: calculate_lengths())
    ui.save.clicked.connect(lambda: save())
    ui.load.clicked.connect(lambda: load())


def fill_check():
    if len(ui.s_left.text()) == 0 or ui.s_left.text() == "!!!":
        ui.s_left.setText("!!!")
    elif len(ui.s_rigth.text()) == 0 or ui.s_rigth.text() == "!!!":
        ui.s_rigth.setText("!!!")
    elif len(ui.d_left.text()) == 0 or ui.d_left.text() == "!!!":
        ui.d_left.setText("!!!")
    elif len(ui.d_rigth.text()) == 0 or ui.d_rigth.text() == "!!!":
        ui.d_rigth.setText("!!!")
    elif len(ui.A.text()) == 0 or ui.A.text() == "!!!":
        ui.A.setText("!!!")
    elif len(ui.B.text()) == 0 or ui.B.text() == "!!!":
        ui.B.setText("!!!")
    elif len(ui.ERD.text()) == 0 or ui.ERD.text() == "!!!":
        ui.ERD.setText("!!!")
    else:
        return True


def calculate_lengths():
    if fill_check():
        sl = float(ui.s_left.text())
        sr = float(ui.s_rigth.text())
        dl = float(ui.d_left.text())
        dr = float(ui.d_rigth.text())
        N = float(ui.N.currentText())
        K = float(ui.K.currentText())
        OLD = float(ui.OLD.currentText())
        ERD = float(ui.ERD.text())
        ro = float(ui.L_rim.text())
        f_off = float(ui.frame_offset.text())

        res = (((360 / (N / 2)) * K) * math.pi) / 180
        cos_calc = cos(res)

        if ui.Asymetrical.isChecked():
            ui.wl = (OLD / 2 - float(ui.A.text())) - ro - f_off
            ui.wr = (OLD / 2 - float(ui.B.text())) + ro + f_off
        else:
            ui.wl = (OLD / 2 - float(ui.A.text())) + ro - f_off
            ui.wr = (OLD / 2 - float(ui.B.text())) - ro + f_off

        left_calc = sqrt(pow(ERD / 2, 2) + pow(dl / 2, 2) - 2 * (ERD / 2) * (dl / 2) * cos_calc)
        length_left = sqrt(pow(ui.wl, 2) + pow(left_calc, 2)) - sl / 2 + float(ui.offset_left.text())
        ui.Left_side_length.setText(str(round(length_left, 2)))

        right_calc = sqrt(pow(ERD / 2, 2) + pow(dr / 2, 2) - 2 * (ERD / 2) * (dr / 2) * cos_calc)
        length_right = sqrt(pow(ui.wr, 2) + pow(right_calc, 2)) - sr / 2 + float(ui.offset_right.text())
        ui.Right_side_length.setText(str(round(length_right, 2)))


def save():
    if fill_check():
        if len(ui.save_name.text()) == 0 or ui.save_name.text() == "!!!":
            ui.ERD.setText("!!!")
        else:
            name = ui.save_name.text()
            data = [name, ui.s_left.text(), ui.s_rigth.text(), ui.d_left.text(), ui.d_rigth.text(), ui.N.currentText(),
                    ui.K.currentText(), ui.A.text(), ui.B.text(), ui.OLD.currentText(), ui.frame_offset.text(),
                    ui.offset_left.text(), ui.offset_right.text(), ui.ERD.text(), ui.L_rim.text()]
            with open('db.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=",")
                writer.writerow(data)


def load():
    pass


def show_db():
    ui.load_select.clear()
    with open('db.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for i in reader:
            ui.load_select.addItem(i[0])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    functions()
    sys.exit(app.exec_())
