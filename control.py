from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
import final_cctv
from PyQt5.QtCore import QDir, QUrl
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTime, QDateTime
import cv2
import subprocess
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time
import os
from PyQt5.QtWidgets import QFileDialog, QFileSystemModel
import torch
import torch.nn as nn
import cv2
import csv
import json
import torchvision.models as models
import statistics
import math
import subprocess
from torchvision import transforms
import time
from object_tracking import *

model = torch.hub.load('ultralytics/yolov5', 'yolov5m', pretrained=True)
model.eval();
class Image_Classifier(nn.Module):
    def init(self):
        super().init()
        self.model = nn.Sequential(
             Conv2d(3, 32, kernel_size=(3, 3), stride=(1, 1)),
             ReLU(),
             Conv2d(32, 32, kernel_size=(3, 3), stride=(1, 1)),
             ReLU(),
             MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False),
             Flatten(start_dim=1, end_dim=-1),
             Dropout(p=0.25, inplace=False),
             Linear(in_features=6272, out_features=132, bias=True),
             ReLU(),
             Dropout(p=0.5, inplace=False),
             Linear(in_features=132, out_features=11, bias=True),
        )

    def forward(self, x):
        return self.model(x)
    

Vpath = os.path.dirname(os.path.abspath(__file__))

color_classifier = torch.load(rf"{Vpath}\2layers_colour_model.pt")
color_classifier = color_classifier.cuda()
color_classifier.eval()

body_classifier = torch.load(rf'{Vpath}\model.pt')
body_classifier.eval();
flag = True

class MiApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = final_cctv.Ui_MainWindow() 
        self.ui.setupUi(self)

        self.file_path =''
        self.duration = 0
        self.duration_list = 0
        self.duration_his = 0

    

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

        #control test video player in cams
        #self.ui.openBtn_1.clicked.connect(self.open_file)
        self.ui.playBtn.clicked.connect(self.play_video)
        self.ui.slider.sliderMoved.connect(self.seek)

        #self.ui.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        #self.ui.mediaPlayer.positionChanged.connect(self.position_changed)
        #self.ui.mediaPlayer.durationChanged.connect(self.duration_changed)
        self.ui.mediaPlayer.positionChanged.connect(self.position_changed)
        self.ui.mediaPlayer.durationChanged.connect(self.duration_changed)

        self.ui.slider.setRange(0, self.ui.mediaPlayer.duration() // 1000)
        self.ui.slider.sliderMoved.connect(self.set_position)

        self.ui.mediaPlayer.stateChanged.connect(self.mediastate_changed)

        self.ui.mediaPlayer.mediaStatusChanged.connect(self.handle_media_status)

        if not os.path.exists("videos"):
                os.makedirs("videos")
        if not os.path.exists("vechiles"):
                os.makedirs("vechiles")
        if not os.path.exists("history"):
                os.makedirs("history")
        if not os.path.exists("notification"):
                os.makedirs("notification")

        self.ui.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(rf'{os.path.dirname(os.path.abspath(__file__))}\test_video\vechiles.mp4')))
        video_icon = QtGui.QIcon()
        video_icon.addPixmap(QtGui.QPixmap(rf"{Vpath}\play-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.playBtn.setIcon(video_icon)
        self.ui.playBtn.setEnabled(True)


        #control test video player in history
        self.ui.playBtn_his.clicked.connect(self.play_video_his)
        self.ui.slider_his.sliderMoved.connect(self.seek_his)

        self.ui.mediaPlayer_his.stateChanged.connect(self.mediastate_changed_his)
        self.ui.mediaPlayer_his.positionChanged.connect(self.position_changed_his)
        self.ui.mediaPlayer_his.durationChanged.connect(self.duration_changed_his)        
        video_icon_his = QtGui.QIcon()
        video_icon_his.addPixmap(QtGui.QPixmap(rf"{Vpath}\play-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.playBtn_his.setIcon(video_icon_his)
        self.ui.playBtn_his.setEnabled(True)

        
        #control test video player in list view of search
        self.ui.playBtn_sp.clicked.connect(self.play_video_list)
        self.ui.slider_sp.sliderMoved.connect(self.seek_list)

        self.ui.mediaPlayer_sp.stateChanged.connect(self.mediastate_changed_list)
        self.ui.mediaPlayer_sp.positionChanged.connect(self.position_changed_list)
        self.ui.mediaPlayer_sp.durationChanged.connect(self.duration_changed_list)
        
        video_icon_sp = QtGui.QIcon()
        video_icon_sp.addPixmap(QtGui.QPixmap(rf"{Vpath}\play-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.playBtn_sp.setIcon(video_icon_his)
        self.ui.playBtn_sp.setEnabled(True)

        #self.ui.playBtn.setEnabled(False)
        #self.ui.mediaPlayer_sp.setMedia(QMediaContent(QUrl.fromLocalFile(rf'C:\Users\Bebo\Desktop\final_project\vechiles.mp4')))
        #video_icon_sp = QtGui.QIcon()
        #video_icon_sp.addPixmap(QtGui.QPixmap(Vpath+"\play-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.ui.playBtn_sp.setIcon(video_icon)

        #connect search button
        self.ui.Search.clicked.connect(self.go_vid)
        
        self.ui.list_view_folders.doubleClicked.connect(self.on_clicked_listvideo_search)
        self.ui.list_view.doubleClicked.connect(self.on_clicked_video)
        self.ui.h_list_view.doubleClicked.connect(self.on_clicked_hisVid)

        #self.ui.list_view.setItemDelegate(self.ui.file_system_model)

        self.ui.back_sp.clicked.connect(self.back_search_sp)
        self.ui.back_his.clicked.connect(self.back_his)
        self.ui.backbt_file.clicked.connect(self.back_listview_folders)




        self.ui.record_button.clicked.connect(self.start_recording)
        self.ui.stop_button.clicked.connect(self.stop_recording)
        if self.ui.record_button.isChecked():
                self.flag = True

        # Creating a thread to continuously display the video stream
        self.thread = VideoThread()
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.start()

        self.playerState = QMediaPlayer.StoppedState
        self.playerState_list = QMediaPlayer.StoppedState
        self.playerState_his = QMediaPlayer.StoppedState


    def go_vid(self):
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_vidp_p)


    #########################################
    #conrol videoplayer of test video on cams
    def play_video(self):
        self.ui.videoWidget.setVisible(True)
        if self.ui.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.ui.mediaPlayer.pause()
        else:
            self.ui.mediaPlayer.play()

        


    def handle_media_status(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.ui.mediaPlayer.setPosition(0)
            self.ui.mediaPlayer.stop()
            self.ui.videoWidget.repaint()
            #self.ui.videoWidget.setDisabled(True)
            self.ui.videoWidget.setHidden(True)
            

            #self.ui.videoWidget.setFullScreen(False)



    def mediastate_changed(self, state):
        Vpath = os.path.dirname(os.path.abspath(__file__))
        vid_icon = QtGui.QIcon()
        if self.ui.mediaPlayer.state() == QMediaPlayer.PlayingState:
            vid_icon.addPixmap(QtGui.QPixmap(rf"{Vpath}\pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.playBtn.setIcon(vid_icon)

        else:
            vid_icon.addPixmap(QtGui.QPixmap(rf"{Vpath}\play-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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

            self.ui.labelDuration.setText(tStr)

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





##############################
#control video player of search
    def play_video_list(self):
        if self.ui.mediaPlayer_sp.state() == QMediaPlayer.PlayingState:
            self.ui.mediaPlayer_sp.pause()

        else:
            self.ui.mediaPlayer_sp.play()


    def mediastate_changed_list(self, state_list):
        Vpath = os.path.dirname(os.path.abspath(__file__))
        vid_icon = QtGui.QIcon()
        if self.ui.mediaPlayer_sp.state() == QMediaPlayer.PlayingState:
            vid_icon.addPixmap(QtGui.QPixmap(rf"{Vpath}\pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.playBtn_sp.setIcon(vid_icon)

        else:
            vid_icon.addPixmap(QtGui.QPixmap(rf"{Vpath}\play-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.playBtn_sp.setIcon(vid_icon)

    
    def updateDurationInfo_list(self, currentInfo_list):
            duration_list = self.duration_list
            if currentInfo_list or duration_list:
                currentTime_list = QTime((currentInfo_list/3600)%60, (currentInfo_list/60)%60,
                        currentInfo_list%60, (currentInfo_list*1000)%1000)
                totalTime_list = QTime((duration_list/3600)%60, (duration_list/60)%60,
                        duration_list%60, (duration_list*1000)%1000);

                format_list = 'hh:mm:ss' if duration_list > 3600 else 'mm:ss'
                tStr_list = currentTime_list.toString(format_list) + " / " + totalTime_list.toString(format_list)
            else:
                tStr_list = ""

            self.ui.labelDuration_sp.setText(tStr_list)

    def position_changed_list(self, progress_list):
        progress_list /= 1000

        if not self.ui.slider_sp.isSliderDown():
            self.ui.slider_sp.setValue(progress_list)

        self.updateDurationInfo_list(progress_list)
        #self.slider.setValue(progress)


    def duration_changed_list(self, duration_list):
        duration_list /= 1000

        self.duration_list = duration_list
        self.ui.slider_sp.setMaximum(duration_list)

    def set_position_list(self, position_list):
            self.ui.mediaPlayer_sp.setPosition(position_list)

    def seek_list(self, seconds_list):
            self.ui.mediaPlayer_sp.setPosition(seconds_list * 1000)
            self.ui.mediaPlayer_sp.play()




##############################
#control video player in history
    def play_video_his(self):
        if self.ui.mediaPlayer_his.state() == QMediaPlayer.PlayingState:
            self.ui.mediaPlayer_his.pause()

        else:
            self.ui.mediaPlayer_his.play()


    def mediastate_changed_his(self, state_his):
        Vpath = os.path.dirname(os.path.abspath(__file__))
        vid_icon = QtGui.QIcon()
        if self.ui.mediaPlayer_his.state() == QMediaPlayer.PlayingState:
            vid_icon.addPixmap(QtGui.QPixmap(rf"{Vpath}\pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.playBtn_his.setIcon(vid_icon)

        else:
            vid_icon.addPixmap(QtGui.QPixmap(rf"{Vpath}\play-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.playBtn_his.setIcon(vid_icon)

    
    def updateDurationInfo_his(self, currentInfo_his):
            duration_his = self.duration_his
            if currentInfo_his or duration_his:
                currentTime_his = QTime((currentInfo_his/3600)%60, (currentInfo_his/60)%60,
                        currentInfo_his%60, (currentInfo_his*1000)%1000)
                totalTime_his = QTime((duration_his/3600)%60, (duration_his/60)%60,
                        duration_his%60, (duration_his*1000)%1000);

                format_his = 'hh:mm:ss' if duration_his > 3600 else 'mm:ss'
                tStr_his = currentTime_his.toString(format_his) + " / " + totalTime_his.toString(format_his)
            else:
                tStr_his = ""

            self.ui.labelDuration_his.setText(tStr_his)

    def position_changed_his(self, progress_his):
        progress_his /= 1000

        if not self.ui.slider_his.isSliderDown():
            self.ui.slider_his.setValue(progress_his)

        self.updateDurationInfo_his(progress_his)
        #self.slider.setValue(progress)


    def duration_changed_his(self, duration_his):
        duration_his /= 1000

        self.duration_his = duration_his
        self.ui.slider_his.setMaximum(duration_his)

    def set_position_his(self, position_his):
            self.ui.mediaPlayer_his.setPosition(position_his)

    def seek_his(self, seconds_his):
            self.ui.mediaPlayer_his.setPosition(seconds_his * 1000)
            self.ui.mediaPlayer_his.play()





    def on_clicked_video(self, index):
            x = index.data(Qt.DisplayRole)
            self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_vidp_p)
            slash = "\\"
            path =rf"{self.files_path}{slash}{x}"
            self.ui.mediaPlayer_sp.setMedia(QMediaContent(QUrl.fromLocalFile(path)))
            y = str(x)
            self.ui.label_sp.setText(y.replace('.mp4', ' '))
            print(path)

    def on_clicked_listvideo_search(self, index):
            x = index.data(Qt.DisplayRole)
            self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_btlist_s)
            path =rf'{os.path.dirname(os.path.abspath(__file__))}\videos\{x}'
            self.files_path = path
            self.file_system_model = QFileSystemModel()
            self.file_system_model.setRootPath(QDir.homePath())
            self.file_system_model.setNameFilters(['*.mp4', '*.avi', '*.mkv'])
            self.ui.list_view.setModel(self.file_system_model)
            self.ui.list_view.setRootIndex(self.file_system_model.index(path))
            print(path)

    def on_clicked_hisVid(self, index):
            x = index.data(Qt.DisplayRole)
            self.ui.stackedWidget_5.setCurrentWidget(self.ui.page_vidp_his)
            path =rf'{os.path.dirname(os.path.abspath(__file__))}\history\{x}'
            self.ui.mediaPlayer_his.setMedia(QMediaContent(QUrl.fromLocalFile(path)))
            y = str(x)
            self.ui.label_sp.setText(y.replace('.mp4', ' '))
            print(path)

    def on_clicked_notiVid(self, index):
            x = index.data(Qt.DisplayRole)
            self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_vidp_p)
            path =rf'{os.path.dirname(os.path.abspath(__file__))}\notification\{x}'
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
        self.thread.pause_writing_flag = False
        self.ui.record_button.setEnabled(False)
        self.ui.stop_button.setEnabled(True)

    # Stop recording the video
    def stop_recording(self):
        self.thread.recording_flag = False
        self.thread.pause_writing_flag = True
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
    def back_listview_folders(self):
         self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_btlist_folders)

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
    #def run(self):
    #    VideoThread.record_video(self) 


    def run(self):

        cap = cv2.VideoCapture(0)
        #ret, frame = cap.read()
       
        # Open the output file for writing
        #out = subprocess.Popen(ffmpeg_cmd.split(' '), stdin=subprocess.PIPE)
        

        out = None

        # Set the start time
        start_time = time.time()

        while True:
            #cap = cv2.VideoCapture(0)

            fps = cap.get(cv2.CAP_PROP_FPS)
            frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

            ffmpeg_cmd = f"ffmpeg -y -f rawvideo -pix_fmt bgr24 -s {frame_width}x{frame_height} -r {fps} -i - -c:v libx264 -preset fast -crf 30 -pix_fmt nv12 -an -vcodec libx264 {output_path}"

            #output_file = subprocess.Popen(ffmpeg_cmd.split(' '), stdin=subprocess.PIPE)
            
            mot_tracker = Sort(max_age=30, min_hits=60) 

            object_dict = {}

            frame_cut = 0
            frame_count = 0
            clf_state = False

            start = time.time()








            # Read a frame from the capture device
            ret, frame = cap.read()
            current_time = QDateTime.currentDateTime().toString('yyyy-MM-dd-hh-mm-ss')

            parent_dir = rf"{os.path.dirname(os.path.abspath(__file__))}\videos"
            directory = QDateTime.currentDateTime().toString('yyyy-MM-dd')
            folder_path = os.path.join(parent_dir, directory)
            

            
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
                print(folder_path)

            output_path = rf"{folder_path}\{current_time}.mp4"
            #print(output_path)

            #fps = int(30)
            #frame_width = int(640)
            #frame_height = int(480)
            # Define the ffmpeg command to write the output video
            #ffmpeg_cmd = f"ffmpeg -y -f rawvideo -pix_fmt bgr24 -s {frame_width}x{frame_height} -r {fps} -i - -c:v libx264 -crf 18 -preset veryfast {output_path}"

            

            out = subprocess.Popen(ffmpeg_cmd.split(' '), stdin=subprocess.PIPE)
                # Check if 5 minutes have passed
            while self._run_flag:
                    ret, frame = cap.read()
                    #######################
                    if not ret:
                        print('Video processing completed')
                        break
                    

                    if ret:
                        # Display video frames
                        frame_model = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        h, w, ch = frame_model.shape()
                        bytes_per_line = ch * w
                        img = QImage(frame_model.data, w, h, bytes_per_line, QImage.Format_RGB888)
                        self.change_pixmap_signal.emit(img)
                        results = model(frame_model[frame_cut:])

                        track_bbs_ids = mot_tracker.update(results.xyxy[0][:,:4].cpu())
                        for x1, y1, x2, y2, obj_id in track_bbs_ids:
                            cx1 = int((x1 + x2) / 2)
                            cy1 = int((y1 + y2) / 2)
                            width = abs(x2 - x1)
                            height = abs(y2 - y1)
                            diagonal = math.sqrt(width**2 + height**2)
                            
                            
                            if diagonal > 100 :
                                try: #TODO optimize
                                    car_image = frame_model[int(y1):int(y2), int(x1):int(x2)]
                                    transform = transforms.Compose([transforms.ToTensor(),
                                                                    transforms.Resize((32,32)),])
                                    car_image = transform(car_image)
                                    car_image = car_image.cuda()
                                    
                                    body_car_image = frame_model[int(y1):int(y2), int(x1):int(x2)]
                                    transform = transforms.Compose([transforms.ToTensor(),
                                                                    transforms.Resize((256,256)),])
                                    body_car_image = transform(body_car_image)
                                    body_car_image = body_car_image.cuda()
                                except:
                                    print('no object detected')
                                    continue
                                with torch.no_grad():
                                    color_output = color_classifier(car_image.unsqueeze(0))
                                    color_prediction = torch.argmax(color_output).item()
                                    color_name = ['black','blue','brown','green','grey','orange','pink','purple','red','white','yellow']
                                    color_class_name = color_name[color_prediction]

                                    body_output = body_classifier(body_car_image.unsqueeze(0))
                                    body_prediction = torch.argmax(body_output).item()
                                    body_name = ['Heavy-Duty', 'Lorry', 'Luxury', 'Pickup', 'SUV', 'Sedan', 'Van']
                                    body_class_name = body_name[body_prediction]
                                    clf_state = True

                            
                                if obj_id not in object_dict:
                                    object_dict[obj_id] = {
                                        'bboxes': [(x1, y1, x2, y2)],
                                        'frames':[frame_count],
                                        'color_classifier_preds': [color_prediction],
                                        'body_classifier_preds': [body_prediction]
                                    }
                                else:
                                    object_dict[obj_id]['bboxes'].append(( x1, y1, x2, y2))
                                    object_dict[obj_id]['frames'].append((frame_count))
                                    object_dict[obj_id]['color_classifier_preds'].append(color_prediction)
                                    object_dict[obj_id]['body_classifier_preds'].append(body_prediction)



                                # Calculate the mode prediction of the classifier for the tracked object
                                color_mode_pred = statistics.mode(object_dict[obj_id]['color_classifier_preds'])
                                object_dict[obj_id]['color_mode_pred'] = str(color_name[color_mode_pred])

                                body_mode_pred = statistics.mode(object_dict[obj_id]['body_classifier_preds'])
                                object_dict[obj_id]['body_mode_pred'] = str(body_name[body_mode_pred])
                            
                            if flag:
                                cv2.putText(frame, str(obj_id), (cx1, cy1), 0, 0.5, (255, 255, 255), 2)
                                if clf_state == True:
                                    cv2.putText(frame, color_name[color_mode_pred], (int(x1), int(y1)), cv2.FONT_HERSHEY_SIMPLEX, 1, (203, 192, 255), 2)
                                    cv2.putText(frame,  body_name[body_mode_pred], (int(cx1), int(y2)), cv2.FONT_HERSHEY_SIMPLEX, 1, (203, 192, 255), 2)
                                    clf_state = False

                        if self.recording_flag:
                            if time.time() - start_time >= 300:
                                    # Release the video file writer object
                                    #out.release()

                                    # Reset the start time
                                    start_time = time.time()
                                
                                    
                                    #x = rf"C:\Users\Bebo\Desktop\final_project\icons\videos\{current_time}.mp4"
                                    #video_file_name = "video-" + time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()) + ".mp4"
                                    out = None
                                    break
                            if not self.pause_writing_flag:
                                if out is None:
                                    current_time = QDateTime.currentDateTime().toString('yyyy-MM-dd-hh-mm-ss')

                                    output_path = rf"{folder_path}\{current_time}.mp4"
                                    #output_path = rf"C:\Users\Bebo\Desktop\final_project\icons\videos\{current_time}.mp4"
                                    fps = int(30)
                                    frame_width = int(640)
                                    frame_height = int(480)
                                    # Define the ffmpeg command to write the output video
                                    ffmpeg_cmd = f"ffmpeg -y -f rawvideo -pix_fmt bgr24 -s {frame_width}x{frame_height} -r {fps} -i - -c:v libx264 -crf 18 -preset veryfast {output_path}"
                                    out = subprocess.Popen(ffmpeg_cmd.split(' '), stdin=subprocess.PIPE)
                                out.stdin.write(frame.tobytes())
                                #out.stdin.write(frame)
                        if self.pause_writing_flag:
                                out = None

                                        
                                    
            if not self._run_flag:
                break

            
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