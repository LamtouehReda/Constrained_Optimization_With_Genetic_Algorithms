from imports import *


def generate_population(size, x_boundaries, y_boundaries):
    lower_x_boundry, upper_x_boundry = x_boundaries
    lower_y_boundry, upper_y_boundry = y_boundaries

    population = []
    for i in range(size):
        individual = {
            "x": random.uniform(lower_x_boundry, upper_x_boundry),
            "y": random.uniform(lower_y_boundry, upper_y_boundry)
        }
        population.append(individual)
    return population



def fitness_function(individual,strObjective,Contraint):
    x = individual['x']
    y = individual['y']
    if Contraint=='':
        return eval(strObjective)
    else:
        penalite=eval(Contraint)
        return eval(strObjective)+penalite


def choice_by_roulette(sorted_population, fitness_sum,strObjective,Contraint):
    offset = 0
    normalized_fitness_sum = fitness_sum

    lowest_fitness = fitness_function(sorted_population[0],strObjective,Contraint)
    if lowest_fitness < 0:
        offset = -lowest_fitness
        normalized_fitness_sum += offset * len(sorted_population)

    draw = random.uniform(0, 1)

    accumulated = 0
    for individual in sorted_population:
        fitness = fitness_function(individual,strObjective,Contraint) + offset
        probability = fitness / normalized_fitness_sum
        accumulated += probability

        if draw <= accumulated:
            return individual


def sort_population_by_fitness(population,strObjective,Contraint):
    return sorted(population,
                  key=(lambda individual : fitness_function(individual,strObjective,Contraint)))


def crossover(individual_a, individual_b):
    return {'x': (individual_a['x'] + individual_b['x']) / 2,
            'y': (individual_b['x'] + individual_b['x']) / 2}


def mutate(individual,XBoundries,YBoundries):
    next_x = individual['x'] + random.uniform(-0.05, 0.05)
    next_y = individual['y'] + random.uniform(-0.05, 0.05)

    Xlower_boundary, Xupper_boundary = XBoundries
    Ylower_boundary, Yupper_boundary = YBoundries

    next_x = min(max(next_x, Xlower_boundary), Xupper_boundary)
    next_y = min(max(next_y, Ylower_boundary), Yupper_boundary)

    return {'x': next_x, 'y': next_y}


def make_next_generation(previous_population,strObjective,XBoundries,YBoundries,Contraint):
    next_generation = []
    sorted_by_fitness_population = sort_population_by_fitness(previous_population,strObjective,Contraint)
    population_size = len(previous_population)
    fitness_sum = sum(fitness_function(individual,strObjective,Contraint) for individual in previous_population)

    for i in range(population_size):
        first_individual_parent = choice_by_roulette(sorted_by_fitness_population, fitness_sum,strObjective,Contraint)
        second_individual_parent = choice_by_roulette(sorted_by_fitness_population, fitness_sum,strObjective,Contraint)

        individual_child = crossover(first_individual_parent, second_individual_parent)

        individual_child = mutate(individual_child,XBoundries,YBoundries)

        next_generation.append(individual_child)

    return next_generation


