
def word_mesh(words: list[str]):
    # Write your code here.
    pass

# Run this file for test
assert word_mesh(["beacon", "condominium", "umbilical", "california"]) == "conumcal"
assert word_mesh(["allow", "lowering", "ringmaster", "terror"]) == "lowringter"
assert word_mesh(["abandon", "donation", "onion", "ongoing"]) == "dononon"
assert word_mesh(["jamestown", "ownership", "hippocampus", "pushcart", "cartographer", "pheromone"]) == "ownhippuscartpher"
assert word_mesh(["kingdom", "dominator", "notorious", "usual", "allegory"] ) == "failed to mesh"