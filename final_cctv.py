from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtMultimedia import  QMediaPlayer
from PyQt5.QtWidgets import ( QHBoxLayout, QLabel,
        QPushButton, QSizePolicy, QSlider, QVBoxLayout)

from PyQt5.QtWidgets import  QListView, QFileSystemModel, QAbstractItemView, QGridLayout, QWidget
from PyQt5.QtCore import QDir, Qt
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaPlayer
import os


Fpath = os.path.dirname(os.path.abspath(__file__))
print(Fpath)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        
        MainWindow.setWindowFlag(Qt.FramelessWindowHint)
        MainWindow.setWindowOpacity(1)

        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(1200, 700)
        

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_background = QtWidgets.QFrame(self.frame)
        self.frame_background.setStyleSheet("QFrame{\n"
"background-color: rgb(0, 0, 0);\n"
"}")
        self.frame_background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_background.setObjectName("frame_background")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_background)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")


        ##########################################################
        ###Navigation bar (close , mini , maxi , logo ,..... )
        self.frame_nav = QtWidgets.QFrame(self.frame_background)
        self.frame_nav.setMinimumSize(QtCore.QSize(0, 75))
        self.frame_nav.setStyleSheet("QFrame{\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: #000000ff;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(53, 53, 79);\n"
"border-radius:20px;\n"
"}")
        
        self.frame_nav.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_nav.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_nav.setObjectName("frame_nav")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_nav)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_nav)
        self.label_2.setMinimumSize(QtCore.QSize(70, 70))
        self.label_2.setMaximumSize(QtCore.QSize(70, 70))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(QtGui.QPixmap(rf"{Fpath}\cctv-logo.svg")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.frame_nav)
        self.label.setStyleSheet("font:87 12pt \"Arialn Black\";\n"
"color:#58D68D ;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(257, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.bt_hide = QtWidgets.QPushButton(self.frame_nav)
        self.bt_hide.setMinimumSize(QtCore.QSize(70, 70))
        self.bt_hide.setStyleSheet("")
        self.bt_hide.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(rf"{Fpath}\minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_hide.setIcon(icon)
        self.bt_hide.setIconSize(QtCore.QSize(70, 70))
        self.bt_hide.setObjectName("bt_hide")
        self.horizontalLayout.addWidget(self.bt_hide)
        self.bt_mini = QtWidgets.QPushButton(self.frame_nav)
        self.bt_mini.setMinimumSize(QtCore.QSize(70, 70))
        self.bt_mini.setStyleSheet("")
        self.bt_mini.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(rf"{Fpath}\minimize-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_mini.setIcon(icon1)
        self.bt_mini.setIconSize(QtCore.QSize(70, 70))
        self.bt_mini.setObjectName("bt_mini")
        self.horizontalLayout.addWidget(self.bt_mini)
        self.bt_max = QtWidgets.QPushButton(self.frame_nav)
        self.bt_max.setMinimumSize(QtCore.QSize(70, 70))
        self.bt_max.setStyleSheet("")
        self.bt_max.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(rf"{Fpath}\maximize-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_max.setIcon(icon2)
        self.bt_max.setIconSize(QtCore.QSize(70, 70))
        self.bt_max.setObjectName("bt_max")
        self.horizontalLayout.addWidget(self.bt_max)
        self.bt_close = QtWidgets.QPushButton(self.frame_nav)
        self.bt_close.setMinimumSize(QtCore.QSize(70, 70))
        self.bt_close.setStyleSheet("")
        self.bt_close.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(rf"{Fpath}\close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_close.setIcon(icon3)
        self.bt_close.setIconSize(QtCore.QSize(70, 70))
        self.bt_close.setObjectName("bt_close")
        self.horizontalLayout.addWidget(self.bt_close)
        self.verticalLayout_3.addWidget(self.frame_nav)

        ################################################
        ###Create body of whole design
        self.frame_body = QtWidgets.QFrame(self.frame_background)
        self.frame_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_body.setObjectName("frame_body")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_body)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        ################################################
        ###Create left side bar contain (live , search , history) freeze
        self.frame_side = QtWidgets.QFrame(self.frame_body)
        self.frame_side.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_side.setMaximumSize(QtCore.QSize(200, 1080))
        self.frame_side.setStyleSheet("QFrame{\n"
"background-color:rgb(53, 53, 79);\n"
"}\n"
"\n"
"QPushButton{\n"
"font:87 12pt \"Arialn Black\";\n"
"background-color:#000000ff;\n"
"color:rgb(255, 255, 255); \n"
"border-radius:5px;\n"
"border:1px solid #58D68D;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:black;\n"
"}")
        self.frame_side.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_side.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_side.setObjectName("frame_side")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_side)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.bt_live = QtWidgets.QPushButton(self.frame_side)
        self.bt_live.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_live.sizePolicy().hasHeightForWidth())
        self.bt_live.setSizePolicy(sizePolicy)
        self.bt_live.setMinimumSize(QtCore.QSize(170, 100))
        self.bt_live.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(rf"{Fpath}\live(1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_live.setIcon(icon4)
        self.bt_live.setIconSize(QtCore.QSize(170, 100))
        self.bt_live.setCheckable(False)
        self.bt_live.setObjectName("bt_live")
        self.verticalLayout_4.addWidget(self.bt_live)
        self.bt_vechile_search = QtWidgets.QPushButton(self.frame_side)
        self.bt_vechile_search.setMinimumSize(QtCore.QSize(170, 100))
        self.bt_vechile_search.setIconSize(QtCore.QSize(50, 50))
        self.bt_vechile_search.setObjectName("bt_vechile_search")
        self.verticalLayout_4.addWidget(self.bt_vechile_search)
        self.bt_history = QtWidgets.QPushButton(self.frame_side)
        self.bt_history.setMinimumSize(QtCore.QSize(170, 100))
        self.bt_history.setObjectName("bt_history")
        self.verticalLayout_4.addWidget(self.bt_history)
        self.horizontalLayout_2.addWidget(self.frame_side)


        ####################################################
        ###Create Content of whole body
        self.frame_content = QtWidgets.QFrame(self.frame_body)
        self.frame_content.setStyleSheet("QFrame{\n"
"background-color:rgb(53, 53, 79);\n"
"}\n"
" ")
        self.frame_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_content)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        #####################################################
        ###Create stackedWidget for display content of whole project(page_live , page_vechile_search , page_history)
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_content)
        self.stackedWidget.setStyleSheet("QFrame{\n"
"background-color:rgb(39, 39, 58);\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_live = QtWidgets.QWidget()
        self.page_live.setObjectName("page_live")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.page_live)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.stream = QtWidgets.QFrame(self.page_live)
        self.stream.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stream.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stream.setObjectName("stream")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.stream)
        self.verticalLayout_2.setObjectName("verticalLayout_2")


        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.stream)
        self.stackedWidget_2.setObjectName("stackedWidget_2")


        ###################################
        ###Create cam1 page for live cam
        self.cam1 = QtWidgets.QWidget()
        self.cam1.setObjectName("cam1")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.cam1)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_cam1 = QtWidgets.QFrame(self.cam1)
        self.frame_cam1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cam1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cam1.setObjectName("frame_cam1")
        self.frame_cam1.setStyleSheet("QPushButton{\n"
"font:87 10pt \"black\";\n"
"background-color:#FFFFFF;\n"
"color:rgb(0, 0, 0); \n"
"border-radius:2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#DFF7D7;\n"
"}\n"
"\n"
"}")
        self.video_label = QLabel()
        self.video_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        self.video_label.setAlignment(Qt.AlignCenter)
        self.record_button = QPushButton('Record')
        self.record_button.setMinimumSize(100,120)
        self.stop_button = QPushButton('Stop')
        self.stop_button.setMinimumSize(100,120)
        self.stop_button.setEnabled(False)
        self.TM_label = QLabel()
        self.TM_label.setMaximumWidth(300)
        self.TM_label.setStyleSheet("color : #FFFFFF")
        vboxlayout_cam1 = QVBoxLayout()
        hboxlayout_cam1 = QHBoxLayout()
        hboxlayout_cam1.setContentsMargins(0,0,0,0)
        hboxlayout_cam1.addWidget(self.record_button)
        hboxlayout_cam1.addWidget(self.stop_button)
        hboxlayout_cam1.addWidget(self.TM_label)
        vboxlayout_cam1.addWidget(self.video_label)
        vboxlayout_cam1.addLayout(hboxlayout_cam1)
        self.frame_cam1.setLayout(vboxlayout_cam1)
        self.verticalLayout_11.addWidget(self.frame_cam1)
        self.stackedWidget_2.addWidget(self.cam1)

        
        #################################################
        ###Create view list page for video_test Usage 
        self.list_view_test = QtWidgets.QWidget()
        self.list_view_test.setObjectName("list_view_test")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.list_view_test)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_list_view_test = QtWidgets.QFrame(self.list_view_test)
        self.frame_list_view_test.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_list_view_test.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_list_view_test.setObjectName("frame_list_view_test")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_list_view_test)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_list_view_test.setStyleSheet("QPushButton{\n"
"font:87 12pt \"black\";\n"
"background-color:#FFFFFF;\n"
"color:rgb(0, 0, 0); \n"
"border-radius:2px;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:#FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#DFF7D7;\n"
"}\n"
"\n"

"QListView{\n"
"font:87 12pt;\n"
"color: #FFFFFF;\n"
"}\n"
"\n"

"QScrollBar:vertical{\n"
"border-top: 8px solid #ffffff;\n"
"border-bottom: 8px solid #ffffff;\n"
"border-left: 8px solid #ffffff;\n"
"border-right: 8px solid #ffffff;\n"
"background: rgb(231, 233, 234);\n"
"margin: 0px 0px 0px 0px;\n"
"width :22px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"stop: 0 rgb(138, 147, 155), stop: 0.5 rgb(138, 147, 155), stop:1 rgb(138, 147, 155));\n"
"min-height: 0px\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"stop: 0 rgb(138, 147, 155), stop: 0.5 rgb(138, 147, 155),  stop:1 rgb(138, 147, 155));\n"
"height: 0px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"stop: 0  rgb(138, 147, 155), stop: 0.5 rgb(138, 147, 155),  stop:1 rgb(138, 147, 155));\n"
"height: 0 px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
)
       
        self.list_vid_grid_layout = QGridLayout()
        self.list_vid_file_system_model = QFileSystemModel()
        self.list_vid_file_system_model.setRootPath(QDir.homePath())
        self.list_vid_file_system_model.setNameFilters(['*.mp4', '*.avi', '*.mkv'])      
        self.list_vid_list_view = QListView()
        self.list_vid_list_view.setModel(self.list_vid_file_system_model)
        self.list_vid_list_view.setRootIndex(self.list_vid_file_system_model.index(rf'{Fpath}\test_video'))
        self.list_vid_list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.list_vid_grid_layout.addWidget(self.list_vid_list_view, 0, 0)
        self.list_vid_widget_btlist = QWidget()
        self.list_vid_widget_btlist.setLayout(self.list_vid_grid_layout)
        self.verticalLayout_16.addWidget(self.list_vid_widget_btlist)
        self.verticalLayout_12.addWidget(self.frame_list_view_test)
        self.stackedWidget_2.addWidget(self.list_view_test)


        #################################################
        ###Create video player page for testvideo
        self.testvideo = QtWidgets.QWidget()
        self.testvideo.setObjectName("testvideo")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.testvideo)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_testvid = QtWidgets.QFrame(self.testvideo)
        self.frame_testvid.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_testvid.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_testvid.setObjectName("frame_testvid")
        self.frame_testvid.setStyleSheet("QPushButton{\n"
"font:87 10pt \"black\";\n"
"background-color:#FFFFFF;\n"
"color:rgb(0, 0, 0); \n"
"border-radius:2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#DFF7D7;\n"
"}\n"
"\n"
"}")

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoWidget = QVideoWidget()

        self.playBtn = QPushButton()
        self.playBtn.setMinimumSize(QtCore.QSize(100, 50))
        self.playBtn.setEnabled(False)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMaximumHeight(50)
    
        self.labelDuration = QLabel()
        self.labelDuration.setMaximumHeight(50)
        self.labelDuration.setStyleSheet("color : #FFFFFF")

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setContentsMargins(0,0,0,0)

        self.hboxLayout.addWidget(self.playBtn)
        self.hboxLayout.addWidget(self.slider)
        self.hboxLayout.addWidget(self.labelDuration)

        self.vboxLayout = QVBoxLayout()
        self.vboxLayout.addWidget(self.videoWidget)
        self.vboxLayout.addLayout(self.hboxLayout)

        self.frame_testvid.setLayout(self.vboxLayout)
        self.mediaPlayer.setVideoOutput(self.videoWidget)

        self.verticalLayout_14.addWidget(self.frame_testvid)
        self.stackedWidget_2.addWidget(self.testvideo)
        self.verticalLayout_2.addWidget(self.stackedWidget_2)
        self.horizontalLayout_4.addWidget(self.stream)


        ###################################################
        ###Create right side bar contain buttons of (cam1 , video test)
        self.cams = QtWidgets.QFrame(self.page_live)
        self.cams.setMaximumSize(QtCore.QSize(170, 16777215))
        self.cams.setStyleSheet("QPushButton{\n"
"font:87 12pt \"Black\";\n"
"background-color:#000000ff;\n"
"color:rgb(255, 255, 255); \n"
"border-radius:5px;\n"
"border:1px solid #58D68D;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:black;\n"
"}\n"
"")
        self.cams.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cams.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cams.setObjectName("cams")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.cams)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.cams)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_4 = QtWidgets.QPushButton(self.cams)
        self.pushButton_4.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.horizontalLayout_4.addWidget(self.cams)
        self.stackedWidget.addWidget(self.page_live)




        #####################################################
        ###Create page_vechile_search to add to stackedWidget
        self.page_vechile_search = QtWidgets.QWidget()
        self.page_vechile_search.setObjectName("page_vechile_search")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page_vechile_search)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_3 = QtWidgets.QFrame(self.page_vechile_search)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.frame_3)
        self.stackedWidget_3.setObjectName("stackedWidget_3")

        #####################################################
        ###Create page of view list of folders to add to main page_vechile_search
        self.page_btlist_folders = QtWidgets.QWidget()
        self.page_btlist_folders.setObjectName("page_btlist_folders")
        self.verticalLayout_btlist_folders = QtWidgets.QVBoxLayout(self.page_btlist_folders)
        self.verticalLayout_btlist_folders.setObjectName("verticalLayout_btlist_folders")
        self.frame_btlist_folders = QtWidgets.QFrame(self.page_btlist_folders)
        self.frame_btlist_folders.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_btlist_folders.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btlist_folders.setObjectName("frame_btlist_folders")
        self.verticalLayout_21_folders = QtWidgets.QVBoxLayout(self.frame_btlist_folders)
        self.verticalLayout_21_folders.setObjectName("verticalLayout_21_folders")
        self.frame_btlist_folders.setStyleSheet("QPushButton{\n"
"font:87 12pt \"black\";\n"
"background-color:#FFFFFF;\n"
"color:rgb(0, 0, 0); \n"
"border-radius:2px;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:#FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#DFF7D7;\n"
"}\n"
"\n"

"QListView{\n"
"font:87 12pt;\n"
"color: #FFFFFF;\n"
"}\n"
"\n"

"QScrollBar:vertical{\n"
"border-top: 8px solid #ffffff;\n"
"border-bottom: 8px solid #ffffff;\n"
"border-left: 8px solid #ffffff;\n"
"border-right: 8px solid #ffffff;\n"
"background: rgb(231, 233, 234);\n"
"margin: 0px 0px 0px 0px;\n"
"width :22px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"stop: 0 rgb(138, 147, 155), stop: 0.5 rgb(138, 147, 155), stop:1 rgb(138, 147, 155));\n"
"min-height: 0px\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"stop: 0 rgb(138, 147, 155), stop: 0.5 rgb(138, 147, 155),  stop:1 rgb(138, 147, 155));\n"
"height: 0px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"stop: 0  rgb(138, 147, 155), stop: 0.5 rgb(138, 147, 155),  stop:1 rgb(138, 147, 155));\n"
"height: 0 px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
)
        
        self.grid_layout_folders = QGridLayout()
        self.file_system_model_folders = QFileSystemModel()
        self.file_system_model_folders.setRootPath(QDir.homePath())
        #self.file_system_model_folders.setNameFilters(['*.mp4', '*.avi', '*.mkv'])

        self.list_view_folders = QListView()
        self.list_view_folders.setModel(self.file_system_model_folders)
        self.list_view_folders.setRootIndex(self.file_system_model_folders.index(rf'{Fpath}\videos'))
        self.list_view_folders.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.grid_layout_folders.addWidget(self.list_view_folders, 0, 0)
        self.widget_btlist_folders = QWidget()
        self.widget_btlist_folders.setLayout(self.grid_layout_folders)
        self.verticalLayout_21_folders.addWidget(self.widget_btlist_folders)
        self.verticalLayout_btlist_folders.addWidget(self.frame_btlist_folders)
        self.stackedWidget_3.addWidget(self.page_btlist_folders)



        #####################################################
        ###Create page of view list of video files to add to page_vechile_search
        self.page_btlist_s = QtWidgets.QWidget()
        self.page_btlist_s.setObjectName("page_btlist_s")
        self.verticalLayout_btlist = QtWidgets.QVBoxLayout(self.page_btlist_s)
        self.verticalLayout_btlist.setObjectName("verticalLayout_btlist")
        self.frame_btlist_s = QtWidgets.QFrame(self.page_btlist_s)
        self.frame_btlist_s.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_btlist_s.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btlist_s.setObjectName("frame_btlist_s")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_btlist_s)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.frame_btlist_s.setStyleSheet("QPushButton{\n"
"font:87 12pt \"black\";\n"
"background-color:#FFFFFF;\n"
"color:rgb(0, 0, 0); \n"
"border-radius:2px;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:#FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#DFF7D7;\n"
"}\n"
"\n"

"QListView{\n"
"font:87 12pt;\n"
"color: #FFFFFF;\n"
"}\n"
"\n"

"QScrollBar:vertical{\n"
"border-top: 8px solid #ffffff;\n"
"border-bottom: 8px solid #ffffff;\n"
"border-left: 8px solid #ffffff;\n"
"border-right: 8px solid #ffffff;\n"
"background: rgb(231, 233, 234);\n"
"margin: 0px 0px 0px 0px;\n"
"width :22px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"stop: 0 rgb(138, 147, 155), stop: 0.5 rgb(138, 147, 155), stop:1 rgb(138, 147, 155));\n"
"min-height: 0px\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"stop: 0 rgb(138, 147, 155), stop: 0.5 rgb(138, 147, 155),  stop:1 rgb(138, 147, 155));\n"
"height: 0px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"stop: 0  rgb(138, 147, 155), stop: 0.5 rgb(138, 147, 155),  stop:1 rgb(138, 147, 155));\n"
"height: 0 px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
)
        self.grid_layout = QGridLayout()
        self.list_view = QListView()
        self.grid_layout.addWidget(self.list_view, 0, 0)
        self.backbt_file =  QPushButton("Back To Folders")
        self.widget_btlist_s = QWidget()
        self.widget_btlist_s.setLayout(self.grid_layout)
        self.verticalLayout_21.addWidget(self.widget_btlist_s)
        self.verticalLayout_21.addWidget(self.backbt_file)
        self.verticalLayout_btlist.addWidget(self.frame_btlist_s)
        self.stackedWidget_3.addWidget(self.page_btlist_s)

        #####################################################
        ###Create page of video player to add to page_vechile_search
        self.page_vidp_p = QtWidgets.QWidget()
        self.page_vidp_p.setObjectName("page_vidp_p")
        self.verticalLayout_p = QtWidgets.QVBoxLayout(self.page_vidp_p)
        self.verticalLayout_p.setObjectName("verticalLayout_20")
        self.frame_vidp_p = QtWidgets.QFrame(self.page_vidp_p)
        self.frame_vidp_p.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_vidp_p.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_vidp_p.setObjectName("frame_vidp_p")
        self.frame_vidp_p.setStyleSheet("QPushButton{\n"
"font:87 10pt \"black\";\n"
"background-color:#FFFFFF;\n"
"color:rgb(0, 0, 0); \n"
"border-radius:2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#DFF7D7;\n"
"}\n"
"\n"

"QLabel{\n"
"font:87 10pt ;\n"
"color:#FFFFFF;\n"
"}\n"
"\n"
"QScrollBar:vertical{"
"border-top: 8px solid #ffffff;"
"border-bottom: 8px solid #ffffff;"
"border-left: 8px solid #ffffff;"
"border-right: 8px solid #ffffff;"
"background: rgb(231, 233, 234);"
"margin: 0px 0px 0px 0px;"
"width :22px;"
"}"
"QScrollBar::handle:vertical {"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
"stop: 0 rgb(138, 147, 155), stop: 0.5 rgb(138, 147, 155), stop:1 rgb(138, 147, 155));"
"min-height: 0px"
"}"
"QScrollBar::add-line:vertical {"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
"stop: 0 rgb(138, 147, 155), stop: 0.5 rgb(138, 147, 155),  stop:1 rgb(138, 147, 155));"
"height: 0px;"
"subcontrol-position: bottom;"
"subcontrol-origin: margin;"
"}"
"QScrollBar::sub-line:vertical {"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
"stop: 0  rgb(138, 147, 155), stop: 0.5 rgb(138, 147, 155),  stop:1 rgb(138, 147, 155));"
"height: 0 px;"
"subcontrol-position: top;"
"subcontrol-origin: margin;\n"
"}\n"
"\n")

        self.mediaPlayer_sp = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoWidget_sp = QVideoWidget()

        self.playBtn_sp = QPushButton()
        self.playBtn_sp.setMinimumSize(QtCore.QSize(100, 50))
        self.playBtn_sp.setEnabled(False)

        self.back_sp = QPushButton("Back")
        self.back_sp.setMinimumSize(QtCore.QSize(70, 50))
        self.back_sp.setEnabled(True)

        self.slider_sp = QSlider(Qt.Horizontal)
        self.slider_sp.setMaximumHeight(50)

        self.labelDuration_sp = QLabel()
        self.labelDuration_sp.setMaximumHeight(50)
        self.labelDuration_sp.setStyleSheet("color : #FFFFFF")
        
        self.hboxLayout_sp = QHBoxLayout()
        self.hboxLayout_sp.setContentsMargins(0,0,0,0)

        self.hboxLayout_sp1 = QHBoxLayout()
        self.hboxLayout_sp1.setContentsMargins(0,0,0,0)

        self.hboxLayout_sp.addWidget(self.playBtn_sp)
        self.hboxLayout_sp.addWidget(self.slider_sp)
        self.hboxLayout_sp.addWidget(self.labelDuration_sp)

        self.hboxLayout_sp1.addWidget(self.back_sp)

        self.vboxLayout_sp = QVBoxLayout()
        self.vboxLayout_sp.addWidget(self.videoWidget_sp)
        self.vboxLayout_sp.addLayout(self.hboxLayout_sp)
        self.vboxLayout_sp.addLayout(self.hboxLayout_sp1)

        self.frame_vidp_p.setLayout(self.vboxLayout_sp)

        self.mediaPlayer_sp.setVideoOutput(self.videoWidget_sp)
        self.verticalLayout_p.addWidget(self.frame_vidp_p)
        self.stackedWidget_3.addWidget(self.page_vidp_p)

        self.verticalLayout_19.addWidget(self.stackedWidget_3)
        self.horizontalLayout_5.addWidget(self.frame_3)


        #####################################################
        ###Create right side bar of search to add to page_vechile_search
        self.frame_2 = QtWidgets.QFrame(self.page_vechile_search)
        self.frame_2.setMaximumSize(QtCore.QSize(210, 16777215))
        self.frame_2.setStyleSheet("QPushButton{\n"
"font:87 12pt \"black\";\n"
"background-color:#FFFFFF;\n"
"color:rgb(0, 0, 0); \n"
"border-radius:2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#DFF7D7;\n"
"}\n"
"\n"
"QComboBox{\n"
"text-color:#000000;\n"
"background-color: rgb(231,233,234);\n"
"border-top: none;\n"
"border-left: none;\n"
"border-right: none;\n"
"border-bottom:1px solid rgb(138,147,155);\n"
"}\n"
"\n"

"QListView{\n"
"background-color: rgb(231,233,234);\n"
"}\n"
"\n"

"QDateEdit{\n"
"background-color:#FFFFFF;\n"
"text-color:#000000;\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"border-top: 8px solid #ffffff;\n"
"border-bottom: 8px solid #ffffff;\n"
"border-left: 8px solid #ffffff;\n"
"border-right: 8px solid #ffffff;\n"
"background: rgb(231, 233, 234);\n"
"margin: 0px 0px 0px 0px;\n"
"width :22px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"stop: 0 rgb(138, 147, 155), stop: 0.5 rgb(138, 147, 155), stop:1 rgb(138, 147, 155));\n"
"min-height: 0px\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"stop: 0 rgb(138, 147, 155), stop: 0.5 rgb(138, 147, 155),  stop:1 rgb(138, 147, 155));\n"
"height: 0px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"stop: 0  rgb(138, 147, 155), stop: 0.5 rgb(138, 147, 155),  stop:1 rgb(138, 147, 155));\n"
"height: 0 px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"QSpinBox{\n"
"background-color:#FFFFFF;\n"
"text-color:#000000;\n"
"}\n"
"\n"
"QTimeEdit{\n"
"background-color:#FFFFFF;\n"
"text-color:#000000;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setContentsMargins(-1, 10, -1, 7)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:#DFF7D7;;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5, 0, QtCore.Qt.AlignLeft)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setMinimumHeight(40)

        options = ['None','black','blue','brown','green','grey','orange','pink','purple','red','white','yellow']
                
        for option in options:
                self.comboBox_2.addItem(option)

        self.verticalLayout_6.addWidget(self.comboBox_2)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.setMinimumHeight(40)
        options = ['None' ,'Heavy-Duty', 'Lorry', 'Pickup', 'SUV', 'Sedan', 'Van']
                
        for option in options:
                self.comboBox_3.addItem(option)

        self.verticalLayout_6.addWidget(self.comboBox_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.Search = QtWidgets.QPushButton(self.frame_2)
        self.Search.setMinimumSize(QtCore.QSize(0, 30))
        self.Search.setObjectName("Search")
        self.verticalLayout_6.addWidget(self.Search)
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.horizontalLayout_5.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.page_vechile_search)
        

        #####################################################
        ###Create page_history to add to main stackedWidget
        self.page_history = QtWidgets.QWidget()
        self.page_history.setObjectName("page_history")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_history)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.stackedWidget_5 = QtWidgets.QStackedWidget(self.page_history)
        self.stackedWidget_5.setObjectName("stackedWidget_5")

        #####################################################
        ###Create page of list view of history to add to page_history
        self.page_btlist_his = QtWidgets.QWidget()
        self.page_btlist_his.setObjectName("page_btlist_his")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.page_btlist_his)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.page_btlist_his.setStyleSheet("QPushButton{\n"
"font:87 12pt \"black\";\n"
"background-color:#FFFFFF;\n"
"color:rgb(0, 0, 0); \n"
"border-radius:2px;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:#FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#DFF7D7;\n"
"}\n"
"\n"

"QListView{\n"
"font:87 12pt;\n"
"color: #FFFFFF;\n"
"}\n"
"\n"

"QScrollBar:vertical{\n"
"border-top: 8px solid #ffffff;\n"
"border-bottom: 8px solid #ffffff;\n"
"border-left: 8px solid #ffffff;\n"
"border-right: 8px solid #ffffff;\n"
"background: rgb(231, 233, 234);\n"
"margin: 0px 0px 0px 0px;\n"
"width :22px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"stop: 0 rgb(138, 147, 155), stop: 0.5 rgb(138, 147, 155), stop:1 rgb(138, 147, 155));\n"
"min-height: 0px\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"stop: 0 rgb(138, 147, 155), stop: 0.5 rgb(138, 147, 155),  stop:1 rgb(138, 147, 155));\n"
"height: 0px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"stop: 0  rgb(138, 147, 155), stop: 0.5 rgb(138, 147, 155),  stop:1 rgb(138, 147, 155));\n"
"height: 0 px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
)
        self.h_grid_layout = QGridLayout()
        self.h_file_system_model = QFileSystemModel()
        self.h_file_system_model.setRootPath(QDir.homePath())
        self.h_file_system_model.setNameFilters(['*.mp4', '*.avi', '*.mkv'])      

        self.h_list_view = QListView()
        self.h_list_view.setModel(self.h_file_system_model)
        self.h_list_view.setRootIndex(self.h_file_system_model.index(rf'{Fpath}\history'))
        self.h_list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.h_grid_layout.addWidget(self.h_list_view, 0, 0)

        self.h_widget_btlist = QWidget()
        self.h_widget_btlist.setLayout(self.h_grid_layout)
        
        self.verticalLayout_24.addWidget(self.h_widget_btlist)
        self.stackedWidget_5.addWidget(self.page_btlist_his)
        #self.stackedWidget_5.addWidget(self.page_btlist_his)

        #####################################################
        ###Create page of video player of history to add to page_history
        self.page_vidp_his = QtWidgets.QWidget()
        self.page_vidp_his.setObjectName("page_vidp_his")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.page_vidp_his)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.frame_vidp_his = QtWidgets.QFrame(self.page_vidp_p)
        self.frame_vidp_his.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_vidp_his.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_vidp_his.setObjectName("frame_vidp_his")
        self.frame_vidp_his.setStyleSheet("QPushButton{\n"
"font:87 10pt \"black\";\n"
"background-color:#FFFFFF;\n"
"color:rgb(0, 0, 0); \n"
"border-radius:2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#DFF7D7;\n"
"}\n"
"\n"

"QLabel{\n"
"font:87 10pt ;\n"
"color:#FFFFFF;\n"
"}\n"
"\n"
"QScrollBar:vertical{"
"border-top: 8px solid #ffffff;"
"border-bottom: 8px solid #ffffff;"
"border-left: 8px solid #ffffff;"
"border-right: 8px solid #ffffff;"
"background: rgb(231, 233, 234);"
"margin: 0px 0px 0px 0px;"
"width :22px;"
"}"
"QScrollBar::handle:vertical {"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
"stop: 0 rgb(138, 147, 155), stop: 0.5 rgb(138, 147, 155), stop:1 rgb(138, 147, 155));"
"min-height: 0px"
"}"
"QScrollBar::add-line:vertical {"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
"stop: 0 rgb(138, 147, 155), stop: 0.5 rgb(138, 147, 155),  stop:1 rgb(138, 147, 155));"
"height: 0px;"
"subcontrol-position: bottom;"
"subcontrol-origin: margin;"
"}"
"QScrollBar::sub-line:vertical {"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
"stop: 0  rgb(138, 147, 155), stop: 0.5 rgb(138, 147, 155),  stop:1 rgb(138, 147, 155));"
"height: 0 px;"
"subcontrol-position: top;"
"subcontrol-origin: margin;\n"
"}\n"
"\n")

        self.mediaPlayer_his = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoWidget_his = QVideoWidget()

        self.playBtn_his = QPushButton()
        self.playBtn_his.setMinimumSize(QtCore.QSize(100, 50))
        self.playBtn_his.setEnabled(False)

        self.back_his = QPushButton("Back")
        self.back_his.setMinimumSize(QtCore.QSize(70, 50))
        self.back_his.setEnabled(True)

        self.slider_his = QSlider(Qt.Horizontal)
        self.slider_his.setMaximumHeight(50)

        self.labelDuration_his = QLabel()
        self.labelDuration_his.setMaximumHeight(50)
        self.labelDuration_his.setStyleSheet("color : #FFFFFF")

        self.hboxLayout_his = QHBoxLayout()
        self.hboxLayout_his.setContentsMargins(0,0,0,0)

        self.hboxLayout_his1 = QHBoxLayout()
        self.hboxLayout_his1.setContentsMargins(0,0,0,0)

        self.hboxLayout_his.addWidget(self.playBtn_his)
        self.hboxLayout_his.addWidget(self.slider_his)
        self.hboxLayout_his.addWidget(self.labelDuration_his)

        self.hboxLayout_his1.addWidget(self.back_his)

        self.vboxLayout_his = QVBoxLayout()
        self.vboxLayout_his.addWidget(self.videoWidget_his)
        self.vboxLayout_his.addLayout(self.hboxLayout_his)
        self.vboxLayout_his.addLayout(self.hboxLayout_his1)

        self.frame_vidp_his.setLayout(self.vboxLayout_his)

        self.mediaPlayer_his.setVideoOutput(self.videoWidget_his)
        self.verticalLayout_25.addWidget(self.frame_vidp_his)
        
        self.stackedWidget_5.addWidget(self.page_vidp_his)
        self.verticalLayout_9.addWidget(self.stackedWidget_5)
        self.stackedWidget.addWidget(self.page_history)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_content)
        self.verticalLayout_3.addWidget(self.frame_body)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 8)
        self.horizontalLayout_3.addWidget(self.frame_background)
        self.verticalLayout_10.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

#function of renaming items
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "CCTV SYSTEM"))
        self.bt_vechile_search.setText(_translate("MainWindow", "Vehicle Search"))
        self.bt_history.setText(_translate("MainWindow", "History"))
        self.pushButton.setText(_translate("MainWindow", "CAM 1"))
        self.pushButton_4.setText(_translate("MainWindow", "TEST VIDEO"))
        self.label_4.setText(_translate("MainWindow", "Car Search"))
        self.label_5.setText(_translate("MainWindow", "Car Color"))
        self.label_3.setText(_translate("MainWindow", "Car Type"))
        self.Search.setText(_translate("MainWindow", "Search"))
       