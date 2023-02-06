import time

def automatic_door_opening_system(sensor_value):
    # Define the threshold for door opening
    threshold = 100

    # Check if the sensor value is greater than the threshold
    if sensor_value > threshold:
        print("Opening door...")
        # Simulate door opening process
        time.sleep(2)
        print("Door opened.")
        return True
    else:
        print("Door remains closed.")
        return False

# Example usage
sensor_value = 150
automatic_door_opening_system(sensor_value)
