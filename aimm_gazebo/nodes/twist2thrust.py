#!/usr/bin/env python3
# license removed for brevity

import sys
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32
from aimm_gazebo.srv import BallShooter
from std_msgs.msg import Empty

class Node():
    def __init__(self, linear_scaling, keyboard=False):
        self.linear_scaling = linear_scaling
        self.mid_pub = None
        self.mid_msg = None
        self.keyboard = keyboard
        self.shooter_pub = None

    def callback(self, data):
        rospy.logdebug("RX: Twist " + rospy.get_caller_id())
        rospy.logdebug("\tlinear: x: %f, y: %f, z: %f" % (data.linear.x, data.linear.y, data.linear.z))

        # Apply scaling factors for linear movement
        linfac = self.linear_scaling

        # Handle linear movement (forward/backward)
        linear_velocity = linfac * data.linear.x
        self.mid_msg.data = linear_velocity
        rospy.logdebug("TX mid (linear): %f" % self.mid_msg.data)
        self.mid_pub.publish(self.mid_msg)

    def handle_ball_shooter(self, req):
        self.shooter_pub.publish()
        return True

if __name__ == '__main__':
    rospy.init_node('twist2drive', anonymous=True)

    # ROS Parameters for linear scaling
    linear_scaling = rospy.get_param('~linear_scaling', 0.2)  # Linear scaling

    rospy.loginfo("Linear scaling=%f" % linear_scaling)

    key = '--keyboard' in sys.argv
    node = Node(linear_scaling, keyboard=key)

    # Publisher for the mid-thruster (linear control)
    node.mid_pub = rospy.Publisher("/lpv/thrusters/mid_thrust_cmd", Float32, queue_size=10)
    node.mid_msg = Float32()

    # Subscriber for the Twist messages (cmd_vel)
    rospy.Subscriber("cmd_vel", Twist, node.callback)

    # Service - adds functionality to shoot via joystick
    sub = rospy.Service('ball_shooter', BallShooter, node.handle_ball_shooter)
    node.shooter_pub = rospy.Publisher("/lpv/shooters/ball_shooter/fire", Empty, queue_size=1)

    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
