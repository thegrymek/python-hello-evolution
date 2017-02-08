import argparse
import functools
import math
import random
import string


letters = ''.join([
    string.ascii_letters,
    string.digits,
    string.printable,
    string.punctuation
])


def random_character():
    return random.choice(letters)


def fitness(child, target_string):
    diff = [
        math.fabs(ord(child[i]) - ord(target_string[i]))
        for i in range(len(child))
    ]
    return sum(diff)


def create_child(length):
    random_string_iterable = [random_character()
                              for _ in range(length)]
    random_string = ''.join(random_string_iterable)
    return random_string


def create_population(population_length, child_length):
    population = [create_child(child_length)
                  for _ in range(population_length)]
    return population


def crossover(child1, child2, locus):
    new_child1 = child1[:locus] + child2[locus:]
    new_child2 = child2[:locus] + child1[locus:]
    return new_child1, new_child2


def mutation(child, pos):
    char = random_character()
    child = child[:pos] + char + child[pos + 1:]
    return child


def run(target_string, population_length):
    fitness_func = functools.partial(fitness, target_string=target_string)
    child_length = len(target_string)
    population = create_population(population_length, child_length)

    best = population[0]
    current_generation = 0

    print('Generation | Fitness | Phenotype')
    print('-----------------------' + '-' * child_length)

    while best != target_string:
        #
        # selection
        #
        population = sorted(population, key=fitness_func)
        new_population_length = int(len(population) * 0.2)
        population = population[:new_population_length]

        #
        # crossover
        #
        while population_length > len(population):
            child1 = random.choice(population)
            child2 = random.choice(population)

            locus = random.randrange(0, child_length)
            new_child1, new_child2 = crossover(child1, child2, locus)

            population.append(new_child1)
            population.append(new_child2)

        #
        # mutation
        #
        for i in range(len(population)):
            if random.random() > 0.98:
                random_position = random.randrange(0, child_length)
                population[i] = mutation(population[i], random_position)

        current_generation += 1
        best = min(population, key=fitness_func, default=best)

        verbose_line = '{0:>10} | {1:>7} | {2}'.format(
            current_generation,
            fitness(best, target_string),
            best
        )
        print(verbose_line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Welcome to Hello-Evolution!')
    parser.add_argument('-n',
                        dest='population_length',
                        default=10000,
                        help='population 1lenght')
    parser.add_argument('--target', '-t',
                        dest='target_string',
                        default='Hello-Evolution',
                        help='String, that you are looking for')

    args = parser.parse_args()
    run(args.target_string, int(args.population_length))
