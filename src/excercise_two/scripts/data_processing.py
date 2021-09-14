import rospy
from std_msgs.msg import String


def process_clbk(raw_data: String):
    name, age, height = map(lambda x: x.split(": ")[1], raw_data.data.split(", "))
    age = int(age)
    height = int(height)
    rospy.loginfo(f"\nname: {name}\nage: {age}\nheight: {height}")


def data_processing():
    rospy.init_node("data_processing")
    subscriber = rospy.Subscriber("raw_data", String, process_clbk)
    rospy.spin()



if __name__ == "__main__":
    data_processing()
