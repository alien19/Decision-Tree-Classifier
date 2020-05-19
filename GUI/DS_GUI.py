import PyQt5
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
# from PyQt5 import QtChart
import os.path
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtCore import*
import sys
# import DS_DecisionTree
# from PyQt5.QtChart import*
# from serial import*

class Start_Window(QMainWindow):

    def __init__(DStart):
        super(Start_Window,DStart).__init__()
        DStart.left = 2 #position from left of screen
        DStart.top = 40 #position from top of screen
        DStart.title = 'Decision Tree Classifier'
        DStart.width = 2000 #width of window
        DStart.height = 1000 #height of window


        DStart.InitWindow()
        DStart.Design()
        DStart.setObjectNames()
        DStart.btnTrain.clicked.connect(DStart.onTrainClicked)

    def InitWindow(DStart):
        DStart.setWindowTitle(DStart.title)
        DStart.setAutoFillBackground(True)

        p = DStart.palette()
        p.setColor(DStart.backgroundRole(), Qt.white) #OR teleStart.setStyleSheet("background-color: white;")
        DStart.setPalette(p)

        DStart.mainWidget = QWidget()
        DStart.mainLayout = QHBoxLayout()

        DStart.lay1 = QVBoxLayout()
        DStart.layTrain = QHBoxLayout()
        DStart.lblDepth = QLabel("Decision Tree Maximum Depth")
        DStart.depthEdit  = QLineEdit()
        DStart.depthEdit.setPlaceholderText("maximum depth")
        DStart.btnTrain = QPushButton("Train Decision Tree")
        DStart.gBox1 = QGroupBox("Decision Tree Classifier")
        DStart.gBox1 .setAlignment(Qt.AlignCenter)

        DStart.lay2 = QVBoxLayout()
        DStart.gBox2 = QGroupBox("Decision Tree")
        DStart.gBox2 .setAlignment(Qt.AlignCenter)
        DStart.graph = QPixmap("example1_graph.png")
        DStart.lblGraph = QLabel()





    def Design(DStart):
        DStart.gBox1.setMaximumWidth(DStart.mainLayout.maximumSize[0]/2)
        DStart.mainLayout.addWidget(DStart.gBox1)
        DStart.mainLayout.addWidget(DStart.gBox2)
        DStart.gBox1.setLayout(DStart.lay1)

        DStart.lay1.addLayout(DStart.layTrain)
        DStart.layTrain.addWidget(DStart.lblDepth)
        DStart.layTrain.addWidget(DStart.depthEdit)
        DStart.layTrain.addWidget(DStart.btnTrain)

        DStart.gBox2.setLayout(DStart.lay2)
        DStart.lay2.addWidget(DStart.lblGraph)
        DStart.mainWidget.setLayout(DStart.mainLayout)
        DStart.setCentralWidget(DStart.mainWidget)

        # DStart.show()
    def setObjectNames(DStart):
        DStart.gBox1.setObjectName("TrainBox")


    @pyqtSlot()
    def onTrainClicked(DStart):
        # Call the decision_tree_algorithm train the model and draw the output graph
        DStart.lblGraph.setPixmap(DStart.graph)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    ex = Start_Window()
    ex.show()
    App.setStyleSheet("".join(open("style.css").readlines()))
    sys.exit(App.exec())
