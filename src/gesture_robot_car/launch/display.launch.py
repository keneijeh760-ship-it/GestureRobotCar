
from launch import LaunchDescription
from launch.substitutions import Command, PathJoinSubstitution

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():

    # Locate the robot description file
    xacro_file = PathJoinSubstitution([
        FindPackageShare("gesture_robot_car"),
        "urdf",
        "robot.urdf.xacro"
    ])
    
        # Locate the RViz configuration file
    rviz_config = PathJoinSubstitution([
        FindPackageShare("gesture_robot_car"),
        "config",
        "robot.rviz"
    ])

    # Convert Xacro into a URDF robot description
    robot_description = ParameterValue(
        Command(["xacro ", xacro_file]),
        value_type=str
    )

    return LaunchDescription([

        # Publishes robot links and joints
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            name="robot_state_publisher",
            parameters=[
                {"robot_description": robot_description}
            ]
        ),

        # Allows joint positions to be adjusted
        Node(
            package="joint_state_publisher_gui",
            executable="joint_state_publisher_gui",
            name="joint_state_publisher_gui"
        ),

        # Displays the robot
        Node(
            package="rviz2",
            executable="rviz2",
            name="rviz2",
            arguments=["-d", rviz_config]
        )

    ])
