from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import serial
class Ui_Incubator(object):

    def __init__(self):
        self.flag = False
    def abnormalities_alarm(self, high: bool):
        self.label_5.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                   "text-align: center;")
        if high:
            self.label_5.setText("Danger : High Temperature")
        else:
            self.label_5.setText("Danger : Low Temperature")

    def jaundice_signal(self):

        if not self.flag:
            self.serial.write(b'1')  # Sending '1' as a signal
            self.flag = True
        else:
            self.serial.write(b'2')
            self.flag = False

    def update_data(self):
        self.serial = serial.Serial('COM3', 9600)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.read_data)
        self.timer.start(500)

    def read_data(self):
        if self.serial.in_waiting > 0:
            arduino_data = self.serial.readline().decode('ascii').rstrip()
            x, y, z = arduino_data.split(',')
            self.lcdNumber_3.display(float(x))
            self.lcdNumber.display(float(y))
            self.lcdNumber_2.display(float(z))

            if float(y) > 28:
                self.abnormalities_alarm(True)
            elif float(y) < 26:
                self.abnormalities_alarm(False)
            else:
                self.label_5.setStyleSheet("background-color: rgb(85, 170, 0);\n"
                                           "text-align: center;")
                self.label_5.setText("Stable Conditions")

    def setupUi(self, Incubator):
        Incubator.setObjectName("Incubator")
        Incubator.resize(945, 772)
        Incubator.setStyleSheet("background-color: #1e1e2f;")
        self.centralwidget = QtWidgets.QWidget(Incubator)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("color:white;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        font = QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.verticalLayout_2.addWidget(self.label_2)
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.setStyleSheet("border: 2px solid black; border-color: rgb(255,255,255);")
        self.verticalLayout_2.addWidget(self.lcdNumber)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        font = QFont()
        font.setBold(True)
        self.label_4.setFont(font)
        self.verticalLayout_2.addWidget(self.label_4)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_2.setStyleSheet("border: 2px solid black; border-color: rgb(255,255,255);")
        self.verticalLayout_2.addWidget(self.lcdNumber_2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        font = QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.verticalLayout_2.addWidget(self.label_3)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.lcdNumber_3.setStyleSheet("border: 2px solid black; border-color: rgb(255,255,255);")
        self.verticalLayout_2.addWidget(self.lcdNumber_3)
        self.pushButton = QtWidgets.QPushButton(self.frame, clicked = lambda: self.jaundice_signal())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(300, 0))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color: rgb(0,0,255);")
        font = QFont()
        font.setBold(True)
        self.pushButton.setFont(font)
        self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.label_5 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(0, 50))
        self.label_5.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"text-align: center;")
        self.label_5.setObjectName("label_5")
        self.label_5.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setBold(True)
        self.label_5.setFont(font)
        self.verticalLayout_3.addWidget(self.label_5)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        Incubator.setCentralWidget(self.centralwidget)

        self.retranslateUi(Incubator)
        QtCore.QMetaObject.connectSlotsByName(Incubator)

    def retranslateUi(self, Incubator):
        _translate = QtCore.QCoreApplication.translate
        Incubator.setWindowTitle(_translate("Incubator", "Incubator"))
        self.label_2.setText(_translate("Incubator", "Temperature"))
        self.label_4.setText(_translate("Incubator", "Heartbeats"))
        self.label_3.setText(_translate("Incubator", "Humidity"))
        self.pushButton.setText(_translate("Incubator", "Jaundice Lights"))
        self.label_5.setText(_translate("Incubator", "Stable Conditions"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Incubator = QtWidgets.QMainWindow()
    ui = Ui_Incubator()
    ui.setupUi(Incubator)
    Incubator.show()
    ui.update_data()
    sys.exit(app.exec_())
