import unittest
from hello import *


class HelloEvolutionTests(unittest.TestCase):
    def setUp(self):
        self.child_lenght = 10
        self.population_lenght = 100

    def test_random_character(self):
        s = random_character()
        assert isinstance(s, str)
        assert len(s) == 1

    def test_fitness(self):
        assert fitness('test', 'test') == 0
        assert fitness('t1st', 'test') > fitness('test', 'test')
        assert fitness('t23a', 'test') > fitness('t1st', 'test')

    def test_create_child(self):
        child = create_child(self.child_lenght)
        assert isinstance(child, str)
        assert len(child) == self.child_lenght

    def test_create_population(self):
        population = create_population(self.population_lenght,
                                       self.child_lenght)
        assert isinstance(population, list)
        assert len(population) == self.population_lenght

        for child in population:
            assert isinstance(child, str)
            assert len(child) == self.child_lenght

    def test_crossover(self):
        child1 = create_child(self.child_lenght)
        child2 = create_child(self.child_lenght)

        new_child1, new_child2 = crossover(child1, child2, 2)

        assert new_child1 != new_child2
        assert child2[2:] in new_child1
        assert child2[:2] in new_child2

    def test_mutation(self):
        child = create_child(self.child_lenght)
        mutated_child = mutation(child, 2)

        assert child[2] != mutated_child[2]


if __name__ == '__main__':
    unittest.main()
