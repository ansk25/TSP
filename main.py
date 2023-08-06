from City import City
from FitnessCalculator import FitnessCalculator
from Population import Population
from Genetic_algorithm import evolve_population
import random


def main():
    noc = 50
    cites = []
    random.seed()
    for i in range(noc):
        x = random.randint(0, 99)
        y = random.randint(0, 99)
        c = City(x, y)
        cites.append(c)

    FitnessCalculator.set_problem(cites)

    size = 200
    pop = Population(size, cites)

    for i in range(100000):
        print(pop.get_fittest())
        pop = evolve_population(pop)


if __name__ == "__main__":
    main()
