class Robot:
    MAX_ENERGY = 100

    def __init__(self):
        self.name = "Robot"
        self.age = 0
        self.energy = 0

    def display(self):
        print(f"I am {self.name}")

    def __repr__(self):
        return f'Robot(name={self.name!r}, age={self.age}, energy={self.energy})'

    def __str__(self):
        return f'Robot {self.name} is {self.age} years old with {self.energy} energy.'

    # Increases age by 1
    def grow(self):
        self.age += 1

    # Increases energy by 'amount', but not above MAX_ENERGY
    def eat(self, amount):
        self.energy += amount
        if self.energy > Robot.MAX_ENERGY:
            self.energy = Robot.MAX_ENERGY

    # Reduces energy by 'distance', but not below 0
    def move(self, distance):
        self.energy -= distance
        if self.energy < 0:
            self.energy = 0

if __name__ == "__main__":
    robot = Robot()
    robot.display()
    print(str(robot))
    robot.grow()
    robot.eat(80)
    robot.move(30)
    print(repr(robot))