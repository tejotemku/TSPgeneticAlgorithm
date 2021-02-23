from zadanie2.city import City
from typing import List
import random, math


class Wolska:
    def __init__(self, wolska_type: str, wolska_size: int, debug: bool = False):
        self.Debug = debug
        self.cities : List[City] = []
        self.wolska_size = wolska_size
        self.is_wolska_ok = True

        types_of_wolska = {
            "chess": self.wolska_type_chess,
            "random": self.wolska_type_random,
            "regions": self.wolska_type_regions
        }

        if not types_of_wolska.keys().__contains__(wolska_type):
            print('wrong type of wolska, please choose from given')
            self.is_wolska_ok = False
            for k in types_of_wolska.keys():
                print(k)
            return
        types_of_wolska.get(wolska_type)()
        self.calculate_distances()

    def wolska_type_chess(self):
        if self.Debug:
            print('chess')
        for i in range(0, self.wolska_size):
            self.cities.append(City(i, i % 6, i//5, debug=self.Debug))

    def wolska_type_random(self):
        if self.Debug:
            print('random')
        for i in range(0, self.wolska_size):
            self.cities.append(City(i, random.randint(0, 49), random.randint(0, 49), debug=self.Debug))

    def wolska_type_regions(self):
        if self.Debug:
            print('regions')
        for i in range(0, self.wolska_size):
            x = i // (self.wolska_size//2) * 15
            y = (i % (self.wolska_size//2)) // (self.wolska_size//6) * 15
            self.cities.append(City(i, random.randint(x, x + 7), random.randint(y, y + 7), debug=self.Debug))

    def calculate_distances(self):
        for i in range(0, self.wolska_size):
            for j in range(0, self.wolska_size):
                if i != j:
                    distance = math.sqrt((self.cities[i].x - self.cities[j].x)**2 + (self.cities[i].y - self.cities[j].y)**2)
                    self.cities[i].add_neighbour(j, distance)
                    self.cities[j].add_neighbour(i, distance)

    def create_graph(self):
        graph = []
        for i in range(0,  50):
            row = []
            for j in range(0, 50):
                row.append('  ')
            graph.append(row)
        for city in self.cities:
            graph[city.x][city.y] = str(city.index)
        graph_string = ''
        for row in graph:
            for element in row:
                graph_string += str(element)
            graph_string += '\n'
        return graph_string