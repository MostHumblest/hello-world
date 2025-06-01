from random import choice

class RandomWalk():
    """A class to generate random walk."""

    def __init__(self, num_points=5000):
        """init attributes of walk"""
        self.num_points = num_points

        #all walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """calculate next step"""
        dis_list = [0, 1, 2, 3, 4]
        dir_list = [1, -1]
        direction = choice(dir_list)
        distance = choice(dis_list)
        step = direction * distance

        return step

    def fill_walk(self):
        """calculate walk points"""
        #keep taking steps until desired length
        while len(self.x_values) < self.num_points:
            #Decide which direction to go and how far to go
            x_step = self.get_step()
            y_step = self.get_step()

            #reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    



