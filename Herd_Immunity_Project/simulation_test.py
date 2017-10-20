from simulation import Simulation

def test_simulation():
    sim = Simulation(200, 0.2, 'Swagola', 0.69, 0.1, 3)

    assert len(sim.population) == 200
    assert sim.vacc_percentage == 0.2
    assert sim.virus.name is 'Swagola'
    assert sim.virus.kill_rate == 0.69
    assert sim.virus.infection_rate == 0.1
    assert sim.initial_infected == 3
    assert sim.logger is not None
