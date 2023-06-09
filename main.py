from landscape.component.tree import Tree
from landscape.component.rock import Rock
from landscape.component.trunk import Trunk

from landscape.forest import Forest

if __name__ == '__main__':
    tree_star = Tree(5, '*')

    rock = Rock(5, 3, '#')
    tree_o = Tree(3, 'o')
    trunk = Trunk(5, '*')
    forest = Forest()
    forest.add(tree_star)
    forest.add(rock)
    forest.add(tree_o)
    forest.add(trunk)

    print(forest)
