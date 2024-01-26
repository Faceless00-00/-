import sys
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QMainWindow, QLabel, QApplication, QWidget, QLineEdit
from PyQt6.QtCore import Qt
import datetime
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUi()
    def f_forgot_pass (self):
        pass

    def serf_in_logins(self):
        pass

    def serf_in_admins(self):
        pass

    def f_enter(self):
        if self.serf_in_logins():
            with open('base_for_admins.txt', 'a', encoding="utf-8") as f:
                f.write(self.edit_login.text())
                f.write('/')
                f.write(str(datetime.datetime.now()))
                f.write('\n')
            self.new_window = TableWindow()
            self.new_window.show()
            window.close()
        elif self.serf_in_admins():
            with open('base_for_admins.txt', 'a', encoding="utf-8") as f:
                f.write(self.edit_login.text())
                f.write('/')
                f.write(str(datetime.datetime.now()))
                f.write('\n')
            self.new_window = Admin()
            self.new_window.show()
            window.close()
        else:
            dlg = Error()
            dlg.exec()

    def initUi(self):
        self.setWindowTitle("Авторизация")
        self.setFixedSize(300, 300)

        self.lable_login = QLabel('Введите ID')
        self.lable_login.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        #self.lable_login.setStyleSheet("QLabel {color:rgb(188, 188, 188)}") - Задание цвета для всех элеентов

        self.edit_login = QLineEdit()
        self.lable_password = QLabel('Введите пароль')
        self.lable_password.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.edit_password = QLineEdit()
        self.btn_forg_pass = QPushButton('Забыли пароль')
        self.btn_forg_pass.setFlat(True)

        self.btn_enter = QPushButton('Войти')

        self.layout_login = QVBoxLayout()
        self.layout_login.setContentsMargins(0,0,0,20)
        self.layout_password = QVBoxLayout()
        self.layout_password.setContentsMargins(0, 0, 0, 40)
        self.additional_btn = QHBoxLayout()
        self.additional_btn.setContentsMargins(10, 0, 0, 0)
        self.layout_enter = QVBoxLayout()
        self.layout_enter.setContentsMargins(0, 0, 0, 10)
        self.layout_all = QVBoxLayout()

        self.layout_login.addWidget(self.lable_login)
        self.layout_login.addWidget(self.edit_login)
        self.layout_password.addWidget(self.lable_password)
        self.layout_password.addWidget(self.edit_password)

        self.additional_btn.addWidget(self.btn_forg_pass)

        self.layout_enter.addWidget(self.btn_enter)

        self.layout_all.addLayout(self.layout_login)
        self.layout_all.addLayout(self.layout_password)
        self.layout_all.addLayout(self.layout_enter)
        self.layout_all.addLayout(self.additional_btn)

        self.widget = QWidget()
        self.widget.setLayout(self.layout_all)
        self.setCentralWidget(self.widget)

        self.btn_forg_pass.clicked.connect(self.f_forgot_pass)
        self.btn_enter.clicked.connect(self.f_enter)

    def center(self):
        qr = self.frameGeometry()  # Получаем прямоугольник, описывающий геометрию окна
        cp = QApplication.primaryScreen().availableGeometry().center()  # Получаем центр экрана
        qr.moveCenter(cp)  # Устанавливаем центр прямоугольника в центр экрана
        self.move(qr.topLeft())

if __name__ == '__main__':
    # Включаем возможность подключать команную строку
    app = QApplication(sys.argv)
    # window присваеваем виджет QMainWindow
    window = MainWindow()
    window.show()
    #Запускаем цикл событий
    sys.exit(app.exec())
    # экологическаЯ ситуация калининграда, монторинг на современные 2 года 2021-2023