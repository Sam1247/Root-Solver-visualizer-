# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Result_2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogResultSeidel(object):
    def setupUi(self, DialogResultSeidel):
        DialogResultSeidel.setObjectName("DialogResultSeidel")
        DialogResultSeidel.resize(663, 537)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogResultSeidel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.treeResult = QtWidgets.QTreeWidget(DialogResultSeidel)
        self.treeResult.setObjectName("treeResult")
        self.treeResult.headerItem().setText(0, "1")
        self.horizontalLayout_3.addWidget(self.treeResult)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnShowGraph = QtWidgets.QPushButton(DialogResultSeidel)
        self.btnShowGraph.setObjectName("btnShowGraph")
        self.horizontalLayout.addWidget(self.btnShowGraph)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogResultSeidel)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogResultSeidel)
        self.buttonBox.accepted.connect(DialogResultSeidel.accept)
        self.buttonBox.rejected.connect(DialogResultSeidel.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogResultSeidel)

    def retranslateUi(self, DialogResultSeidel):
        _translate = QtCore.QCoreApplication.translate
        DialogResultSeidel.setWindowTitle(_translate("DialogResultSeidel", "Gauss Seidel Details"))
        self.btnShowGraph.setText(_translate("DialogResultSeidel", "Show Graph"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogResultSeidel = QtWidgets.QDialog()
    ui = Ui_DialogResultSeidel()
    ui.setupUi(DialogResultSeidel)
    DialogResultSeidel.show()
    sys.exit(app.exec_())

