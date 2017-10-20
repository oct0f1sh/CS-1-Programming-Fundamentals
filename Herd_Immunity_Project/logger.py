class Logger(object):

    def __init__(self, file_name):
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        f = open(self.file_name, 'w')
        f.write('Creating sim: {}\t{}\t{}\t{}\t{}\n'.format(pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num))
        f.close()

    def log_interaction(self, person1, person2, did_infect=None,
                        person2_vacc=None, person2_sick=None):
        f = open(self.file_name, 'a')
        log = 'Interaction: {}\t{}\t{}\t{}\t{}\n'.format(person1._id, person2._id, did_infect, person2_vacc, person2_sick)
        f.write(log)
        f.close()

    def log_infection_survival(self, person, did_die_from_infection):
        f = open(self.file_name, 'a')
        log = 'Died from infection: {}\t{}\n'.format(person._id, did_die_from_infection)
        f.write(log)
        f.close()

    def log_time_step(self, time_step_number):
        f = open(self.file_name, 'a')
        log = 'Starting step {}\n'.format(time_step_number)
        f.write(log)
        f.close()

    def log_results(self, time_step_number):
        f = open(self.file_name, 'a')
        log = 'Simulation ended after {} turns'.format(time_step_number)
        f.write(log)
        f.close()
