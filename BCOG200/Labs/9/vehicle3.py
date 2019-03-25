import math
import random
import turtle

'''
    Modify this program in the following ways:
        - Add at least 1 more class representing another kind of input other 
        than heat.
        - Have the input_list contain multiple kinds of input sources.
        - Use custom images for each input sources
        - Modify vehicle 3 so that it has an 'innate preference' or 'innate 
        dislike' of each kind of input 
'''


class HeatSource(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self, visible=False)
        self.shape('circle')
        self.penup()
        self.color(255, 190, 60)
        self.goto(random.randint(-200, 0), random.randint(-200, 0))
        self.showturtle()
        self.type = 'heat'


class ColdSource(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self, visible=False)
        turtle.Turtle.__init__(self, visible=False)
        self.shape('circle')
        self.penup()
        self.color(60, 255, 190)
        self.goto(random.randint(0, 200), random.randint(0, 200))
        self.showturtle()
        self.type = 'cold'


class Vehicle3(turtle.Turtle):

    def __init__(self, input_list, vehicle_id, vehicle_type):
        turtle.Turtle.__init__(self, visible=False)
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.input_list = input_list
        self.create_vehicle()
        self.speed_parameters = [20, 0.2, 6]
        self.turn_parameters = [20]
        self.moves = 0
        self.distance_weights = {'heat': [0, 1], 'cold': [1, 0]}

    def create_vehicle(self):
        self.shape('turtle')
        self.turtlesize(1)
        self.penup()
        if self.vehicle_type == 'crossed':
            self.color(random.randint(0, 150), random.randint(0, 150), 255)
        else:
            self.color(255, random.randint(0, 150), random.randint(0, 150))
        self.goto(random.randint(-290, 290), random.randint(-290, 290))
        self.right(random.randint(0, 360))
        self.pendown()
        self.showturtle()

    def get_input_information(self, position):
        input_distance = self.distance(position)
        input_angle = self.heading() - self.towards(position)
        return input_distance, input_angle

    def get_sensor_distances(self, distance, angle):
        sin_angle = math.sin(math.radians(angle))
        left_distance = distance - sin_angle
        right_distance = distance + sin_angle
        return left_distance, right_distance

    def compute_speed(self, left_distance, right_distance, source_type):
        left_weight, right_weight = self.distance_weights[source_type]
        if self.vehicle_type == 'crossed':
            left_speed = ((self.speed_parameters[0] /
                           ((right_distance * left_weight
                             + left_distance * right_weight)
                            ** self.speed_parameters[1]))
                          - self.speed_parameters[2])
            right_speed = ((self.speed_parameters[0] /
                            ((right_distance * right_weight
                              + left_distance * left_weight)
                             ** self.speed_parameters[1]))
                           - self.speed_parameters[2])
        else:
            right_speed = ((self.speed_parameters[0] /
                            ((right_distance * left_weight
                              + left_distance * right_weight)
                             ** self.speed_parameters[1]))
                           - self.speed_parameters[2])
            left_speed = ((self.speed_parameters[0] /
                           ((right_distance * right_weight
                             + left_distance * left_weight)
                            ** self.speed_parameters[1]))
                          - self.speed_parameters[2])
        combined_speed = (left_speed + right_speed) / 2
        return left_speed, right_speed, combined_speed

    def compute_turn_amount(self, left_speed, right_speed):
        turn_amount = self.turn_parameters[0] * (right_speed - left_speed)
        return turn_amount

    def move(self):
        combined_speed = 0
        combined_turn_amount = 0

        for current_input in self.input_list:
            input_distance, input_angle = self.get_input_information(
                current_input.position())
            left_distance, right_distance = self.get_sensor_distances(
                input_distance, input_angle)
            left_speed, right_speed, average_speed = self.compute_speed(
                left_distance, right_distance, current_input.type)
            turn_amount = self.compute_turn_amount(left_speed, right_speed)
            combined_turn_amount += turn_amount
            combined_speed += average_speed

        try:
            self.right(combined_turn_amount)
        except:
            print(combined_turn_amount)
        self.forward(combined_speed)
        self.moves += 1


def create_screen():
    wn = turtle.Screen()
    wn.colormode(255)
    wn.setup(1200, 800)
    wn.title("Vehicle 3")
    wn.tracer(0, 0)
    return wn


def main():
    wn = create_screen()
    num_vehicles = 5
    num_heat_sources = 2
    num_cold_sources = 2

    vehicle_list = []
    input_list = []

    for i in range(num_heat_sources):
        input_list.append(HeatSource())

    for i in range(num_cold_sources):
        input_list.append(ColdSource())

    for i in range(num_vehicles):
        vehicle_list.append(
            Vehicle3(input_list, i, random.choice(["crossed", "direct"])))

    wn.update()
    while True:
        for j in range(num_vehicles):
            vehicle_list[j].move()
        wn.update()


if __name__ == '__main__':
    main()
