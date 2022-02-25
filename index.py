from ast import Pass
from PyQt5 import uic,QtWidgets


def funcao_button():
 user = str(cadastro.lineEdit.text())
 email = str(cadastro.lineEdit_2.text())
 passw = cadastro.lineEdit_3.text()

 if(cadastro.radioButton.isChecked()):
    print("Mulher")
 elif cadastro.radioButton.isChecked():
    print("Homem")
 else: 
    print("Indefinido")

 print(f"{user}, {email}, {passw}")

app=QtWidgets.QApplication([])
cadastro=uic.loadUi("cadastro.ui")
cadastro.pushButton.clicked.connect(funcao_button)

cadastro.show()
app.exec()
