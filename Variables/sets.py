# Sets - Conjuntos

# Create set with set().
set_one = set(["Data One", "Data Two"])

# Putting a set inside another set. Using frozenset( )
set_two = frozenset(["Data One", "Data Two"])
set_three = { set_two, "Data One", "Data Two"}

# Set theory
set_1 = {1,3,5,7}
set_2 = {1,3,7}

# Checking if it is a subset. (<= or .issubset())
resultForm1Sub= set_2.issubset(set_1)
resultForm2Sub = set_2 <= set_1

# Checking if it is a superset. (>= or .issuperset())
resultForm1Super = set_2.issuperset(set_1)
resultForm2Super = set_2 >= set_1

# Checking if there are any numbers in common. (!= or .isdisjoint())
reslutForm1 = set_2.isdisjoint(set_1)
reslutForm1 = set_2 != set_1 