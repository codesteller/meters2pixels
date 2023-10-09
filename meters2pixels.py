import math

def height_in_pixels(distance, fov, person_height, sensor_height, image_height):
    return (2 * distance * math.tan(fov/2)) / (person_height * sensor_height / image_height)

distance = 75 # meters
fov = math.radians(90) # degrees to radians
person_height = 1.7 # meters
sensor_height = 4.8 # mm
image_height = 1080 # pixels

height_in_px = height_in_pixels(distance, fov, person_height, sensor_height, image_height)
print(f"A person who is {person_height} meters tall would appear to be approximately {height_in_px:.0f} pixels tall in a 2MP digital image taken from a distance of {distance} meters with a 90-degree field of view.")
