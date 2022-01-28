import random
import src.names


class Characters:
    is_alive = True
    is_magical = False
    is_divine = False
    strength = None
    reflex = None
    intellect = None
    cunning = None


class Knight(Characters):
    character_name = src.names.first_name()
    character_race = "Human"
    strength = random.randint(3, 18)
    reflex = random.randint(3, 18)
    intellect = random.randint(3, 18)
    cunning = random.randint(3, 18)


class Cleric(Characters):
    character_name = src.names.first_name()
    character_race = "Human"
    is_divine = True
    strength = random.randint(3, 18)
    reflex = random.randint(3, 18)
    intellect = random.randint(3, 18)
    cunning = random.randint(3, 18)


class Mage(Characters):
    character_name = src.names.first_name()
    character_race = "Human"
    is_magical = True
    strength = random.randint(3, 18)
    reflex = random.randint(3, 18)
    intellect = random.randint(3, 18)
    cunning = random.randint(3, 18)


class Governor(Characters):
    character_name = src.names.first_name()
    character_race = "Human"
    strength = random.randint(3, 18)
    reflex = random.randint(3, 18)
    intellect = random.randint(3, 18)
    cunning = random.randint(3, 18)
