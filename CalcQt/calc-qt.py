import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *

# Configuração do aplicativo e da janela
app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("CalcQT")
window.setFixedSize(215, 265)

# Funções
def mudar_texto_visor(texto):
    if texto == "0":
        if visor.text() != "0":
            text = [visor.text(), texto]
            visor.setText("".join(text))
    else:
        if visor.text() == "0":
            visor.setText(texto)
        else:
            text = [visor.text(), texto]
            visor.setText("".join(text))

def apagar():
    visor.setText("0")

def calcular_divisores():
    try:
        num = int(visor.text())

        if num < 0:
            QMessageBox.critical(
                window,
                "Erro",
                "Não existem divisores de números negativos."
            )
        elif num == 0:
            QMessageBox.critical(
                window,
                "Erro",
                "Divisores de zero são infinitos."
            )
        else:
            divisores = [str(i) for i in range(1, num + 1) if num % i == 0]
            visor.setText(", ".join(divisores) + ".")
    except ValueError:
        QMessageBox.critical(
            window,
            "Erro",
            "Você não digitou um número."
        )

# Componentes
visor = QLineEdit("0", window)
visor.setGeometry(5, 5, 205, 35)
visor.setAlignment(Qt.AlignRight)
visor.setStyleSheet("font-size: 14pt;")

btn1 = QPushButton("1", window)
btn1.setGeometry(5, 45, 65, 50)
btn1.clicked.connect(lambda: mudar_texto_visor("1"))

btn2 = QPushButton("2", window)
btn2.setGeometry(75, 45, 65, 50)
btn2.clicked.connect(lambda: mudar_texto_visor("2"))

btn3 = QPushButton("3", window)
btn3.setGeometry(145, 45, 65, 50)
btn3.clicked.connect(lambda: mudar_texto_visor("3"))

btn4 = QPushButton("4", window)
btn4.setGeometry(5, 100, 65, 50)
btn4.clicked.connect(lambda: mudar_texto_visor("4"))

btn5 = QPushButton("5", window)
btn5.setGeometry(75, 100, 65, 50)
btn5.clicked.connect(lambda: mudar_texto_visor("5"))

btn6 = QPushButton("6", window)
btn6.setGeometry(145, 100, 65, 50)
btn6.clicked.connect(lambda: mudar_texto_visor("6"))

btn7 = QPushButton("7", window)
btn7.setGeometry(5, 155, 65, 50)
btn7.clicked.connect(lambda: mudar_texto_visor("7"))

btn8 = QPushButton("8", window)
btn8.setGeometry(75, 155, 65, 50)
btn8.clicked.connect(lambda: mudar_texto_visor("8"))

btn9 = QPushButton("9", window)
btn9.setGeometry(145, 155, 65, 50)
btn9.clicked.connect(lambda: mudar_texto_visor("9"))

btn_apagar = QPushButton("Apagar", window)
btn_apagar.setGeometry(5, 210, 65, 50)
btn_apagar.clicked.connect(apagar)

btn0 = QPushButton("0", window)
btn0.setGeometry(75, 210, 65, 50)
btn0.clicked.connect(lambda: mudar_texto_visor("0"))

btn_igual = QPushButton("=", window)
btn_igual.setGeometry(145, 210, 65, 50)
btn_igual.clicked.connect(calcular_divisores)

# Configuração do encerramento
window.show()
sys.exit(app.exec_())
