import rospy
from std_msgs.msg import String

def user_info_driver():
    publisher = rospy.Publisher("raw_data", String, queue_size=10)
    rospy.init_node("user_info_driver")
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        publisher.publish(String("name: Rose, age: 20, height: 170"))
        rate.sleep()

if __name__ == "__main__":
    user_info_driver()
