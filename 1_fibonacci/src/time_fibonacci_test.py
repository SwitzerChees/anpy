from time_fibonacci import *
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(3100)

# Fibonacci Zahlen zum testen
fibTest = [1, 10, 50, 100, 500, 900, 1800, 3000]

# Beschriftungen für den Chart X,Y Achse
plt.ylabel('Time')
plt.xlabel('Fib')

# Berechnung der rekursiven Resultate
results = []
for fib in fibTest:
    results.append(time_fib(fib))
    
# Darstellung des Diagramms
plt.plot(fibTest, results)
plt.show()

# Berechnung der iterativen Resultate
results = []
for fib in fibTest:
    results.append(time_fib_iter(fib))
    
# Darstellung des Diagramms
plt.plot(fibTest, results)
plt.show()