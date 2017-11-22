#!/usr/bin/python

import sys
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
from PyQt5.QtCore import QThread, QStringListModel, QModelIndex, pyqtSignal
from PyQt5.QtWidgets import QListView

class QNode(QThread):
    updateLog = pyqtSignal() ## create a signal to emit when the listview updates
    rosShutdown = pyqtSignal() ## signal the gui for a shutdown
    def __init__(self, queue_view):
        QThread.__init__(self)
        rospy.init_node('listenerim',anonymous=True)

        self.queue = queue_view
        #self.model = QStringListModel(self)
        #self.list = []
        #self.model.setStringList(self.list)
        #self.text_window.setModel(self.model)

        ##connect signal
    def __del__(self):
        if not rospy.is_shutdown():

            #rospy.shutdown('shutdown reason')
            self.wait()

    def callback(self, data):
        #hello = rospy.get_caller_id() + 'I heard ' + data.data
        #self.list.append(hello)
        #self.model.setStringList(self.list)
        #self.text_window.setModel(self.model)
        #self.updateLog.emit()

        #rospy.loginfo(hello)
        br = CvBridge()
        rospy.loginfo('receiving image')
        dx = br.imgmsg_to_cv2(data)
        frame = {}
        frame["img"] = dx
        self.queue.put(frame)

    def run(self):
        rospy.Subscriber('imageri', Image, self.callback) #2hz
        rospy.spin()
        self.rosShutdown.emit() #emit signal for shutdown
