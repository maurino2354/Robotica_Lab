#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from std_srvs.srv import Trigger, TriggerResponse

def trimite(v_lin, v_ang, duration):
    msg = Twist()
    msg.linear.x, msg.angular.z = v_lin, v_ang
    rate = rospy.Rate(10)
    start_time = rospy.Time.now().to_sec()
    while not rospy.is_shutdown() and (rospy.Time.now().to_sec() - start_time) < duration:
        pub.publish(msg)
        rate.sleep()
    
#traseu
def traseu(req):
    trimite(0.2, 0.2, 30) # in cerc
    trimite(0.0, 0.0, 0.1) # stop
    return TriggerResponse(success=True, message='Cerc complet!')
   
rospy.init_node('jackal_server')
pub = rospy.Publisher('/jackal_velocity_controller/cmd_vel', Twist, queue_size=1)
srv = rospy.Service('do_circle', Trigger, traseu)
rospy.spin()
