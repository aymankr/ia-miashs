from apriori import Apriori

data = {100:[1, 3, 4], 200:[2, 3, 5], 300:[1, 2, 3, 5], 400:[2, 5]}
db = Apriori(data)
print("dbase", db.dbase)
print("candidates_sz", db.candidates_sz)
print("support_history", db.support_history)
print("candidates", db.candidates)
print("current", db.current)
print("main(.3)", db.main(.3))
print("candidates_sz", db.candidates_sz)
print("support_history", db.support_history)
print("candidates", db.candidates)
print("current", db.current)

"""
dbase {100: [1, 3, 4], 200: [2, 3, 5], 300: [1, 2, 3, 5], 400: [2, 5]}
candidates_sz 1
support_history {}
candidates {100: [(1,), (3,), (4,)], 200: [(2,), (3,), (5,)], 300: [(1,),
(2,), (3,), (5,)], 400: [(2,), (5,)]}
current {(1,): {100, 300}, (3,): {200, 100, 300}, (4,): {100}, (2,): {200,
300, 400}, (5,): {200, 300, 400}}
main(.3) [[(1,), (2,), (3,), (5,)], [(1, 3), (2, 3), (2, 5), (3, 5)], [(2,
3, 5)]]
candidates_sz 3
support_history {(1,): 0.5, (3,): 0.75, (2,): 0.75, (5,): 0.75, (1, 3): 0.5,
(2, 3): 0.5, (2, 5): 0.75, (3, 5): 0.5, (2, 3, 5): 0.5}
candidates {200: [(2, 3, 5)], 300: [(2, 3, 5)]}
current {(2, 3, 5): {200, 300}}
"""


# print("dbase", db.dbase)
# print("candidates_sz", db.candidates_sz)
# print("support_history", db.support_history)
# print("candidates", db.candidates)
# print("current", db.current)
# print("support(.7)", db.support(.7))
# print("support(.2)", db.support(.2))
# print("#{}#".format('='*73))
# db.scan_dbase(.7)
# print("support_history", db.support_history)
# print("current", db.current)
# print("Lk for size {}".format(db.candidates_sz), db.Lk())
# print("#{}#".format('='*73))
# db.cross_product()
# print("dbase", db.dbase)
# print("candidates_sz", db.candidates_sz)
# print("support_history", db.support_history)
# print("candidates", db.candidates)
# print("current", db.current)