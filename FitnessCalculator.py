from City import City  # Assuming you have implemented the City class separately


class FitnessCalculator:
    solution = None

    @staticmethod
    def set_problem(new_solution):
        FitnessCalculator.solution = new_solution

    @staticmethod
    def calculate(individual):
        fitness = 0
        for i in range(len(FitnessCalculator.solution) - 1):
            fitness += individual.get_gene(i).distance_to(individual.get_gene(i + 1))
        return fitness
