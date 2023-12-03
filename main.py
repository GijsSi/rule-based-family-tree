# from random import choice
from experta import *

class Personne(Fact):
    """Info about the personne."""
    pass

class Father(Fact):
    """Info about the parents."""
    pass

class Mother(Fact):
    """Info about the parents."""
    pass

class Brother(Fact):
    """Info about the siblings."""
    pass

class Sister(Fact):
    """Info about the siblings."""
    pass

class Uncle(Fact):
    """Info about the uncles."""
    pass

class Aunt(Fact):
    """Info about the aunts."""
    pass

class FamilyTree(KnowledgeEngine):
    @Rule(AND(
        Personne(name=MATCH.name),
        Father(name=MATCH.name_father),
        Mother(name=MATCH.name_mother),
        Brother(name=MATCH.name_brother),
        Sister(name=MATCH.name_sister),
        Uncle(name=MATCH.name_uncle),
        Aunt(name=MATCH.name_aunt)))
    def family_tree(self, name, name_father, name_mother, name_brother, name_sister, name_uncle, name_aunt):
        print(f"{name} is the son of {name_father} and {name_mother}.")
        print(f"{name} has a brother {name_brother} and a sister {name_sister}.")
        print(f"{name} has an uncle {name_uncle} and an aunt {name_aunt}.")

engine = FamilyTree()
engine.reset()

engine.declare(Personne(name="Jack"))
engine.declare(Father(name="Laurens"))
engine.declare(Mother(name="Fabienne"))
engine.declare(Brother(name="Peter"))
engine.declare(Sister(name="Gertrude"))
engine.declare(Uncle(name="Donald"))
engine.declare(Aunt(name="Annie"))

engine.run()