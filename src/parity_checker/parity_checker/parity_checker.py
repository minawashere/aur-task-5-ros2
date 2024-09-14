#!/usr/bin/env python3

import rclpy
from rclpy.node import Node


class Parity_checker(Node):

    def __init__(self):
        super().__init__('parity_checker_node')
        self.time = 0;
        self.rate = 0.0 
        self.rate = self.create_timer(1.0, self.print_result_callback)

    def print_result_callback(self):
        self.time += 1
        self.result = "Even" if self.time % 2 == 0 else "Odd"
        self.get_logger().info(self.result)

def main(args = None):
    rclpy.init(args = args)
    parity_checker_node = Parity_checker() 
    rclpy.spin(parity_checker_node)

if __name__ == '__main__':
    main()
