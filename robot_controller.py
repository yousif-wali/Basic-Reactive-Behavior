from controller import Robot, Motor
import numpy as np

# Constants
TIME_STEP = 64
MAX_SPEED = 3.14
FIVE_CM_THRESHOLD = 306  # 5 cm converted to normalized range

# Create the Robot instance
robot = Robot()

# Initialize motors
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Set motors to velocity mode
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
# Helper function to initialize sensors
def initialize_sensors(sensor_prefix, count):
    sensors = []
    for i in range(count):
        sensor = robot.getDevice(f"{sensor_prefix}{i}")
        sensor.enable(TIME_STEP)
        sensors.append(sensor)
    return sensors

# Initialize distance sensors
distance_sensors = initialize_sensors('ps', 8)

# Function to get normalized sensor values
def normalize_sensor_values(sensors):
    values = np.asarray([sensor.getValue() for sensor in sensors])
    return values

def set_speed(left_motor_speed, right_motor_speed):
    left_motor.setVelocity(left_motor_speed)
    right_motor.setVelocity(right_motor_speed)
 
def max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
# Robot state
state = 'FOLLOW'
rotation_start_time = None
performed_180 = False
performed_90 = False
# Main control loop
while robot.step(TIME_STEP) != -1:
    # Read and normalize sensor values
    distance_values = normalize_sensor_values(distance_sensors)

    # Detect obstacle
    object_detected = max(distance_values[0],distance_values[7]) > FIVE_CM_THRESHOLD

    left_tire, right_tire = MAX_SPEED, MAX_SPEED

    if state == 'FOLLOW':
        # Adjust speed based on front sensors
        set_speed(MAX_SPEED, MAX_SPEED)
        
        if distance_values[5] < FIVE_CM_THRESHOLD and performed_90:
            set_speed(0,0)
        # If an object is detected within 5 cm, rotate 180 degrees
        if object_detected:
            rotation_start_time = robot.getTime()
            if performed_180:
                state = 'ROTATE90'
            else:
                state = 'ROTATE180'

    elif state == 'ROTATE180':
        # Perform 180-degree rotation
        set_speed(-MAX_SPEED, MAX_SPEED)
        

        # Rotate for ~2 seconds (adjust based on testing)
        if robot.getTime() - rotation_start_time > 1.5:
            performed_180 = True
            state = 'FOLLOW'
            

    elif state == 'ROTATE90':

        # Perform 90-degree rotation
        set_speed(MAX_SPEED, -MAX_SPEED)
        

        # Rotate for ~2 seconds (adjust based on testing)
        if robot.getTime() - rotation_start_time > 0.75:
            state = 'FOLLOW'
            performed_90 = True
            
    print("State: " + state)
    print(distance_values)
    # Set motor velocities
