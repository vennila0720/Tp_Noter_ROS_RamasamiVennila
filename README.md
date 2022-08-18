# Tp_Noter_ROS_RamasamiVennila
## Installation

Make a git clone of the git repository
sh
https://github.com/vennila0720/Tp_Noter_ROS_RamasamiVennila.git


## Part 1
sh
cd marker_ws
source devel/setup.bash
roscore
rosrun marker_visualiser publish_marker.py /visualization_marker:=/marker_test
rviz


## Part 2
sh

source devel/setup.bash
roscore
rosrun marker_visualiser publish_marker_array.py /visualization_marker:=/space_delimiter
rviz


## Part 3
sh

source devel/setup.bash
roscore
rosrun marker_visualiser randomwalk.py
rviz


## Part 4
sh

source devel/setup.bash
roscore
rosrun marker_visualiser random_walk.py
rviz


On RVIZ click on ADD AND BY TOPIC THEN SELECT THE TOPIC

##Author
RAMASAMI Vennila
