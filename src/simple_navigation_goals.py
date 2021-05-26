#!/usr/bin/env python
# license removed for brevity

import rospy, actionlib, tf
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

import time
from robotnik_msgs.srv import SetElevator
def movebase_position1():
    client = actionlib.SimpleActionClient('/rb1_base/move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "rb1_base_map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x=0.0
    goal.target_pose.pose.position.y=0.0
    goal.target_pose.pose.position.z=0.0
    goal.target_pose.pose.orientation.x= 0.0
    goal.target_pose.pose.orientation.y=0.0
    goal.target_pose.pose.orientation.z=0.0
    goal.target_pose.pose.orientation.w=1.0
 
    
    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()
def movebase_position2():

    client = actionlib.SimpleActionClient('/rb1_base/move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "rb1_base_map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x=1.6073192894
    goal.target_pose.pose.position.y=1.68095123465
    goal.target_pose.pose.position.z=0.0
    goal.target_pose.pose.orientation.x= 0.0
    goal.target_pose.pose.orientation.y=0.0
    goal.target_pose.pose.orientation.z=0.713743641216
    goal.target_pose.pose.orientation.w=0.700407034962
    
    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()
def movebase_position3():

    client = actionlib.SimpleActionClient('/rb1_base/move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "rb1_base_map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x=1.57880866022
    goal.target_pose.pose.position.y=3.38836865759
    goal.target_pose.pose.position.z=0.0
    goal.target_pose.pose.orientation.x= 0.0
    goal.target_pose.pose.orientation.y=0.0
    goal.target_pose.pose.orientation.z=0.998604212364
    goal.target_pose.pose.orientation.w=0.0528169200949

    
    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()
def movebase_position4():

    client = actionlib.SimpleActionClient('/rb1_base/move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "rb1_base_map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x=-0.067090015019
    goal.target_pose.pose.position.y=2.96559839933
    goal.target_pose.pose.position.z=0.0
    goal.target_pose.pose.orientation.x= 0.0
    goal.target_pose.pose.orientation.y=0.0
    goal.target_pose.pose.orientation.z=-0.756153179779
    goal.target_pose.pose.orientation.w= 0.654394658223

    
    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()
def elevator_up():
    rospy.wait_for_service('/rb1_base/robotnik_base_control/set_elevator')
    srv=rospy.ServiceProxy('/rb1_base/robotnik_base_control/set_elevator',SetElevator)
    req=SetElevator()
    req.action=1
    srv(req)
def elevator_down():
    rospy.wait_for_service('/rb1_base/robotnik_base_control/set_elevator')
    srv=rospy.ServiceProxy('/rb1_base/robotnik_base_control/set_elevator',SetElevator)
    req=SetElevator()
    req.action=-1
    srv(req)
    
if __name__ == '__main__':
    try:
	
	
    rospy.init_node('test_nav')
	result = elevator_down()
    result = movebase_position1()
	result = movebase_position2()
	result = movebase_position3()
	time.sleep(3)
	result = elevator_up()
	#It is necessary for the service this delay
	time.sleep(8)
	result = movebase_position4()
	result = movebase_position1()
	time.sleep(3)
	result = elevator_down()
	time.sleep(8)

        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
