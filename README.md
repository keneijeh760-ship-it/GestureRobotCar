# Gesture-Controlled Robot Car

A four-wheel robot car simulation project using ROS 2 and Gazebo.

## Project Overview

The project aims to simulate a robot car controlled through hand gestures.

The physical design consists of:

- Arduino Uno receiver
- Arduino Nano transmitter
- MPU6050 accelerometer and gyroscope
- NRF24L01 wireless communication modules
- L298N motor driver
- Four-wheel robot chassis

## Simulation Technology

- ROS 2 Jazzy
- Gazebo Harmonic
- URDF / Xacro
- SDF
- RViz

## Project Structure

```text
GestureRobotCar/
├── src/
│   └── gesture_robot_car/
│       ├── urdf/
│       ├── meshes/
│       ├── worlds/
│       ├── launch/
│       ├── config/
│       └── scripts/
├── docs/
└── README.md