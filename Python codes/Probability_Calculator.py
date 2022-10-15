import copy
import random
class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for _ in range(value):
        self.contents.append(key)

  def draw(self, number):
    if number > len(self.contents):
      return self.contents
    balls = []
    for _ in range(number):
      choice = random.randrange(len(self.contents))
      balls.append(self.contents.pop(choice))
    return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  expected_no_of_balls = []
  for key in expected_balls:
      expected_no_of_balls.append(expected_balls[key])
  successes = 0

  for _ in range(num_experiments):
    new_hat = copy.deepcopy(hat)
    balls = new_hat.draw(num_balls_drawn)

    no_of_balls = []
    for key in expected_balls:
      no_of_balls.append(balls.count(key))

    if no_of_balls >= expected_no_of_balls:
      successes += 1

  return successes/num_experiments
  
hat = Hat(blue=4, red=2, green=6)
probability =experiment(hat=hat,expected_balls={"blue": 2,"red": 1},num_balls_drawn=4,num_experiments=3000)
print("Probability:{0:.4f}".format(probability))
