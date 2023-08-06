from Individual import Individual

class Population:
    def __init__(self, size, cities=None):
        self.size = size
        self.individuals = []
        if cities is not None:
            for _ in range(self.size):
                self.individuals.append(Individual(cities, True))
        else:
            for _ in range(self.size):
                self.individuals.append(None)  # Create an empty population

    def set_individual(self, indiv, index):
        self.individuals[index] = indiv

    def get_individual(self, index):
        return self.individuals[index]

    def get_fittest(self):
        fittest = self.individuals[0]
        for i in range(len(self.individuals)):
            if fittest.calculate_fitness() > self.individuals[i].calculate_fitness():
                fittest = self.individuals[i]
        return fittest

    def get_size(self):
        return self.size

    def __str__(self):
        data = "\n".join(str(individual) for individual in self.individuals)
        return data

