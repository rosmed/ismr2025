#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose
from ambf_client import Client
import time

class PoseToAMBF(Node):
    def __init__(self):
        super().__init__('pose_to_ambf')

        # Initialize AMBF
        self.ambf_client = Client()
        self.ambf_client.connect()
        time.sleep(1)  # Give AMBF some time to connect

        self.rigid_body_name = 'volume_anatomical_reference'  # change this to match AMBF object name
        self.body_handle = self.ambf_client.get_obj_handle(self.rigid_body_name)

        # ROS2 subscription
        self.subscription = self.create_subscription(
            Pose,
            '/tumor_transform_topic',
            self.pose_callback,
            10
        )

    def pose_callback(self, msg):
        # Get position (convert from meters to mm or simulation scale)
        pos = (
            msg.position.x * 1000,
            msg.position.y * 1000,
            msg.position.z * 1000
        )

        # Get orientation
        quat = (
            msg.orientation.x,
            msg.orientation.y,
            msg.orientation.z,
            msg.orientation.w
        )

        # Send to AMBF
        print(f"Sending to AMBF: pos={pos}, quat={quat}")
        self.body_handle.set_pos(*pos)
        self.body_handle.set_rot(quat)

def main(args=None):
    rclpy.init(args=args)
    node = PoseToAMBF()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
