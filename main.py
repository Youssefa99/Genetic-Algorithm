import numpy as np
import random


# Constraints
# Can't have same Nurse at same Time twice with different patients (N1,T1,p1) and (N1,T1,p2)
# can't have same patient at same Time twice with same nurse (p1,T2,N3) and (p1,T2,N3)
# can't have same patient with same Time with different nurse (p1,T2,N3) and (p1,T2,N2)


# random initial values of population

# Test case for first constraint
test1 = np.zeros((5, 3), dtype=object)


test1[0, :] = ["p1", "T2", "N2"]
test1[1, :] = ["p2", "T2", "N2"]
test1[2, :] = ["p3", "T1", "N1"]
test1[3, :] = ["p4", "T3", "N2"]
test1[4, :] = ["p5", "T3", "N1"]


# Test case for second constraint
test2 = np.zeros((5, 3), dtype=object)

test2[0, :] = ["p1", "T2", "N2"]
test2[1, :] = ["p1", "T2", "N2"]
test2[2, :] = ["p3", "T1", "N1"]
test2[3, :] = ["p4", "T3", "N2"]
test2[4, :] = ["p5", "T3", "N1"]


# Test case for third constraint
test3 = np.zeros((5, 3), dtype=object)

test3[0, :] = ["p1", "T2", "N2"]
test3[1, :] = ["p1", "T2", "N3"]
test3[2, :] = ["p3", "T1", "N1"]
test3[3, :] = ["p4", "T3", "N2"]
test3[4, :] = ["p5", "T3", "N1"]

# test case for all constraints simultaneously
test4 = np.zeros((6, 3), dtype=object)

test4[0, :] = ["p1", "T2", "N2"]
test4[1, :] = ["p2", "T2", "N2"]
test4[2, :] = ["p3", "T1", "N1"]
test4[3, :] = ["p3", "T1", "N1"]
test4[4, :] = ["p4", "T3", "N2"]
test4[5, :] = ["p4", "T3", "N1"]

# available time slots
time = ["T1", "T2", "T3", "T4", "T5", "T6"]

# available Nurses
nurse = ["N1", "N2", "N3", "N4", "N5", "N6"]



def GA(population, n):
    iter = 0
    min_error = 1000
    chromosome_error = [1000] * n
    offspring = np.full((round(n/2), round(n/2)), 0).tolist()
    while min_error != 0:
        print("population of generation " + str(iter) + " is")
        print(population)

        # calculate fitness function
        for i in range(n):
            conflicts = 0
            for j in range(n):
                if i != j:
                    if population[i, :][1] == population[j, :][1] and population[i, :][2] == population[j, :][2]:
                        conflicts = conflicts + 1
                    if population[i, :][0] == population[j, :][0] and population[i, :][1] == population[j, :][1] and population[i, :][2] == population[j, :][2]:
                        conflicts = conflicts + 1
                    if population[i, :][0] == population[j, :][0] and population[i, :][1] == population[j, :][1] and population[i, :][2] != population[j, :][2]:
                        conflicts = conflicts + 1
            chromosome_error[i] = conflicts
        max_indices = [-1] * round(n/2)
        min_indices = []
        min_error = max(chromosome_error)

        # get indices of least fit chromosomes
        for i in range(round(n/2)):
            max_indices[i] = chromosome_error.index(max(chromosome_error))
            chromosome_error[chromosome_error.index(max(chromosome_error))] = -1

        # get indices of most fit chromosomes
        for i in range(n):
            if i not in max_indices:
                min_indices.append(i)

        # crossover
        for i in range(round(n/2)):
            if i == 1:
                offspring[0] = np.concatenate((population[min_indices[0], :][:round(n/2) - 1], population[min_indices[round(n/2) - 1], :][round(n/2) - 1:]))
            else:
                for j in range(i+1, round(n/2)):
                    offspring[i+j] = np.concatenate((population[min_indices[i+j], :][:round(n/2) - 1], population[min_indices[i+j-1], :][round(n / 2) - 1:]))

        # replace offsprings with troubled chromosomes
        j = 0
        for i in range(n):
            if i in max_indices:
                # random resetting mutation
                offspring[j][1] = random.choice(time)
                population[i, :][1:] = offspring[j][1:]
                j = j + 1
            if j == round(n/2) - 1:
                break
        iter = iter + 1
        if iter > 10:
            break


GA(test4, len(test4))
