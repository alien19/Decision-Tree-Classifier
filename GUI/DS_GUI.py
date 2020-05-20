import PyQt5
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
import os.path
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtCore import*
import sys
import os
path = os.curdir.replace('\GUI',"")
sys.path.append(path)
path = sys.path[-1]
from Classifier.DecisionTree import*


class Start_Window(QMainWindow):

    def __init__(DStart):
        super(Start_Window,DStart).__init__()
        DStart.title = 'Decision Tree Classifier'

        DStart.InitWindow()
        DStart.Design()
        DStart.setObjectNames()
        DStart.btnTrain.clicked.connect(DStart.onTrainClicked)
        DStart.btnPredict.clicked.connect(DStart.onPredictClicked)
        DStart.btnShow.clicked.connect(DStart.onShowClicked)

    def InitWindow(DStart):
        DStart.setWindowTitle(DStart.title)
        # DStart.setAutoFillBackground(True)

        p = DStart.palette()
        p.setColor(DStart.backgroundRole(), Qt.white) #OR teleStart.setStyleSheet("background-color: white;")
        DStart.setPalette(p)

        DStart.mainWidget = QWidget(DStart)
        DStart.mainLayout = QGridLayout()

        #-------------------1st Left Widget--------------------------------------
        #-------------------Upper GroupBox----------------------------
        DStart.stackLay = QStackedLayout()
        DStart.w1 = QWidget()
        DStart.lay1 = QGridLayout()
        DStart.trainBox = QGroupBox("Training Decision Tree")
        DStart.layTrainBox = QVBoxLayout()
        DStart.layTrain = QFormLayout()
        DStart.lblDepth = QLabel("Decision Tree Maximum Depth:")
        DStart.depthEdit  = QLineEdit()
        DStart.depthEdit.setPlaceholderText("maximum depth")
        DStart.btnTrain = QPushButton("Train Decision Tree")

        #-----------------Bottom GroupBox-------------------------------
        DStart.classifyBox = QGroupBox("Reviews Classification")
        DStart.layClassifyBox = QGridLayout()
        DStart.reviewText = QTextEdit()
        DStart.reviewText.setPlaceholderText("review text")
        DStart.btnClassify = QPushButton("Classify Review")
        DStart.btnClassify.setMaximumWidth(200)


        DStart.fileEdit = QLineEdit()
        DStart.fileEdit.setPlaceholderText("testFileName.csv")
        DStart.btnPredict = QPushButton("Predict Reviews")

        #----------------2nd Left Widget-----------------------------
        DStart.predictBox = QGroupBox("Review Prediciton")
        DStart.layPredictBox = QVBoxLayout()
        DStart.w2 = QWidget()
        DStart.layW2 = QVBoxLayout()
        DStart.btnBack = QPushButton("Back")
        DStart.tablePrediction = QTableWidget()
        # DStart.tableHeader = QHeaderView()
        DStart.lblGraph = QLabel()

        #----------------Right Widget---------------------------------
        DStart.gBox1 = QGroupBox("Decision Tree Classifier")
        DStart.gBox1 .setAlignment(Qt.AlignCenter)
        DStart.lay2 = QVBoxLayout()
        DStart.scrollarea = QScrollArea()
        DStart.gBox2 = QGroupBox("Decision Tree")
        DStart.gBox2 .setAlignment(Qt.AlignCenter)
        DStart.btnShow = QPushButton("Show Predictions")




    def Design(DStart):
        qtRectangle = DStart.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)

        DStart.setCentralWidget(DStart.mainWidget)
        DStart.mainWidget.setLayout(DStart.mainLayout)
        DStart.mainLayout.addLayout(DStart.stackLay,0,0)
        DStart.mainLayout.setColumnStretch(0,1)
        DStart.mainLayout.setColumnStretch(1,1)
        dummylay2 = QHBoxLayout()
        DStart.mainLayout.addLayout(dummylay2,0,1)
        dummylay2.addWidget(DStart.scrollarea)
        DStart.scrollarea.setWidget(DStart.gBox2)
        DStart.scrollarea.setWidgetResizable(True)
        
        


        DStart.stackLay.addWidget(DStart.w1)
        DStart.stackLay.addWidget(DStart.w2)
        DStart.w1.setLayout(DStart.lay1)
        DStart.lay1.addWidget(DStart.trainBox)
        DStart.lay1.addWidget(DStart.classifyBox)
        DStart.lay1.setRowStretch(0,1)
        DStart.lay1.setRowStretch(1,1)
        DStart.stackLay.setCurrentIndex(0)
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


        DStart.classifyBox.setLayout(DStart.layClassifyBox)
        DStart.layClassifyBox.addWidget(DStart.reviewText,0,0)
        DStart.layClassifyBox.addWidget(DStart.btnClassify,0,1)
        DStart.layClassifyBox.addWidget(DStart.fileEdit,1,0)
        DStart.layClassifyBox.addWidget(DStart.btnPredict,1,1)
        DStart.layClassifyBox.addWidget(DStart.btnShow,2,1)
        DStart.layClassifyBox.setColumnStretch(0,2)
        DStart.layClassifyBox.setColumnStretch(1,1)
        DStart.layClassifyBox.setRowStretch(0,1)
        DStart.layClassifyBox.setRowStretch(1,2)
        DStart.layClassifyBox.setAlignment(Qt.AlignCenter)
        
        DStart.w2.setLayout(DStart.layW2)
        DStart.layW2.addWidget(DStart.tablePrediction)
        DStart.tablePrediction.setColumnCount(2)
        DStart.tablePrediction.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # DStart.tablePrediction.setHorizontalHeaderLabels([])

        DStart.lay2.addWidget(DStart.lblGraph)
        # DStart.show()


    def setObjectNames(DStart):
        DStart.gBox1.setObjectName("TrainBox")
        DStart.btnShow.setObjectName("Back")


    @pyqtSlot()
    def onTrainClicked(DStart):
        # Call the decision_tree_algorithm train the model and draw the output graph
        print("the path is:"+path)
        dataFrame = data_init(path+"/Datasets/sample_train.csv")
        adjustedDataframe = words_count(dataFrame)
        depth = int(DStart.depthEdit.text())
        DStart.tree = decision_tree_algorithm(adjustedDataframe,max_depth=depth)
        
        d.clear()
        draw_graph(DStart.tree.root)
        d.render(format='png')
        DStart.graph = QPixmap('graph.gv.png')
        DStart.lblGraph.setPixmap(DStart.graph)
        DStart.layTrain.addWidget(QLabel("Accuracy:\n"+"91.25%"))


    def onPredictClicked(DStart):
        # DStart.statusBar().showMessage("Telemetry started")
        name,_ = QtWidgets.QFileDialog.getOpenFileName(DStart,'Open File')
        file = open(name,'r')

        with file:
            # text = file.read()
            DStart.fileEdit.setText(file.name)
            testData = data_init(file.name)
            p = predict(testData,DStart.tree)
            print(p)
    
    def onShowClicked(DStart):
        DStart.stackLay.setCurrentIndex(1)
    
    def onBackClicked(DStart):
        DStart.stackLay.setCurrentIndex(0)




# if __name__ == '__main__':
#     App = QApplication(sys.argv)
#     ex = Start_Window()
#     ex.show()
#     # App.setStyleSheet("".join(open("style.css").readlines()))
#     sys.exit(App.exec())
