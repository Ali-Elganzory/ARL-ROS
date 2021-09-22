import rospy
from std_msgs.msg import String, Int32, Float32


name_pub = rospy.Publisher("name", String, queue_size=10)
age_pub = rospy.Publisher("age", Int32, queue_size=10)
height_pub = rospy.Publisher("height", Float32, queue_size=10)


def process_clbk(raw_data: String):
    name, age, height = map(lambda x: x.split(": ")[1], raw_data.data.split(", "))
    age = int(age)
    height = int(height)
    name_pub.publish(String(name))
    age_pub.publish(Int32(age))
    height_pub.publish(Float32(height))


def data_processing():
    rospy.init_node("data_processing")
    subscriber = rospy.Subscriber("raw_data", String, process_clbk)
    rospy.spin()



if __name__ == "__main__":
    data_processing()
