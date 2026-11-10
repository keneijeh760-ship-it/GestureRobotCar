
cmake_minimum_required(VERSION 3.8)

project(gesture_robot_car)

find_package(ament_cmake REQUIRED)

# Install robot description and simulation resources
install(
    DIRECTORY
        urdf
        worlds
        launch
        config
    DESTINATION share/${PROJECT_NAME}
)

ament_package()
