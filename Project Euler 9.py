def triples_generator(input_size_of_terms):  # argument of triples_generator is how large the sum of triples can be
    def ozanam_generator(term_ozanam):  # argument is just how many terms are generated
        term_ozanam += 1
        numerator = ((4 * term_ozanam) + 3)
        denominator = ((4 * term_ozanam) + 4)
        side_a = denominator
        side_b = (term_ozanam * denominator) + numerator
        side_c = ((side_a ** 2) + (side_b ** 2)) ** .5
        triples_sublist = [side_a, side_b, side_c]
        return triples_sublist

    def stifel_generator(term_stifel):
        term_stifel += 1
        numerator = term_stifel
        denominator = ((2 * term_stifel) + 1)
        side_a = denominator
        side_b = (term_stifel * denominator) + numerator
        side_c = ((side_a ** 2) + (side_b ** 2)) ** .5
        triples_sublist = [side_a, side_b, side_c]
        return triples_sublist

    def triple_multiplier(input_list): #finds multiples of already found pythagorean triplets, which, also, are valid triplets
        for i in range(0, len(input_list)):
            new_a, new_b, new_c = input_list[i][0], input_list[i][1], input_list[i][2]
            while new_a + new_b + new_c <= input_size_of_terms:
                new_a += input_list[i][0]
                new_b += input_list[i][1]
                new_c += input_list[i][2]
                list_of_new_sides = [new_a, new_b, new_c]
                input_list.append(list_of_new_sides)


    triples_list = []
    triples_sublist_ozanam = [[8, 15, 17]]
    triples_sublist_stifel = [[3, 4, 5]]
    term_ozanam = 1
    term_stifel = 1

    while sum(triples_sublist_ozanam[-1]) < input_size_of_terms:
        triples_sublist_ozanam.append(ozanam_generator(term_ozanam))
        term_ozanam += 1

    while sum(triples_sublist_stifel[-1]) <= input_size_of_terms:
        triples_sublist_stifel.append(stifel_generator(term_stifel))
        term_stifel += 1

    triple_multiplier(triples_sublist_ozanam)
    triple_multiplier(triples_sublist_stifel)

    def list_populater(input_list): # argument must be a list
        for i in range(0, len(input_list)):
            triples_list.append(input_list[i])

    list_populater(triples_sublist_stifel)
    list_populater(triples_sublist_ozanam)

    for i in range(0, len(triples_list)):
        if sum(triples_list[i]) == input_size_of_terms:
            print(triples_list[i][0] * triples_list[i][1] * triples_list[i][2])
            break


triples_generator(12)
