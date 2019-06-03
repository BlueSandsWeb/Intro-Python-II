int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# lc = [ formatting collection condition]
# lc = [ map collection filter]

# add three to each number
# lc = [ formatting collection condition]
add_3 = [(i + 3) for i in int_list]  # (formatting) then collection
print(add_3)

#                 (formatting) collection       (if) = condition
add_3_to_odds_list = [(i + 3) for i in int_list if i % 2 == 1]
print(add_3_to_odds_list)

#                 (formatting) collection (if) = condition
add_3_to_evens_list = [str(i) for i in int_list if i % 2 == 0]
print(add_3_to_evens_list)
