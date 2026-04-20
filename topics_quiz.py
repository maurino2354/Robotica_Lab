#! /usr/bin/env python
import ropsy
from std_msgs.msg import Int32
from sensor_msgs.msg import LaserScan


rospy.init_node('vel_publisher')
pub = rospy.Publisher('/cmd_vel', Int32, queue_size=1)
velocity = Int32()

while not rospy.is_shutdown():
	pub.publish(velocity)
def callback(msg):
    
    forward_distance = msg.ranges[0]
    print("Forward Distance: {:.3f} meters".format(forward_distance))
    
    backward_distance = msg.ranges[179]
    
    right_distance =msg.ranges[89]
    
    left_distance = msg.ranges[269]
    
    
    
    

def scan_listener():
    
    rospy.init_node('forward_scan_simple')
    
    
    rospy.Subscriber('/scan', LaserScan, callback)
    
    
    rospy.spin()

if __name__ == '__main__':
    scan_listener()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
