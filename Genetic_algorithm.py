import random
from Population import Population
from Individual import Individual
from copy import deepcopy

numberOfMutations = 1
tournamentSize = 10
elitism = True

def evolve_population(pop):
    new_pop = Population(pop.get_size())
    fittest = pop.get_fittest()

    for i in range(pop.get_size()):
        indiv1 = tournament_selection(pop)
        indiv2 = tournament_selection(pop)
        new_indiv = crossover(indiv1, indiv2)
        mutate(new_indiv)
        new_pop.set_individual(new_indiv, i)

    if elitism:
        new_pop.set_individual(fittest, 0)

    return new_pop

def crossover(ind1, ind2):
    size = len(ind1.genes)
    parent1_genes = deepcopy(ind1.genes)
    parent2_genes = deepcopy(ind2.genes)

    gene_a = random.randint(0, size - 1)
    gene_b = random.randint(0, size)

    start_gene = min(gene_a, gene_b)
    end_gene = max(gene_a, gene_b)

    child = Individual(ind1.genes, False)
    child_genes = deepcopy(child.genes)
    child_genes.clear()
    child_genes.extend(parent1_genes[start_gene:end_gene])

    current_city_index = 0
    current_city_in_tour2 = 0
    for i in range(size):
        current_city_index = (end_gene + i) % size

        current_city_in_tour2 = parent2_genes.index(parent2_genes[current_city_index])

        if parent2_genes[current_city_in_tour2] not in child_genes:
            child_genes.append(parent2_genes[current_city_in_tour2])

    child_genes = child_genes[start_gene:] + child_genes[:start_gene]
    for i in range(size):
        child.set_gene(child_genes[i], i)

    return child

def mutate(indiv):
    for n in range(numberOfMutations):
        r1 = random.randint(0, indiv.get_gene_length() - 1)
        r2 = random.randint(0, indiv.get_gene_length() - 1)
        temp = indiv.get_gene(r1)
        indiv.set_gene(indiv.get_gene(r2), r1)
        indiv.set_gene(temp, r2)

def tournament_selection(pop):
    tournament = Population(tournamentSize)
    for i in range(tournamentSize):
        random_id = random.randint(0, pop.get_size() - 1)
        tournament.set_individual(pop.get_individual(random_id), i)

    return tournament.get_fittest()
