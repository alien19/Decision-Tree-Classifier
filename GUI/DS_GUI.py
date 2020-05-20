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
sys.path.append('E:\Engineering courses\Data Structures\Project\Decision-Tree-Classifier')
path = sys.path[-1]
from Classifier.DS_DecisionTreeNotebook_Mariam import*


class Start_Window(QMainWindow):

    def __init__(DStart):
        super(Start_Window,DStart).__init__()
        # DStart.left = 2 #position from left of screen
        # DStart.top = 40 #position from top of screen
        DStart.title = 'Decision Tree Classifier'
        # DStart.width = 2000 #width of window
        # DStart.height = 1000 #height of window

        # DStart.setGeometry
        DStart.InitWindow()
        DStart.Design()
        DStart.setObjectNames()
        DStart.btnTrain.clicked.connect(DStart.onTrainClicked)
        DStart.btnPredict.clicked.connect(DStart.onPredictClicked)
    def InitWindow(DStart):
        DStart.setWindowTitle(DStart.title)
        # DStart.setAutoFillBackground(True)

        p = DStart.palette()
        p.setColor(DStart.backgroundRole(), Qt.white) #OR teleStart.setStyleSheet("background-color: white;")
        DStart.setPalette(p)

        DStart.mainWidget = QWidget(DStart)
        DStart.mainLayout = QHBoxLayout()

        DStart.lay1 = QStackedLayout()
        DStart.trainBox = QGroupBox("Decision Tree Classifier")
        DStart.layTrainBox = QVBoxLayout()
        DStart.layTrain = QFormLayout()

        DStart.predictBox = QGroupBox("Review Prediciton")
        DStart.lblDepth = QLabel("Decision Tree Maximum Depth")
        DStart.depthEdit  = QLineEdit()
        DStart.depthEdit.setPlaceholderText("maximum depth")
        DStart.btnTrain = QPushButton("Train Decision Tree")
        DStart.btnPredict = QPushButton("predict new example")
        DStart.fileEdit = QLineEdit()
        DStart.fileEdit.setPlaceholderText("testFileName.csv")
        DStart.gBox1 = QGroupBox("Decision Tree Classifier")
        DStart.gBox1 .setAlignment(Qt.AlignCenter)

        DStart.lay2 = QVBoxLayout()
        DStart.gBox2 = QGroupBox("Decision Tree")
        DStart.gBox2 .setAlignment(Qt.AlignCenter)

        DStart.lblGraph = QLabel()





    def Design(DStart):
        qtRectangle = DStart.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)

        # DStart.lay1.setGeometry((DStart.frameGeometry())/2)
        # DStart.lay2.setGeometry((DStart.frameGeometry())/2)
        DStart.setCentralWidget(DStart.mainWidget)
        DStart.mainWidget.setLayout(DStart.mainLayout)
        DStart.mainLayout.addLayout(DStart.lay1)
        DStart.mainLayout.addWidget(DStart.gBox2)

        DStart.lay1.addWidget(DStart.trainBox)
        DStart.lay1.addWidget(DStart.predictBox)
        DStart.lay1.setCurrentIndex(0)
        DStart.gBox2.setLayout(DStart.lay2)

        DStart.trainBox.setLayout(DStart.layTrainBox)
        DStart.layTrainBox.addLayout(DStart.layTrain)

        DStart.layTrain.addRow(DStart.lblDepth,DStart.depthEdit)

        dummyLay = QHBoxLayout()
        dummyLay.addWidget(DStart.btnTrain)
        dummyLay.setAlignment(Qt.AlignRight)
        DStart.layTrain.setAlignment(Qt.AlignCenter)
        DStart.layTrain.setFormAlignment(Qt.AlignCenter)
        DStart.layTrain.addRow(dummyLay)
        DStart.layTrain.addWidget(DStart.fileEdit)
        DStart.layTrain.addWidget(DStart.btnPredict)
        DStart.lay2.addWidget(DStart.lblGraph)
        # DStart.show()


    def setObjectNames(DStart):
        DStart.gBox1.setObjectName("TrainBox")


    @pyqtSlot()
    def onTrainClicked(DStart):
        # Call the decision_tree_algorithm train the model and draw the output graph
        dataFrame = data_init(path+"\Datasets\sample_train.csv")
        adjustedDataframe = words_count(dataFrame)
        tree = decision_tree_algorithm(adjustedDataframe,max_depth=DStart.depthEdit.text)

        draw_graph(tree)
        d.render(format='png')
        DStart.graph = QPixmap('graph.gv.png')
        print("Done")
        DStart.lblGraph.setPixmap(DStart.graph)


    def onPredictClicked(DStart):
        # DStart.statusBar().showMessage("Telemetry started")
        name,_ = QtWidgets.QFileDialog.getOpenFileName(DStart,'Open File')
        file = open(name,'r')

        with file:
            # text = file.read()
            DStart.fileEdit.setText(file.name)





if __name__ == '__main__':
    App = QApplication(sys.argv)
    ex = Start_Window()
    ex.show()
    App.setStyleSheet("".join(open("style.css").readlines()))
    sys.exit(App.exec())
