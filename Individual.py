import random
from typing import List

from City import City  # Assuming you have implemented the City class separately
from FitnessCalculator import FitnessCalculator  # Assuming you have implemented the FitnessCalculator class separately


class Individual:
    def __init__(self, gene_pool: List[City], init: bool):
        self.gene_length = len(gene_pool)
        self.genes = [None] * self.gene_length
        if init:
            self.generate_genes(gene_pool)

    def generate_genes(self, gene_pool: List[City]):
        gene_list = gene_pool[:]
        random.shuffle(gene_list)
        for i in range(self.gene_length):
            gene = gene_list.pop()
            self.set_gene(gene, i)

    def calculate_fitness(self) -> float:
        self.fitness = FitnessCalculator.calculate(self)
        return self.fitness

    def set_gene(self, gene: City, index: int):
        self.genes[index] = gene
        self.fitness = 0

    def get_genes(self) -> List[City]:
        return self.genes

    def get_gene(self, index: int) -> City:
        return self.genes[index]

    def get_gene_length(self) -> int:
        return self.gene_length

    def __str__(self) -> str:
        s_genes = "".join(str(gene) for gene in self.get_genes())
        return "{fitness: " + str(self.fitness) + ", genes: " + s_genes + "}"
