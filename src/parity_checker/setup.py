from setuptools import find_packages, setup

package_name = 'parity_checker'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lolo',
    maintainer_email='minasalama2580@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'parity_checker_node = parity_checker.parity_checker:main',
            'weather_data_collector = parity_checker.data_collector:main',
        ],
    },
)
