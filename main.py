from experta import *

class Person(Fact):
    """ Persoon met nnaam en geslacht. """
    name = Field(str, mandatory=True)
    gender = Field(str, mandatory=True)

class ParentOf(Fact):
    """ De vader/moeder relatie van kind """
    parent = Field(str, mandatory=True)
    child = Field(str, mandatory=True)

class GrandparentOf(Fact):
    """ De opa/oma relatie van kind. """
    pass

class UncleAuntOf(Fact):
    """ De nicht/neef relatie. """
    pass

class FamilyTree(KnowledgeEngine):
    @Rule(ParentOf(parent=MATCH.parent, child=MATCH.child),
          ParentOf(parent=MATCH.grandparent, child=MATCH.parent))
    def infer_grandparent(self, grandparent, child):
        self.declare(GrandparentOf(grandparent=grandparent, grandchild=child))

    @Rule(ParentOf(parent=MATCH.parent, child=MATCH.child),
          ParentOf(parent=MATCH.grandparent, child=MATCH.parent),
          Person(name=MATCH.grandparent, gender=MATCH.gender))
    def print_grandparent(self, grandparent, child, gender):
        grandparent_type = "grandmother" if gender == "F" else "grandfather"
        print(f"{grandparent} is the {grandparent_type} of {child}.")

    @Rule(ParentOf(parent=MATCH.parent, child=MATCH.child),
          ParentOf(parent=MATCH.grandparent, child=MATCH.uncle_aunt),
          TEST(lambda parent, uncle_aunt: parent != uncle_aunt))
    def infer_uncle_aunt(self, grandparent, uncle_aunt, child):
        self.declare(UncleAuntOf(uncle_aunt=uncle_aunt, niece_nephew=child))

    @Rule(UncleAuntOf(uncle_aunt=MATCH.uncle_aunt, niece_nephew=MATCH.niece_nephew))
    def print_uncle_aunt(self, uncle_aunt, niece_nephew):
        print(f"{uncle_aunt} is the uncle/aunt of {niece_nephew}.")

# Creating the engine and adding facts
engine = FamilyTree()
engine.reset()

engine.declare(Person(name="Alice", gender="F"))
engine.declare(Person(name="Bob", gender="M"))
engine.declare(Person(name="Charlie", gender="M"))
engine.declare(Person(name="Diana", gender="F"))
engine.declare(ParentOf(parent="Alice", child="Bob"))
engine.declare(ParentOf(parent="Charlie", child="Alice"))
engine.declare(ParentOf(parent="Diana", child="Alice"))

engine.run()
