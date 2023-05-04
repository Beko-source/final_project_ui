from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5 import Qt
from PySide2.QtCore import QObject
import final_cctv
import sys
import numpy as np
from ui_cctv_2 import *
from PyQt5 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import Vplayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5 import QtCore, QtWidgets, QtMultimedia
from tkinter import filedialog
from PyQt5.QtCore import QDir, Qt, QUrl
import sys
import cv2
import datetime
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QVBoxLayout , QHBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer, QDateTime
import ffmpegcv
import time
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt


Vpath = r"C:\Users\Bebo\Desktop\final_project\icons"

current_time = QDateTime.currentDateTime().toString('yyyy-MM-dd  hh-mm-ss')
video_file = rf"C:\Users\Bebo\Desktop\final_project\icons\videos\{current_time}.mp4"
class MiApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = final_cctv.Ui_MainWindow() 
        self.ui.setupUi(self)


        self.duration = 0
        self.duration_list = 0
    

        #conrol MainWindow
        self.ui.bt_hide.clicked.connect(self.control_bt_hide)
        self.ui.bt_mini.clicked.connect(self.control_bt_mini)
        self.ui.bt_max.clicked.connect(self.control_bt_max)
        self.ui.bt_close.clicked.connect(self.control_bt_close)

        #control window resize
        x = self.ui.gripSize = 100
        self.ui.grip = QtWidgets.QSizeGrip(self)
        self.ui.grip.resize(x , x)

        #control window move
        self.ui.frame_nav.mouseMoveEvent = self.mover_window

        #control main menu
        self.ui.bt_live.clicked.connect(self.cont_live_page)
        self.ui.bt_vechile_search.clicked.connect(self.cont_vsearch_page)
        self.ui.bt_notification.clicked.connect(self.cont_notification_page)
        #self.ui.bt_old_footage.clicked.connect(self.cont_oldf_page)
        self.ui.bt_history.clicked.connect(self.cont_history_page)


        #control cams
        self.ui.pushButton.clicked.connect(self.cam1_page)
        #self.ui.pushButton_2.clicked.connect(self.cam2_page)
        #self.ui.pushButton_3.clicked.connect(self.cam3_page)
        self.ui.pushButton_4.clicked.connect(self.cam_test_page)

        #control test video in cams
        #self.ui.openBtn_1.clicked.connect(self.open_file)
        self.ui.playBtn.clicked.connect(self.play_video)
        self.ui.slider.sliderMoved.connect(self.seek)

        self.ui.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.ui.mediaPlayer.positionChanged.connect(self.position_changed)
        self.ui.mediaPlayer.durationChanged.connect(self.duration_changed)


        self.ui.playBtn_his.clicked.connect(self.play_video_his)
        self.ui.slider_his.sliderMoved.connect(self.seek_his)
        self.ui.slider_his.setEnabled(True)


        self.ui.mediaPlayer.stateChanged.connect(self.mediastate_changed_his)
        self.ui.mediaPlayer.positionChanged.connect(self.position_changed_his)
        self.ui.mediaPlayer.durationChanged.connect(self.duration_changed_his)

        

        #self.ui.playBtn.setEnabled(False)
        self.ui.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(rf'C:\Users\Bebo\Desktop\final_project\vechiles.mp4')))
        self.ui.playBtn.setEnabled(True)
        video_icon = QtGui.QIcon()

        video_icon.addPixmap(QtGui.QPixmap(Vpath+"\play-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.playBtn.setIcon(video_icon)



        #connect search button
        self.ui.Search.clicked.connect(self.go_vid)

        self.ui.playBtn_sp.clicked.connect(self.play_video_list)
        self.ui.slider_sp.sliderMoved.connect(self.seek)

        self.ui.mediaPlayer_sp.stateChanged.connect(self.mediastate_changed_list)
        self.ui.mediaPlayer_sp.positionChanged.connect(self.position_changed_list)
        self.ui.mediaPlayer_sp.durationChanged.connect(self.duration_changed_list)

        self.ui.playBtn_sp.clicked.connect(self.play_video)

        #self.ui.playBtn.setEnabled(False)
        #self.ui.mediaPlayer_sp.setMedia(QMediaContent(QUrl.fromLocalFile(rf'C:\Users\Bebo\Desktop\final_project\vechiles.mp4')))
        self.ui.playBtn_sp.setEnabled(True)
        video_icon_sp = QtGui.QIcon()

        video_icon_sp.addPixmap(QtGui.QPixmap(Vpath+"\play-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.playBtn_sp.setIcon(video_icon)


        
        #self.ui.list_view.clicked.connect(self.on_clicked_video)
        self.ui.list_view.doubleClicked.connect(self.on_clicked_video)
        self.ui.h_list_view.doubleClicked.connect(self.on_clicked_hisVid)

        #self.ui.list_view.setItemDelegate(self.ui.file_system_model)

        self.ui.back_sp.clicked.connect(self.back_search_sp)
        self.ui.back_his.clicked.connect(self.back_his)




        self.ui.record_button.clicked.connect(self.start_recording)
        self.ui.stop_button.clicked.connect(self.stop_recording)

        # Creating a thread to continuously display the video stream
        self.thread = VideoThread()
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.start()

        self.playerState = QMediaPlayer.StoppedState
        self.playerState_list = QMediaPlayer.StoppedState
        self.playerState_his = QMediaPlayer.StoppedState


    def go_vid(self):
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_vidp_p)
    def state(self):
        return self.playerState

    def setState(self,state):
        if state != self.playerState:
            self.playerState = state

            if state == QMediaPlayer.StoppedState:
                self.ui.playBtn.setEnabled(True)
                self.playButton.setIcon(
                        self.style().standardIcon(QStyle.SP_MediaPlay))
            elif state == QMediaPlayer.PlayingState:
                self.ui.playBtn.setEnabled(False)
                self.playButton.setIcon(
                        self.style().standardIcon(QStyle.SP_MediaPause))
            elif state == QMediaPlayer.PausedState:
                self.ui.playBtn.setEnabled(True)
                self.playButton.setIcon(
                        self.style().standardIcon(QStyle.SP_MediaPlay))

    def play_video(self):
        if self.ui.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.ui.mediaPlayer.pause()

        else:
            self.ui.mediaPlayer.play()


    def mediastate_changed(self, state):
        Vpath = r"C:\Users\Bebo\Desktop\final_project\icons"
        vid_icon = QtGui.QIcon()
        if self.ui.mediaPlayer.state() == QMediaPlayer.PlayingState:
            vid_icon.addPixmap(QtGui.QPixmap(Vpath+"\pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.playBtn.setIcon(vid_icon)

        else:
            vid_icon.addPixmap(QtGui.QPixmap(Vpath+"\play-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.playBtn.setIcon(vid_icon)

    
    def updateDurationInfo(self, currentInfo):
            duration = self.duration
            if currentInfo or duration:
                currentTime = QTime((currentInfo/3600)%60, (currentInfo/60)%60,
                        currentInfo%60, (currentInfo*1000)%1000)
                totalTime = QTime((duration/3600)%60, (duration/60)%60,
                        duration%60, (duration*1000)%1000);

                format = 'hh:mm:ss' if duration > 3600 else 'mm:ss'
                tStr = currentTime.toString(format) + " / " + totalTime.toString(format)
            else:
                tStr = ""

            self.ui.labelDuration_test.setText(tStr)

    def position_changed(self, progress):
        progress /= 1000

        if not self.ui.slider.isSliderDown():
            self.ui.slider.setValue(progress)

        self.updateDurationInfo(progress)
        #self.slider.setValue(progress)


    def duration_changed(self, duration):
        duration /= 1000

        self.duration = duration
        self.ui.slider.setMaximum(duration)

    def set_position(self, position):
            self.ui.mediaPlayer.setPosition(position)

    def seek(self, seconds):
            self.ui.mediaPlayer.setPosition(seconds * 1000)
            self.ui.mediaPlayer.play()




#####################
######################

    def state_list(self):
        return self.playerState_list

    def setState_list(self,state):
        if state != self.playerState_list:
            self.playerState_list = state

            if state == QMediaPlayer.StoppedState:
                self.ui.playBtn_sp.setEnabled(True)
                self.playButton.setIcon(
                        self.style().standardIcon(QStyle.SP_MediaPlay))
            elif state == QMediaPlayer.PlayingState:
                self.ui.playBtn_sp.setEnabled(False)
                self.playButton.setIcon(
                        self.style().standardIcon(QStyle.SP_MediaPause))
            elif state == QMediaPlayer.PausedState:
                self.ui.playBtn_sp.setEnabled(True)
                self.playButton.setIcon(
                        self.style().standardIcon(QStyle.SP_MediaPlay))

    def play_video_list(self):
        if self.ui.mediaPlayer_sp.state() == QMediaPlayer.PlayingState:
            self.ui.mediaPlayer_sp.pause()

        else:
            self.ui.mediaPlayer_sp.play()


    def mediastate_changed_list(self, state):
        Vpath = r"C:\Users\Bebo\Desktop\final_project\icons"
        vid_icon = QtGui.QIcon()
        if self.ui.mediaPlayer_sp.state() == QMediaPlayer.PlayingState:
            vid_icon.addPixmap(QtGui.QPixmap(Vpath+"\pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.playBtn_sp.setIcon(vid_icon)

        else:
            vid_icon.addPixmap(QtGui.QPixmap(Vpath+"\play-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.playBtn_sp.setIcon(vid_icon)

    
    def updateDurationInfo_list(self, currentInfo):
            duration = self.duration_list
            if currentInfo or duration:
                currentTime = QTime((currentInfo/3600)%60, (currentInfo/60)%60,
                        currentInfo%60, (currentInfo*1000)%1000)
                totalTime = QTime((duration/3600)%60, (duration/60)%60,
                        duration%60, (duration*1000)%1000);

                format = 'hh:mm:ss' if duration > 3600 else 'mm:ss'
                tStr = currentTime.toString(format) + " / " + totalTime.toString(format)
            else:
                tStr = ""

            self.ui.labelDuration_sp.setText(tStr)

    def position_changed_list(self, progress):
        progress /= 1000

        if not self.ui.slider_sp.isSliderDown():
            self.ui.slider_sp.setValue(progress)

        self.updateDurationInfo(progress)
        #self.slider.setValue(progress)


    def duration_changed_list(self, duration):
        duration /= 1000

        self.duration = duration
        self.ui.slider_sp.setMaximum(duration)

    def set_position_list(self, position):
            self.ui.mediaPlayer_sp.setPosition(position)

    def seek_list(self, seconds):
            self.ui.mediaPlayer_sp.setPosition(seconds * 1000)
            self.ui.mediaPlayer_sp.play()




    
    def state_his(self):
        return self.playerState_his

    def setState_his(self,state):
        if state != self.playerState_his:
            self.playerState_his = state

            if state == QMediaPlayer.StoppedState:
                self.ui.playBtn_his.setEnabled(True)
                self.playButton.setIcon(
                        self.style().standardIcon(QStyle.SP_MediaPlay))
            elif state == QMediaPlayer.PlayingState:
                self.ui.playBtn_his.setEnabled(False)
                self.playButton.setIcon(
                        self.style().standardIcon(QStyle.SP_MediaPause))
            elif state == QMediaPlayer.PausedState:
                self.ui.playBtn_his.setEnabled(True)
                self.playButton.setIcon(
                        self.style().standardIcon(QStyle.SP_MediaPlay))

    def play_video_his(self):
        if self.ui.mediaPlayer_his.state() == QMediaPlayer.PlayingState:
            self.ui.mediaPlayer_his.pause()

        else:
            self.ui.mediaPlayer_his.play()


    def mediastate_changed_his(self, state):
        Vpath = r"C:\Users\Bebo\Desktop\final_project\icons"
        vid_icon = QtGui.QIcon()
        if self.ui.mediaPlayer_his.state() == QMediaPlayer.PlayingState:
            vid_icon.addPixmap(QtGui.QPixmap(Vpath+"\pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.playBtn_his.setIcon(vid_icon)

        else:
            vid_icon.addPixmap(QtGui.QPixmap(Vpath+"\play-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.playBtn_his.setIcon(vid_icon)

    
    def updateDurationInfo_his(self, currentInfo):
            duration = self.duration
            if currentInfo or duration:
                currentTime = QTime((currentInfo/3600)%60, (currentInfo/60)%60,
                        currentInfo%60, (currentInfo*1000)%1000)
                totalTime = QTime((duration/3600)%60, (duration/60)%60,
                        duration%60, (duration*1000)%1000);

                format = 'hh:mm:ss' if duration > 3600 else 'mm:ss'
                tStr = currentTime.toString(format) + " / " + totalTime.toString(format)
            else:
                tStr = ""

            self.ui.labelDuration_his.setText(tStr)

    def position_changed_his(self, progress):
        progress /= 1000

        if not self.ui.slider.isSliderDown():
            self.ui.slider_his.setValue(progress)

        self.updateDurationInfo(progress)
        #self.slider.setValue(progress)


    def duration_changed_his(self, duration):
        duration /= 1000

        self.duration = duration
        self.ui.slider_his.setMaximum(duration)

    def set_position_his(self, position):
            self.ui.mediaPlayer_his.setPosition(position)

    def seek_his(self, seconds):
            self.ui.mediaPlayer_his.setPosition(seconds * 1000)
            self.ui.mediaPlayer_his.play()





    def on_clicked_video(self, index):
            x = index.data(Qt.DisplayRole)
            self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_vidp_p)
            path =rf'C:\Users\Bebo\Desktop\final_project\icons\videos\{x}'
            self.ui.mediaPlayer_sp.setMedia(QMediaContent(QUrl.fromLocalFile(path)))
            y = str(x)
            self.ui.label_sp.setText(y.replace('.mp4', ' '))
            print(path)

    def on_clicked_hisVid(self, index):
            x = index.data(Qt.DisplayRole)
            self.ui.stackedWidget_5.setCurrentWidget(self.ui.page_vidp_his)
            path =rf'C:\Users\Bebo\Desktop\final_project\icons\history\{x}'
            self.ui.mediaPlayer_his.setMedia(QMediaContent(QUrl.fromLocalFile(path)))
            y = str(x)
            self.ui.label_sp.setText(y.replace('.mp4', ' '))
            print(path)

    def on_clicked_notiVid(self, index):
            x = index.data(Qt.DisplayRole)
            self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_vidp_p)
            path =rf'C:\Users\Bebo\Desktop\final_project\icons\notification{x}'
            self.ui.mediaPlayer_sp.setMedia(QMediaContent(QUrl.fromLocalFile(path)))
            y = str(x)
            self.ui.label_sp.setText(y.replace('.mp4', ' '))
            print(path)




  ####################
    ####################
        # Update the video player with the current frame
    def update_image(self, img):
        self.ui.video_label.setPixmap(QPixmap.fromImage(img))
        self.ui.TM_label.setText(QtCore.QDateTime.currentDateTime().toString())
        

    # Start recording the video
    def start_recording(self):
        self.thread.recording_flag = True
        self.ui.record_button.setEnabled(False)
        self.ui.stop_button.setEnabled(True)

    # Stop recording the video
    def stop_recording(self):
        self.thread.recording_flag = False
        self.ui.record_button.setEnabled(True)
        self.ui.stop_button.setEnabled(False)


    #control main menu functions
    def cont_live_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_live)
    def cont_vsearch_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_vechile_search)
    def cont_notification_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_notification)
    def cont_oldf_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_old_footage)
    def cont_history_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_history)
    
    #control cams functions
    def cam1_page(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.cam1)
    def cam2_page(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.cam2)
    def cam3_page(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.cam3)
    def cam_test_page(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.testvideo)

    #control test video in cams
    def open_file(self):
        filename , _ = QFileDialog.getOpenFileName()
        #filename.sleep(30)

        print(filename)
        if filename != " ":
            self.ui.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            #self.ui.playBtn.setEnabled(True)


    
    
    def handle_errors(self):
        self.ui.playBtn.setEnabled(False)

    def set_position_sp(self, position):
            self.ui.mediaPlayer_sp.setPosition(position)
    def back_search_sp(self):
            self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_btlist_s)
    def back_his(self):
            self.ui.stackedWidget_5.setCurrentWidget(self.ui.page_btlist_his)

    #conrol MainWindow functions
    def control_bt_hide(self):
        self.showMinimized()
    def control_bt_mini(self):
        self.showNormal()
    def control_bt_max(self):
        self.showMaximized()
    def control_bt_close(self):
        self.close()
    
    #move and resize window functions
    def resizeEvent(self , event):
        rec = self.rect()
        self.ui.grip.move(rec.right() - self.ui.gripSize, rec.bottom() - self.ui.gripSize)

    def mousePressEvent(self , event):
        self.clickPosition = event.globalPos()
   
    def mover_window(self , event):
        if self.isMaximized() == False:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        if event.globalPos().y() <=10:
            self.showMaximized()
        else:
            self.showNormal()

class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(QImage)

    def __init__(self):
        super().__init__()
        self._run_flag = True
        self.recording_flag = False
        self.pause_writing_flag = False

  
###############################################################
    def run(self):
        VideoThread.record_video(self ,file_name ="")


    def record_video(self,file_name):

        cap = cv2.VideoCapture(0)
        #ret, frame = cap.read()

        

        out = None

        # Set the start time
        start_time = time.time()

        while True:
            # Read a frame from the capture device
            ret, frame = cap.read()
            

            file_name = rf"C:\Users\Bebo\Desktop\final_project\icons\videos\{current_time}.mp4"
            out = ffmpegcv.VideoWriter(file_name,None, 30)
                # Check if 5 minutes have passed
            while self._run_flag:
                    ret, frame = cap.read()

                    if out is None:
                        x = rf"C:\Users\Bebo\Desktop\final_project\icons\videos\{current_time}.mp4"
                        out = ffmpegcv.VideoWriter(x,None, 30)
                    if ret:
                        # Display video frames
                        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        h, w, ch = rgb_frame.shape
                        bytes_per_line = ch * w
                        img = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
                        self.change_pixmap_signal.emit(img)
                        if self.recording_flag:
                            if not self.pause_writing_flag:
                                out.write(frame)
                                if time.time() - start_time >= 50:
                                    # Release the video file writer object
                                    #out.release()

                                    # Reset the start time
                                    start_time = time.time()
                                
                                    
                                    x = rf"C:\Users\Bebo\Desktop\final_project\icons\videos\{current_time}.mp4"
                                    #video_file_name = "video-" + time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()) + ".mp4"
                                    out = None

            if not self._run_flag:
                break
            
            
            
                
                    
                
                                


        
            # Write the frame to the video file

 


##############################################################################################


    # Resume video writing
    def resume_writing(self):
        self.pause_writing_flag = False

"""   
if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = control.MiApp()
     mi_app.show()
     sys.exit(app.exec_())  
"""