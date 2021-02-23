from math import sqrt
from zadanie2.tsp_genetic_algorithm import TspGeneticAlgorithm, insertion_sort
import time


def experiment(type_of_wolska, size_of_wolska, size_of_population, quantity_of_generations, rate_of_mutation, debug,
               number_of_samples):
    # variables holding experiment data
    average = 0
    standard_deviation = 0
    results = []
    time_average = 0
    # creating wolska
    path = TspGeneticAlgorithm(type_of_wolska, size_of_wolska, debug)

    # performing evolutions
    for sample in range(0, number_of_samples):
        time_start = time.time()
        results.append(path.start_evolution(size_of_population, quantity_of_generations, rate_of_mutation))
        time_average += time.time()-time_start
    results = insertion_sort(results)
    time_average /= number_of_samples

    # calculating average
    for res in results:
        average += res[1]
    average /= number_of_samples

    # calculation standard_deviation
    for res in results:
        standard_deviation += (res[1] - average) ** 2
    standard_deviation = sqrt(standard_deviation / number_of_samples)

    print("Best result: " + str(results[0][1]) + ", for path - " + str(results[0][0]))
    print("Average: " + str(average))
    print("Worst result: " + str(results[-1][1]) + ", for path - " + str(results[-1][0]))
    print("Standard_deviation: " + str(standard_deviation))
    print("Average Time: " + str(time_average) + "s\n\n\n")
    # print(path.wolska.create_graph())


experiment(type_of_wolska="chess", size_of_wolska=30, size_of_population=500, quantity_of_generations=20,
           rate_of_mutation=0.05, debug=False, number_of_samples=100)
