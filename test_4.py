def word_mesh(words: list[str]) -> str:
    def lcs(a, b):
        for i in range(1, len(a) + 1):
            if b.startswith(a[-i:]):
                return a[-i:]
        return ''     

    result = ""
    for a, b in zip(words, words[1:]):
        pair_lcs = lcs(a,b)
        if not pair_lcs:
            return "failed to mesh"
        result += pair_lcs


    return result

# Run this file for test
assert word_mesh(["beacon", "condominium", "umbilical", "california"]) == "conumcal"
assert word_mesh(["allow", "lowering", "ringmaster", "terror"]) == "lowringter"
assert word_mesh(["abandon", "donation", "onion", "ongoing"]) == "dononon"
assert word_mesh(["jamestown", "ownership", "hippocampus", "pushcart", "cartographer", "pheromone"]) == "ownhippuscartpher"
assert word_mesh(["kingdom", "dominator", "notorious", "usual", "allegory"] ) == "failed to mesh"