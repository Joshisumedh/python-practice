# Python program to illustrate different set op.
set_A = set(map(int, input("Enter elements of Set A : ").split()))
set_B = set(map(int, input("Enter elements of Set B : ").split()))

union_set = set_A.union(set_B)
print("Union of Set A and Set B : ", union_set)

intersection_set = set_A.intersection(set_B)
print("intersection of Set A and Set B: ",intersection_set)

is_subset = set_A.issubset(set_B)
print("Is Set A a subset of Set B?", is_subset)

difference_set = set_A.difference(set_B)
print("Difference of A and B (A - B): ", difference_set)