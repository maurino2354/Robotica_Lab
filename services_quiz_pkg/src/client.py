#! /usr/bin/env python
import rospy
from std_srvs.srv import Trigger

rospy.init_node('jackal_service_client')
rospy.wait_for_service('do_circle')

circle_service = rospy.ServiceProxy('do_circle', Trigger)
result = circle_service()

print(result)
