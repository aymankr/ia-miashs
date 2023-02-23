from apriori import Apriori

data = {100:[1, 3, 4], 200:[2, 3, 5], 300:[1, 2, 3, 5], 400:[2, 5]}
db = Apriori(data)
print("dbase", db.dbase)
print("candidates_sz", db.candidates_sz)
print("support_history", db.support_history)
print("candidates", db.candidates)
print("current", db.current)
print("support(.7)", db.support(.7))
print("support(.2)", db.support(.2))
print("#{}#".format('='*73))
db.scan_dbase(.7)
print("support_history", db.support_history)
print("current", db.current)
print("Lk for size {}".format(db.candidates_sz), db.Lk())
print("#{}#".format('='*73))
db.cross_product()
print("dbase", db.dbase)
print("candidates_sz", db.candidates_sz)
print("support_history", db.support_history)
print("candidates", db.candidates)
print("current", db.current)



"""
#=========================================================================#
dbase {100: [1, 3, 4], 200: [2, 3, 5], 300: [1, 2, 3, 5], 400: [2, 5]}
candidates_sz 2
support_history {(3,): 0.75, (2,): 0.75, (5,): 0.75}
candidates {200: [(2, 3), (2, 5), (3, 5)], 300: [(2, 3), (2, 5), (3, 5)],
400: [(2, 5)]}
current {(2, 3): {200, 300}, (2, 5): {200, 300, 400}, (3, 5): {200, 300}}

"""