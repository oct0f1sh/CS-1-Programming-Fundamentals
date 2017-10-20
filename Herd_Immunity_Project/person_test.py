from person import *
from virus import *


def test_person():
    virus = Virus("swag", 0.3, 0.5)
    person_1 = Person(69, False, virus)
    person_2 = Person(420, True, None)

    assert person_1.is_alive is True
    assert person_1._id == 69
    assert person_1.is_vaccinated is False
    assert person_1.infected.name == "swag"

    assert person_2.is_alive is True
    assert person_2._id == 420
    assert person_2.is_vaccinated is True
    assert person_2.infected is None

    is_person_1_alive = person_1.did_survive_infection()
    assert is_person_1_alive is not None
    if is_person_1_alive:
        assert person_1.is_alive is True
        assert person_1.infected is None
        assert person_1.is_vaccinated is True
    else:
        assert person_1.is_alive is False
