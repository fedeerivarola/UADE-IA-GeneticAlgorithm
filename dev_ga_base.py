'''
Condiciones
~~~~~~~~~~~
1. Hay 5 casas.
2. El Matematico vive en la casa roja.
3. El hacker programa en Python.
4. El Brackets es utilizado en la casa verde.
5. El analista usa Atom.
6. La casa verde esta a la derecha de la casa blanca.
7. La persona que usa Redis programa en Java
8. Cassandra es utilizado en la casa amarilla
9. Notepad++ es usado en la casa del medio.
10. El Desarrollador vive en la primer casa.
11. La persona que usa HBase vive al lado de la que programa en JavaScript.
12. La persona que usa Cassandra es vecina de la que programa en C#.
13. La persona que usa Neo4J usa Sublime Text.
14. El Ingeniero usa MongoDB.
15. EL desarrollador vive en la casa azul.

Quien usa vim?


Resumen:
Colores = Rojo, Azul, Verde, Blanco, Amarillo
Profesiones = Matematico, Hacker, Ingeniero, Analista, Desarrollador
Lenguaje = Python, C#, JAVA, C++, JavaScript
BD = Cassandra, MongoDB, Neo4j, Redis, HBase
editor = Brackets, Sublime Text, Atom, Notepad++, Vim
'''

import random
import time



colors =      {'001' : 'red',          '010' : 'blue',          '011' : 'green',    '100' : 'white',    '101' : 'yellow'}
prefession =  {'001' : 'Mathematician','010' : 'Hacker',        '011' : 'Engineer', '100' : 'Analyst',  '101' : 'Developer'}
languaje =    {'001' : 'Python',       '010' : 'C#',            '011' : 'Java',     '100' : 'C++',      '101' : 'JavaScript'}
database =    {'001' : 'Cassandra',    '010' : 'MongoDB',       '011' : 'HBase',    '100' : 'Neo4j',    '101' : 'Redis'}
editor =      {'001' : 'Brackets',     '010' : 'Sublime Text',  '011' : 'Vim',      '100' : 'Atom',     '101' : 'Notepad++'}

class Phenotype:

    def __init__(self):
        # crear un individuo
        values = ['001','010','011','100','101']
        casa = []
        vecindario = []
        for x in range(0,5):
            casa.clear()
            for y in range(0,5):
                gen = random.randint(0,4)
                casa.append(values[gen])
            print(f"casa {x+1}: {casa}")
            vecindario.extend(casa.copy())
        print(f"vecindario {vecindario}")
        self.chromosome = vecindario.copy()
        self.score   = 0

    def decode(self):
        ''' traduce 0's y 1's (conjunto de genes: 3) en valores segun un diccionario '''
        return [[colors[self.chromosome[i*5+0]], 
                 prefession[self.chromosome[i*5+1]],
                 languaje[self.chromosome[i*5+2]],
                 database[self.chromosome[i*5+3]],
                 editor[self.chromosome[i*5+4]]] for i in range(5)]
        

    def encode(self):
        pass

    def setChromosoma(self, chromosoma):
        self.chromosome.clear()
        self.chromosome = chromosoma
        pass

    def mutate(self):
        ''' muta un fenotipo, optimizado'''
        x  = random.randint(0,24)
        if (self.chromosome[x] == '001'):
            self.chromosome[x] = '100'
        elif self.chromosome[x] == '010':
            self.chromosome[x] = '011'
        elif self.chromosome[x] == '011':
            self.chromosome[x] = '001'
        elif self.chromosome[x] == '100':
            self.chromosome[x] = '101'
        elif self.chromosome[x] == '101':
            self.chromosome[x] = '010'
        pass

    def fitness_function(self):
        ''' calcula el valor de fitness del cromosoma segun el problema en particular '''

        self.score = 0

        ok_score = 1
        fail_score = -1
        punish_score = -1 
        
        original = self.decode()
        chromosome = []
        for x in range(len(original)):
            chromosome.extend(original[x])
        
# 1. Hay 5 casas.
# 2. El Matematico vive en la casa roja.
        try:
            i = chromosome.index('Mathematician')
            if chromosome[i-1] == 'red':
                self.score += ok_score
            else:
                self.score += fail_score
        except:
            self.score += fail_score
# 3. El hacker programa en Python.
        try:
            i = chromosome.index('Hacker')
            if chromosome[i+1] == 'Python':
                self.score += ok_score
            else:
                self.score += fail_score
        except:
            self.score += fail_score
# 4. El Brackets es utilizado en la casa verde.
        try:
            i = chromosome.index('Brackets')
            if chromosome[i-4] == 'green':
                self.score += ok_score
            else:
                self.score += fail_score
        except:
            self.score += fail_score
# 5. El analista usa Atom.
        try:
            i = chromosome.index('Analyst')
            if chromosome[i+3] == 'Atom':
                self.score += ok_score
            else:
                self.score += fail_score
        except:
            self.score += fail_score
# 6. La casa verde esta a la derecha de la casa blanca.
        try:
            i = chromosome.index('green')
            if chromosome[i-5] == 'white':
                self.score += ok_score
            else:
                self.score += fail_score
        except:
            self.score += fail_score
# 7. La persona que usa Redis programa en Java
        try:
            i = chromosome.index('Redis')
            if chromosome[i-1] == 'Java':
                self.score += ok_score
            else:
                self.score += fail_score
        except:
            self.score += fail_score
# 8. Cassandra es utilizado en la casa amarilla
        try:
            i = chromosome.index('Cassandra')
            if chromosome[i-3] == 'yellow':
                self.score += ok_score
            else:
                self.score += fail_score
        except:
            self.score += fail_score
