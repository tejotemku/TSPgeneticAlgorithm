from zadanie2.wolska import Wolska
import random


class TspGeneticAlgorithm:
    def __init__(self, wolska_type, wolska_size, debug=False):
        # if prints should be activated
        self.Debug = debug
        # mutation rate
        self.mutation_rate = 0
        # number of generations before revealing "the winner"
        self.number_of_generations = 0
        # map of the cities
        self.wolska = Wolska(wolska_type, wolska_size, debug)
        # size of population that will take part in evolution
        self.population_size = 0
        # currently shortest path (by generation)
        self.currently_shortest_path = 0
        # sorted list of indexes from 0 to 29 used to generate random paths
        self.cities_list = []
        for i in range(0, 30):
            self.cities_list.append(i)
        self.population = []

    def start_evolution(self, pop_size, generations, mutation_rate, print_info: bool = False):
        self.mutation_rate = mutation_rate
        self.population_size = pop_size
        self.number_of_generations = generations

        # creating initial population
        self.population = []
        for i in range(0, self.population_size):
            # shuffling sorted list to create random paths
            rand_list = list(self.cities_list)
            random.shuffle(rand_list)
            self.population.append(rand_list)
        if not self.wolska.is_wolska_ok:
            print("Bad wolska type, cannot start")
            return []
        current_generation = 0
        
        while current_generation < self.number_of_generations:
            self.population = self.test_population()
            self.next_generation()
            self.mutate()
            current_generation += 1
            if print_info:
                print("Generation: " + str(current_generation) + ", Path: " + str(self.population[0]) + ", length: " + str(self.currently_shortest_path))
        return [self.population[0], self.currently_shortest_path]

    # tests populations results
    def test_population(self):
        population_results = []
        for i in range(0, self.population_size):
            element = self.population[i]
            starting_city = element[0]
            distance = 0
            for i in range(1, 30):
                distance += self.wolska.cities[element[i]].get_neighbour(element[i-1])
            distance += self.wolska.cities[starting_city].get_neighbour(element[-1])
            population_results.append([element, distance])
        return population_results

    # decides which elements stay
    def next_generation(self):
        self.population = insertion_sort(self.population)
        self.currently_shortest_path = self.population[0][1]
        self.tournament_selection()
        return

    def tournament_selection(self):
        surviving_pop = []
        for i in range(self.population_size//2):
            city1 = self.population[random.randint(0, self.population_size-1)]
            city2 = self.population[random.randint(0, self.population_size-1)]
            if city1[1] < city2[1]:
                surviving_pop.append(city1[0])
            else:
                surviving_pop.append(city2[0])
        self.population = surviving_pop
        return

    # mutation new next generation
    def mutate(self):
        next_generation = list(self.population)
        for i in range(0, self.population_size//2):
            next_generation[i] = self.mutate_one(list(next_generation[i]))
        self.population.extend(next_generation)
        return

    def mutate_one(self, path):
        for swapped in range(len(path)):
            if random.random() < self.mutation_rate:
                swap_with = int(random.random() * len(path))
                path[swapped], path[swap_with] = path[swap_with], path[swapped]
        return path


# sorting population by shortest path
def insertion_sort(population):
    size = len(population)
    for i in range(1, size):
        j = i - 1
        temp_arr = population[i]
        while j >= 0 and temp_arr[1] < population[j][1]:
            population[j + 1] = population[j]
            j -= 1
        population[j + 1] = temp_arr
    return population
