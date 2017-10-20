import random, sys
from person import Person
from virus import Virus
from logger import Logger
random.seed(42)

class Simulation(object):

    def __init__(self, population_size, vacc_percentage, virus_name,
                 mortality_rate, basic_repro_num, initial_infected=1):
        self.population_size = population_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.total_infected = 0
        self.current_infected = 0
        self.next_person_id = 0
        self.virus = Virus(virus_name, basic_repro_num, mortality_rate)
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, population_size, vacc_percentage, initial_infected)

        self.logger = Logger('log.txt')
        self.logger.write_metadata(population_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num)

        self.newly_infected = []
        self.population = self._create_population(initial_infected)

    def _create_population(self, starting_infected):
        population = []
        infected_count = 0
        while len(population) < self.population_size:
            if infected_count <= starting_infected:
                infected_person = Person(len(population), False, self.virus)
                population.append(infected_person)
                infected_count += 1
            else:
                randy = random.random()
                if randy < self.vacc_percentage:
                    normal_person = Person(len(population), True, None)
                    population.append(normal_person)
                else:
                    infected_person = Person(len(population), False, self.virus)
                    population.append(infected_person)

                    infected_count += 1
        return population

    def _simulation_should_continue(self):
        dead = 0
        vaccinated = 0

        for person in self.population:
            if not person.is_vaccinated and person.is_alive:
                if person.infected is not None:
                    self.logger.log_infection_survival(person, person.did_survive_infection())
                return True
            if not person.is_alive:
                dead += 1
            if person.is_vaccinated:
                vaccinated += 1
        print('dead: {} + vaccinated: {} = {}'.format(dead, vaccinated, dead + vaccinated))

        if dead + vaccinated >= self.population_size:
            return False
        else:
            print('dead + vaccinated = {} out of {}'.format(dead, vaccinated))
            return True


    def run(self):
        time_step_counter = 1

        should_continue = True
        while should_continue:
            self.logger.log_time_step(time_step_counter)
            self.time_step()
            time_step_counter += 1
            should_continue = self._simulation_should_continue()
        print('The simulation has ended after {} turns.'.format(time_step_counter))

    def time_step(self):
        interactions = 0
        for person in self.population:
            if person.infected is not None and person.is_alive:
                while interactions <= 100:
                    randy = random.randint(0, self.population_size - 1)
                    person_2 = self.population[randy]
                    if person_2.is_alive:
                        self.interaction(person, person_2)
                        interactions += 1
            else:
                continue

        self._infect_newly_infected()



    def interaction(self, person1, random_person):
        assert person1.is_alive
        assert random_person.is_alive

        if random_person.is_vaccinated:
            self.logger.log_interaction(person1, random_person, False, True, False)
            return
        elif random_person.infected is not None:
            self.logger.log_interaction(person1, random_person, False, False, True)
            return
        else:
            randy = random.random()
            if randy < self.virus.infection_rate:
                self.newly_infected.append(random_person)
                self.logger.log_interaction(person1, random_person, True, False, True)
                return
            else:
                self.logger.log_interaction(person1, random_person, False, False, False)
                return

    def _infect_newly_infected(self):
        for infected_person in self.newly_infected:
            for pop_person in self.population:
                if infected_person._id == pop_person._id:
                    pop_person.infected = self.virus
                else:
                    continue

        self.newly_infected = []

if __name__ == "__main__":
    params = sys.argv[1:]
    pop_size = int(params[0])
    vacc_percentage = float(params[1])
    virus_name = str(params[2])
    mortality_rate = float(params[3])
    basic_repro_num = float(params[4])
    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1

    simulation = Simulation(pop_size, vacc_percentage, virus_name, mortality_rate,
                            basic_repro_num, initial_infected)
    simulation.run()
