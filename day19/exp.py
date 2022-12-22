import numpy as np
import time
fname = "test.txt"

def set_costs(line):
    costs = [ [0]*4 for _ in range(4)]
    recipes = line[13:].split(".")
    for i in range(4):
        recipe = recipes[i]
        words = recipe.split()

        ingredients = "".join([word + " " for word in words[words.index("costs")+1:]])

        names = ["ore","clay","obsidian"]
        splitwords = ingredients.split()
        for j in range(3):
            if names[j] in splitwords:
                costs[i][j] = int(splitwords[splitwords.index(names[j]) - 1])
    return costs
"""
this is a very inefficient solution
"""
def recursive(minutes_left, robots, resources, recipes):
    if minutes_left == 0:
        return resources[-1]
    else:
        wait = 0
        new_robots = set()
        new_robots.add(tuple(robots))
        stack = [robots]
        best = wait
        while stack != []:
            current = stack.pop()
            remaining_resources = resources - np.matmul(current - robots,recipes)
            for i in range(len(recipes)):
                reqs = recipes[i]
                hasEnough = (remaining_resources >= reqs).all()
                if hasEnough:
                    next_robot = robots + np.array([j == i for j in range(len(recipes))])
                    if tuple(next_robot) not in new_robots:
                        stack.append(next_robot)
                        new_robots.add(tuple(next_robot))

            best = max(wait, recursive(minutes_left - 1, current, remaining_resources + robots, recipes))
        return best
"""
This is MUCH faster, but still not perfect
"""
def withmemo(minutes_left, robots, resources, recipes):
    key = tuple([minutes_left] + list(robots) + list(resources))
    if key in memo:
        return memo[key]
    else:
        if minutes_left == 0:
            return resources[-1]
        wait = 0
        new_robots = set()
        new_robots.add(tuple(robots))
        stack = [robots]
        best = wait
        while stack != []:
            current = stack.pop()
            remaining_resources = resources - np.matmul(current - robots,recipes)
            for i in range(len(recipes)):
                reqs = recipes[i]
                hasEnough = (remaining_resources >= reqs).all()
                if hasEnough:
                    next_robot = robots + np.array([j == i for j in range(len(recipes))])
                    if tuple(next_robot) not in new_robots:
                        stack.append(next_robot)
                        new_robots.add(tuple(next_robot))

            best = max(wait, withmemo(minutes_left - 1, current, remaining_resources + robots, recipes))
        memo[key] = best
        return best           

time_limit = 3 # actually 24 but lowered for testing purposes
print(time_limit)
f = open(fname)

lines = f.readlines()
f.close()
scores = []
times = []
memo = dict()
ORE,CLAY,OBSIDIAN, GEODE = range(4)

recipe = set_costs(lines[0])
f = open("test_data.txt")
data = f.readlines()
f.close()

minutes = []
robot_init = []
resource_init = []
answers = []
final_minutes = []

for line in data:
    words = line.split("#")
    minutes.append(eval(words[0]))
    robot_init.append(eval(words[1]))
    resource_init.append(eval(words[2]))
    answers.append(eval(words[3]))
    final_minutes.append(eval(words[4]))
print(len(data))
for i in range(-5,0):
    memo = dict()
    print(f"expected: {recursive(final_minutes[i] - minutes[i], np.array(robot_init[i]), np.array(resource_init[i]), np.array(recipe))}, accepted: {answers[i]}")


