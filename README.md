# simple-navigation-goals
This is a simple navigation with multiple goals for rb1-base mobile robot with elevator control

1)After accessing to robot graphical interface using http://192.168.0.200/xxxx , activate mapping

2)After map construction name this map and check use this map by default

3)Activate in order map_server,localization and navigation (All thses steps could be done with terminal:gmapping,amcl,move_base 4)Clone this repository to your workspace then:

4.1)catkin_make

4.2)rosrun simple_navigation_goals simple_navigation_goals

(goals were chosen with rostopic echo /rb1_base/amcl_pose)
