
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, PathJoinSubstitution

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():

    # Locate the robot description
    xacro_file = PathJoinSubstitution([
        FindPackageShare("gesture_robot_car"),
        "urdf",
        "robot.urdf.xacro"
    ])

    # Convert Xacro into a URDF description
    robot_description = ParameterValue(
        Command(["xacro ", xacro_file]),
        value_type=str
    )

    # Locate our Gazebo world
    world_file = PathJoinSubstitution([
        FindPackageShare("gesture_robot_car"),
        "worlds",
        "test_world.sdf"
    ])

    # Locate Gazebo's launch file
    gazebo_launch_file = PathJoinSubstitution([
        FindPackageShare("ros_gz_sim"),
        "launch",
        "gz_sim.launch.py"
    ])

    # Start Gazebo
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(gazebo_launch_file),
        launch_arguments={
            "gz_args": ["-r ", world_file]
        }.items()
    )

    # Publish the robot description
    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        name="robot_state_publisher",
        parameters=[
            {"robot_description": robot_description}
        ],
        output="screen"
    )

    # Spawn the robot inside Gazebo
    spawn_robot = Node(
        package="ros_gz_sim",
        executable="create",
        arguments=[
            "-name", "gesture_robot",
            "-topic", "robot_description",
            "-x", "0",
            "-y", "0",
            "-z", "0.0375"
        ],
        output="screen"
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        TimerAction(
            period=5.0,
            actions=[spawn_robot]
        )
    ])
