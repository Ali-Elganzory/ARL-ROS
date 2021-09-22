import rospy
from rospy.topics import Subscriber
import math
import numpy as np

from bicycle_kin_eular.msg import Reading, State

# Bicycle constants (assumed).
L = 3           # Bicycle length
delta_t = 0.1   # Sampling time
Kdd = 1.5       # Kdd
velocity = 10   # Vf

state = State(0.0, 0.0, 0.0)
path = [(x, 3 * math.sin(x / 2)) for x in range(0, 200, 0.2)]


publisher = rospy.Publisher("Reading", State, queue_size=10)

old_nearest_point_index = None

def search_target_index():
    global state, old_nearest_point_index

    ld = Kdd * velocity

    # To speed up nearest point search, doing it at only first time.
    if old_nearest_point_index is None:
        # search nearest point index
        d = np.hypot(*zip(*path))
        ind = np.argmin(d)
        old_nearest_point_index = ind
    else:
        ind = old_nearest_point_index
        distance_this_index = state.calc_distance(*path[ind])
        while True:
            distance_next_index = state.calc_distance(*path[ind + 1])
            if distance_this_index < distance_next_index:
                break
            ind = ind + 1 if (ind + 1) < len(path) else ind
            distance_this_index = distance_next_index
        old_nearest_point_index = ind

    # search look ahead target point index
    while ld > state.calc_distance(*path[ind]):
        if (ind + 1) >= len(path):
            break  # not exceed goal
        ind += 1

    return ind, ld


def control(state: State):
    global publisher
    path[]

    publisher.publish(reading)


def controller():
    rospy.init_node("Controller")

    subscriber = rospy,Subscriber("State", Reading, callback=control)

    # rate = rospy.Rate(1/delta_t)
    # while not rospy.is_shutdown():
    #     publisher.publish(reading)
    #     rate.sleep()


if __name__ == "__main__":
    controller()