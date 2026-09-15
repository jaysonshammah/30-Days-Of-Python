# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Find the length of the set it_companies
print("1. Length of it_companies:", len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("2. Added Twitter:", it_companies)

# 3. Insert multiple IT companies at once to the set
it_companies.update(['Samsung', 'Intel', 'Cisco'])
print("3. Added multiple companies:", it_companies)

# 4. Remove one of the companies from the set
it_companies.remove('IBM')
print("4. Removed IBM:", it_companies)

# 5. What is the difference between remove and discard?
print("5. Difference between remove() and discard():")
print("   - If you try to remove an item that doesn't exist using remove(), Python throws an error.")
print("   - If you use discard(), Python just ignores it and does nothing (no error).")

# 1. Join A and B
A_union_B = A.union(B)
print("L2-1. Join A and B:", A_union_B)

# 2. Find A intersection B
A_intersect_B = A.intersection(B)
print("L2-2. Intersection of A and B:", A_intersect_B)

# 3. Is A a subset of B?
is_subset = A.issubset(B)
print("L2-3. Is A a subset of B?", is_subset)

# 4. Are A and B disjoint sets? (Do they have no elements in common?)
is_disjoint = A.isdisjoint(B)
print("L2-4. Are A and B disjoint?", is_disjoint)

# 5. Join A with B and B with A
# Note: Since sets are unordered, joining A to B and B to A gives the exact same result.
print("L2-5. Join A with B:", A.union(B))
print("      Join B with A:", B.union(A))

# 6. What is the symmetric difference between A and B?
# (Items in A or B, but NOT in both)
sym_diff = A.symmetric_difference(B)
print("L2-6. Symmetric difference:", sym_diff)

# 7. Delete the sets completely
del A
del B
print("L2-7. Sets A and B have been deleted.")

age_set = set(age)
list_len = len(age)
set_len = len(age_set)
print(f"L3-1. List length: {list_len}, Set length: {set_len}")
print("      The List is bigger because the Set removed all duplicate ages.")

print("L3-2. Data Type Differences:")
print("      - String: Ordered collection of characters. Immutable (cannot be changed).")
print("      - List: Ordered collection of items. Mutable (can be changed). Allows duplicates.")
print("      - Tuple: Ordered collection of items. Immutable (cannot be changed). Allows duplicates.")
print("      - Set: Unordered collection of items. Mutable. DOES NOT allow duplicates.")

# 3. How many unique words have been used in the sentence?
sentence = "I am a teacher and I love to inspire and teach people."
# First, remove the period so 'people.' and 'people' aren't treated differently if they both appeared
clean_sentence = sentence.replace('.', '') 
# Split into a list of words, then convert to a set to remove duplicates
words_list = clean_sentence.split(' ')
unique_words = set(words_list)

print("L3-3. Unique words:", unique_words)
print("      Number of unique words:", len(unique_words))