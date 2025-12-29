import os

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        Node(
            package='rplidar_ros',
            executable='rplidar_composition',
            output='screen',
            parameters=[{
                # Change serial_port
                'serial_port': '/dev/serial/by-path/platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.3:1.0-port0',
                # Change frame_id
                'frame_id': 'laser_frame',
                'angle_compensate': True,
                # Change scan_mode
                'scan_mode': 'Standard'
            }]
        )
    ])