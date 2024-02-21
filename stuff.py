from collections import namedtuple

creature = namedtuple('creature',['name','description','location'])

my_creature = creature('Korrameenu fish','smooth and gileless','Krishna Delta')



thing2:str = "Hello"
thing2 = 43
print(thing2)

print(f'This {my_creature.name} which is uniquely {my_creature.description} is found in {my_creature.location}')