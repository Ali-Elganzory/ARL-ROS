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

def search_target_index(self, state):
    global old_nearest_point_index
    # To speed up nearest point search, doing it at only first time.
    if self.old_nearest_point_index is None:
        # search nearest point index
        d = np.hypot(*zip(*path))
        ind = np.argmin(d)
        self.old_nearest_point_index = ind
    else:
        ind = self.old_nearest_point_index
        distance_this_index = state.calc_distance(self.cx[ind],
                                                    self.cy[ind])
        while True:
            distance_next_index = state.calc_distance(self.cx[ind + 1],
                                                        self.cy[ind + 1])
            if distance_this_index < distance_next_index:
                break
            ind = ind + 1 if (ind + 1) < len(self.cx) else ind
            distance_this_index = distance_next_index
        self.old_nearest_point_index = ind

    Lf = k * state.v + Lfc  # update look ahead distance

    # search look ahead target point index
    while Lf > state.calc_distance(self.cx[ind], self.cy[ind]):
        if (ind + 1) >= len(self.cx):
            break  # not exceed goal
        ind += 1

    return ind, Lf


def control(state: State):
    global publisher
    ld = Kdd * velocity
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