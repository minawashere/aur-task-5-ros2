import random 
import rclpy
from rclpy.node import Node

class Data_collector(Node):
    def __init__(self):
        super().__init__('weather_data_collector')
        self.pressure = None
        self.humidity = None
        self.temperature = None
        self.rate = self.create_timer(1, self.collect_weather_data)

    def collect_weather_data(self):
        self.temperature = random.randint(-40, 70)
        self.humidity = random.random() # percentage
        self.pressure = random.uniform(950, 1050)
        self.
        ()

    def print_data(self):
        msg = f'\nTemperature: \t{self.temperature}\nHumidity: \t{self.humidity}\nPressure: \t{self.pressure}\n'
        self.get_logger().info(msg)



def main(args = None):
    rclpy.init(args = args)
    weather_data_collector = Data_collector()
    rclpy.spin(weather_data_collector)

if __name__ == '__main__':
    main()
