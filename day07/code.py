### day-07
# sets
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# exercice 1
print("exercice-1")
# 1
print(len(it_companies))
# 2
it_companies.add("Twitter")
# 3
it_companies.update(["Heroku", "Linode", "Render"])
print(it_companies)
# 4
it_companies.remove("Twitter")
print(it_companies)
# 5
it_companies.discard("Twitter")
print(it_companies)
# discard do not raise error if element doesn't exist in the set


# exercice 2
# 1
print("exercice-2")
print(A.union(B))
# 2
print(A.intersection(B))
# 3
print(A.issubset(B))
# 4
print(A.isdisjoint(B))
# 5
A.update(B)
print(A)
B.update(A)
print(B)
# 6
print(A.symmetric_difference(B))  # empty set
# 7
del A, B
# exercice 3
print("exercice-3")
# 1
age_set = set(age)
print(len(age) > len(age_set))  # list length is bigger that set length
# 2
# string,particulary in python, like the other types (list, set, tuple) may be, i say may be considered as a list of joined character, proof, it support indexing, slicing
# about differences
# set: can contains only one occurence of specific data (eg: only one 1, only one "s")
# tuple: doesn't support muttation
# list: is collection of data

# 3
sentence = "I am a teacher and I love to inspire and teach people"
sentence_words = set(sentence.split(" "))
print(sentence_words)
print(len(sentence_words))
