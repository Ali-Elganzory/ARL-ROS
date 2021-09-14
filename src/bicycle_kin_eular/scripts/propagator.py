# Eular discretization for propagation of the kinetic model.

import rospy
from rospy.topics import Subscriber
import math
from bicycle_kin_eular.msg import Reading, State


# Bicycle constants (assumed).
L = 3           # Bicycle length
Lr = 1.5        # CG distance from the rear wheel
delta_t = 0.1   # Sampling time


# State
state = State(0.0, 0.0, 0.0)


def propagate(reading: Reading):
    global state

    beta = math.atan(Lr / L * math.tan(reading.steering_angle))

    x_dot = reading.velocity * math.cos(beta + state.theta)
    y_dot = reading.velocity * math.sin(beta + state.theta)
    theta_dot = reading.velocity / L * math.cos(beta) * math.tan(reading.steering_angle)

    state = State(\
        state.x + delta_t * x_dot, \
        state.y + delta_t * y_dot, \
        state.theta + delta_t * theta_dot \
        )


def propagator():
    rospy.init_node("Propagator")

    subscriber = rospy,Subscriber("Reading", Reading, callback=propagate)

    publisher = rospy.Publisher("State", State, queue_size=10)

    rate = rospy.Rate(1/delta_t)
    while not rospy.is_shutdown():
        publisher.publish(state)
        rate.sleep()

if __name__ == "__main__":
    propagator()