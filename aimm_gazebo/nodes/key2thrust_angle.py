#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32
import math
import numpy
import sys
import termios

# Instructions to guide the user
instructions = """
Reading from the keyboard and Publishing Thrust Angles!
---------------------------
Change Thrust Angle clockwise: a
Change Thrust Angle counter-clockwise: d

r/v : increase/decrease thruster angle change speed by 10%

CTRL-C to quit
"""

# Dictionary for controlling thrust angle
moveBindings = {
    'a': -1,  # Clockwise rotation
    'd': 1,   # Counter-clockwise rotation
}

# Dictionary for adjusting the speed of angle change
speedBindings = {
    'r': 1,   # Increase speed
    'v': -1,  # Decrease speed
}

# Function to get a character from the keyboard
def __gen_ch_getter(echo):
    def __fun():
        fd = sys.stdin.fileno()
        oldattr = termios.tcgetattr(fd)
        newattr = oldattr[:]
        try:
            if echo:
                lflag = ~(termios.ICANON | termios.ECHOCTL)
            else:
                lflag = ~(termios.ICANON | termios.ECHO)
            newattr[3] &= lflag
            termios.tcsetattr(fd, termios.TCSADRAIN, newattr)
            ch = sys.stdin.read(1)
            if echo and ord(ch) == 127:  # Handle backspace
                sys.stdout.write('\b \b')
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, oldattr)
        return ch
    return __fun

if __name__ == "__main__":
    # Setup getch function to capture keypresses
    getch = __gen_ch_getter(False)

    # Setup ROS publishers and node
    mid_pub = rospy.Publisher('/lpv/thrusters/mid_thrust_angle', Float32, queue_size=1)
    rospy.init_node('key2thrust_angle')

    # Initialize current angle and angle speed
    thrust_angle_speed = 0.1  # Default speed for changing the thrust angle
    max_angle = rospy.get_param("~max_angle", math.pi / 2)  # Max allowable angle for yaw control
    curr_angle = 0  # Start with a zero-degree angle
    num_prints = 0  # Counter for reprinting instructions

    try:
        # Output instructions and max angle info
        print(instructions)
        print(f'Max Angle: {max_angle}')

        while True:
            # Read the pressed key
            key = getch()

            # Check if the key is for changing the angle (yaw control)
            if key in moveBindings.keys():
                # Adjust the current angle within the allowed range
                curr_angle += thrust_angle_speed * moveBindings[key]
                curr_angle = numpy.clip(curr_angle, -max_angle, max_angle).item()
                print(f'Current thrust angle: {curr_angle}')

            # Check if the key is for adjusting the speed of angle change
            elif key in speedBindings.keys():
                # Adjust the speed of angle change
                thrust_angle_speed += speedBindings[key] * 0.1 * thrust_angle_speed
                print(f'Updated thrust angle change speed: {thrust_angle_speed:.2f}')

                # Print instructions after a certain number of speed changes
                if num_prints == 14:
                    print(instructions)
                num_prints = (num_prints + 1) % 15

            # Exit if CTRL-C is pressed
            elif key == '\x03':
                break

            # Publish the current thrust angle (yaw angle) to the mid-thruster
            angle_msg = Float32()
            angle_msg.data = curr_angle
            mid_pub.publish(angle_msg)

    except Exception as e:
        print(f'Error: {e}')

    finally:
        # Reset the thrust angle to 0 when exiting
        angle_msg = Float32()
        angle_msg.data = 0
        mid_pub.publish(angle_msg)
        print("Thrust angle reset to 0")
