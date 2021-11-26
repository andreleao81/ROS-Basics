#! /usr/bin/env python3
# license removed for brevity

import rospy
from geometry_msgs.msg import Twist

import random 


class Talker:

    def __init__(self):
        rospy.init_node('talker1', anonymous = True)
        self.pub = rospy.Publisher('vel_components', Twist, queue_size = 10)
        self.lst = list (range(100,200))
        self.lst2 = list(range(10))

    def start(self):
        rate = rospy.Rate(5) # 5hz

        while not rospy.is_shutdown():
            vel_msg = Twist()
            #define components
            vel_msg.linear.x = random.choice(self.lst)
            vel_msg.linear.y = random.choice(self.lst)
            vel_msg.linear.z = random.choice(self.lst)
            vel_msg.angular.x = random.choice(self.lst2)
            vel_msg.angular.y = random.choice(self.lst2)
            vel_msg.angular.z = random.choice(self.lst2)

            rospy.loginfo(f'linear velocity:\n{vel_msg.linear}')
            rospy.loginfo(f'angular velocity:\n{vel_msg.angular}') 

            self.pub.publish(vel_msg) 
            rate.sleep()
    


if __name__ == '__main__':

    try:
        t = Talker()
        t.start()
    except  rospy.ROSInterruptException:
        pass