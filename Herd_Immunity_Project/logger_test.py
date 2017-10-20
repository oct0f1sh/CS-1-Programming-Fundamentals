from logger import Logger
from person import Person
from virus import Virus

def test_logger():
    virus = Virus('ugh', 0.10, 0.90)
    logger = Logger('log.txt')
    logger.write_metadata(200, 0.10, 'Virus', 0.90, 0.20)
    logger.log_interaction(Person(1, False, virus), Person(2, False, None), True, False, True)
    logger.log_infection_survival(Person(3, False, virus), False)
    logger.log_time_step(34)
    f = open(logger.file_name, 'r')

    assert f.readline() == 'Creating sim: {}\t{}\t{}\t{}\t{}\n'.format(200, 0.10, 'Virus', 0.90, 0.20)
    assert f.readline() == 'Interaction: {}\t{}\t{}\t{}\t{}\n'.format(1, 2, True, False, True)
    assert f.readline() == 'Died from infection: {}\t{}\n'.format(3, False)
    assert f.readline() == 'Starting step {}\n'.format(34)