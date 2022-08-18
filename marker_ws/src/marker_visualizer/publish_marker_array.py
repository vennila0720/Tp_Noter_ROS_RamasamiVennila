#!/usr/bin/env python3

import roslib; roslib.load_manifest('visualization_marker_tutorials')
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
from geometry_msgs.msg import Point
import rospy
import math


publisher = rospy.Publisher(topic, MarkerArray, queue_size = 10)
publisher_line = rospy.Publisher('/vis_marker', Marker, queue_size=3)


rospy.init_node('register')

markerArray = MarkerArray()



while not rospy.is_shutdown():

   marker = Marker()
   marker.header.frame_id = "map"
   marker.type = marker.SPHERE
   marker.action = marker.ADD
   marker.scale.x = 0.5
   marker.scale.y = 0.5
   marker.scale.z = 0.5
   marker.color.a = 1
   marker.color.r = 0.1
   marker.color.g = 0.1
   marker.color.b = 0.8
   marker.pose.orientation.w = 1.0
   marker.pose.position.x = 5
   marker.pose.position.y = 2
   marker.pose.position.z = 0 

   # We add the new marker to the MarkerArray, removing the oldest
   # marker from it when necessary
  



   secound_marker = Marker()
   secound_marker.header.frame_id = "map"
   secound_marker.type = marker.SPHERE
   secound_marker.action = marker.ADD
   secound_marker.scale.x = 0.5
   secound_marker.scale.y = 0.5
   secound_marker.scale.z = 0.5
   secound_marker.color.a = 1.0
   secound_marker.color.r = 0.1
   secound_marker.color.g = 0.1
   secound_marker.color.b = 0.8
   secound_marker.pose.orientation.w = 1
   secound_marker.pose.position.x = 5
   secound_marker.pose.position.y = 3
   secound_marker.pose.position.z = 0 


   third_marker = Marker()
   third_marker.header.frame_id = "map"
   third_marker.type = marker.SPHERE
   third_marker.action = marker.ADD
   third_marker.scale.x = 0.5
   third_marker.scale.y = 0.5
   third_marker.scale.z = 0.5
   third_marker.color.a = 1.0
   third_marker.color.r = 0.1
   third_marker.color.g = 0.1
   third_marker.color.b = 0.8
   third_marker.pose.orientation.w = 1
   third_marker.pose.position.x = 4
   third_marker.pose.position.y = 2
   third_marker.pose.position.z = 0



   fourth_marker = Marker()
   fourth_marker.header.frame_id = "map"
   fourth_marker.type = marker.SPHERE
   fourth_marker.action = marker.ADD
   fourth_marker.scale.x = 0.5
   fourth_marker.scale.y = 0.5
   fourth_marker.scale.z = 0.5
   fourth_marker.color.a = 1.0
   fourth_marker.color.r = 0.1
   fourth_marker.color.g = 0.1
   fourth_marker.color.b = 0.8
   fourth_marker.pose.orientation.w = 1
   fourth_marker.pose.position.x = 4
   fourth_marker.pose.position.y = 3
   fourth_marker.pose.position.z = 0 
 




  
   line = Marker()
   line.header.frame_id = 'map'

   line.action = Marker.ADD

   line.header.stamp = rospy.Time.now()
   line.id = 1

   line.type = Marker.LINE_STRIP

   line.color.a = 1
   line.color.g = 1
   line.color.r = line.color.b = 0



   line.pose.position.x = 4
   line.pose.position.y = 2
   line.pose.position.z = 0
   line.pose.orientation.w = 1

   line.pose.orientation.x = line.pose.orientation.y = line.pose.orientation.z = 0
   line.scale.x = line.scale.y = 0.1
   line.scale.z = 0.05


   line.points.append(Point(0,0,0))
   line.points.append(Point(0,1,0))
   line.points.append(Point(1,1,0))
   line.points.append(Point(1,0,0))
   line.points.append(Point(0,0,0))


   markerArray.markers.append(marker)
   markerArray.markers.append(secound_marker)
   markerArray.markers.append(third_marker)
   markerArray.markers.append(fourth_marker)

   # Renumber the marker IDs
   id = 0

   for m in markerArray.markers:
       m.id = id
       id += 1

   # Publish the MarkerArray
   publisher.publish(markerArray)
   publisher_line.publish(line)

   

   rospy.sleep(0.01)
