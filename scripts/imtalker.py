#!/usr/bin/env python
import rospy
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import time
def talker():
    pub = rospy.Publisher('imageri', Image, queue_size=10)
    rospy.init_node('talkerim',anonymous=True)
    rate = rospy.Rate(5) #2hz
    capture = cv2.VideoCapture(0)
    br = CvBridge()
    while not rospy.is_shutdown():
        [status, img] = capture.read()
        if status == True:
            rospy.loginfo('publish image')
            pub.publish(br.cv2_to_imgmsg(img))
            rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
