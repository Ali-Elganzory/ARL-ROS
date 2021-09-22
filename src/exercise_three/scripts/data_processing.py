import rospy
from std_msgs.msg import String
from exercise_three.msg import UserInfo


user_info_pub = rospy.Publisher("user_info", UserInfo, queue_size=10)


def process_clbk(raw_data: String):
    name, age, height = map(lambda x: x.split(": ")[1], raw_data.data.split(", "))
    age = int(age)
    height = int(height)
    user_info_pub.publish(UserInfo(name, age, height))


def data_processing():
    rospy.init_node("data_processing")
    subscriber = rospy.Subscriber("raw_data", String, process_clbk)
    rospy.spin()



if __name__ == "__main__":
    data_processing()