# 9. Notepad++ es usado en la casa del medio.
        try:
            i = chromosome.index('Notepad++')
            if 9 < i and i < 15:
                self.score += ok_score
            else:
                self.score += fail_score
        except:
            self.score += fail_score
# 10. El Desarrollador vive en la primer casa.
        try:
            i = chromosome.index('Developer')
            if i < 5:
                self.score += ok_score
            else:
                self.score += fail_score
        except:
            self.score += fail_score
# 11. La persona que usa HBase vive al lado de la que programa en JavaScript.
        try:
            i = chromosome.index('HBase')
            if chromosome[i-1] == 'Javascript':
                self.score += ok_score
            else:
                self.score += fail_score
        except:
            self.score += fail_score
# 12. La persona que usa Cassandra es vecina de la que programa en C#.
        try:
            i = chromosome.index('Cassandra')
            if chromosome[i-1] == 'C#':
                self.score += ok_score
            else:
                self.score += fail_score
        except:
            self.score += fail_score
# 13. La persona que usa Neo4J usa Sublime Text.
        try:
            i = chromosome.index('Neo4J')
            if chromosome[i+1] == 'Sublime Text':
                self.score += ok_score
            else:
                self.score += fail_score
        except:
            self.score += fail_score
# 14. El Ingeniero usa MongoDB.
        try:
            i = chromosome.index('Engineer')
            if chromosome[i+2] == 'MongoDB':
                self.score += ok_score
            else:
                self.score += fail_score
        except:
            self.score += fail_score
# 15. EL desarrollador vive en la casa azul.
        try:
            i = chromosome.index('Developer')
            if chromosome[i-1] == 'blue':
                self.score += ok_score
            else:
                self.score += fail_score
        except:
            self.score += fail_score
            
        for x in range(0, len(chromosome)):
            j = chromosome.count(chromosome[x])
            if j > 1:
                self.score += fail_score 
            pass
        pass

class Riddle:

    def __init__(self):
        self.start_time = time.time()
        self.population = []


    '''
    proceso general
    '''
    def solve(self, n_population):
        
        self.generate(n_population)
        print(f"Población creada con {len(self.population)} individuos")

        ''' descomentame '''
        print(self.population[0].chromosome)
        print(self.population[1].chromosome)
        print(self.population[0].decode())

        print("Inicio del proceso iterativo")
        fit, indi = self.iterar()
        print(f"Fin del proceso, mejor resultado \n - Fitness: {fit} \n - Individuo {indi.chromosome} \n - Individuo {indi.decode()}")
        

    def iterar(self):

        counter = 0
        break_condition = False

        crossover_prop = 0.80

        while not(break_condition):
            
            if counter % 100 == 0:
                print("--------------------------------")
                print(counter)
                print(self.population[0].decode())
            
            # seleccion
            total = len(self.population)
            for i in range(total):                
                self.population[i].fitness_function()
                pass
            self.population.sort(key=lambda x: x.score, reverse=True)
            print(f" soy el mejor {self.population[0].score}")
            
            #condicion de corte porque encontre al mejor
            if(self.population[0].score >= 14):
                break_condition = True
            #condicion de corte porque la poblacion es pesima
            if(self.population[0].score <= 0):
                break_condition = True

            # crossover
            N = 200
            limit = 2000
            newGeneration = []
            while(len(newGeneration) < limit):
                for s in range(0, N, 2):
                    padre1 = self.population[s].chromosome
                    padre2 = self.population[s+1].chromosome
                    nuevo = self.crossOver(progenitor_1 = padre1, progenitor_2 = padre2)
                    newGeneration.append(nuevo)
                    pass
                pass
            
            # mutate
            newGenerationMutado = []
            newGenerationMutado.append(self.mutate(newGeneration))

            print(f"generacion anterior: {self.population}")
            self.population.clear()
            self.population = newGenerationMutado[0]
            print(f"nueva generacion: {self.population}")

            # condicion de corte por cantidad
            N2 = 100
            if counter > N2 :
                print("programame")
                pass
                break_condition = True

            counter += 1

        return self.population[0].score, self.population[0]

    '''
    operacion: generar individuos y agregarlos a la poblacion
    '''
    def generate(self, i):
        for x in range(0,i):
            newbie = Phenotype()
            print(f"newbie: {newbie.chromosome}")
            self.population.append(newbie)

    '''
    operacion: mutación. Cambiar la configuración fenotipica de un individuo
    '''
    def mutate(self, crossed, prob=0.5):
        prob = prob * 100
        for y in range(len(crossed)):
            x = random.randint(0,100)
            if(x > prob):
                crossed[y].mutate()
                pass
            pass
        return crossed

    '''
    operacion: cruazamiento. Intercambio de razos fenotipicos entre individuos
    '''
    def crossOver(self, progenitor_1, progenitor_2):
        print(f"papa 1 {progenitor_1}")
        print(f"papa 2 {progenitor_2}")
        hijo = Phenotype ()
        hijoChromo = []
        i = random.randint(0,1)

        if i == 0:
            for x in range(12):
                hijoChromo.append(progenitor_1[x])
            for y in range(12, 25):
                hijoChromo.append(progenitor_2[y])

        elif i == 1:
            for x in range(12):
                hijoChromo.append(progenitor_2[x])
                
            for y in range(12, 25):
                hijoChromo.append(progenitor_1[y])
        
        hijo.setChromosoma(hijoChromo)

        return hijo

start = time.time()

rid = Riddle()
rid.solve(n_population = 2000)

end = time.time()
hours, rem = divmod(end-start, 3600)
minutes, seconds = divmod(rem, 60)
print("Tiempo transcurrido {:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))