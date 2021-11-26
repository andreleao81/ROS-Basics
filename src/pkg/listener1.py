#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32

import math


class Listener:
    
    def __init__(self):
        rospy.init_node('listener1', anonymous=True)
        rospy.Subscriber("vel_components", Twist, self.callback)
        self.pub = rospy.Publisher('linear_vel', Float32, queue_size=10)
        self.pub1 = rospy.Publisher('angular_vel', Float32, queue_size=10)

    def callback(self, msg):
        vel = msg
        vel_linear = math.sqrt(vel.linear.x**2 + vel.linear.y**2 + vel.linear.z**2)
        vel_angular = math.sqrt(vel.angular.x**2 + vel.angular.y**2 + vel.angular.z**2)
        a = Float32()
        l = Float32()
        a.data = vel_angular
        l.data = vel_linear
        self.pub.publish(l)
        self.pub1.publish(a)    
        
        

if __name__ == '__main__':
    l = Listener()
    rospy.spin()
