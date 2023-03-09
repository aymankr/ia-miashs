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

# data = {'a': [3,5,7], 'b':[3,5], 'c':[7,3], 'd':[5,7], 'e': [7,5],
#                'f': [7,3,5], 'g':[7,5,3]}
# db = Apriori(data)
# print("main(.3)", db.main(.5))
# print("candidates_sz", db.candidates_sz)
# print("support_history", db.support_history)
# print("candidates", db.candidates)
# print("current", db.current)


"""
        'candidates': {
            'g': [(3, 5), (3, 7), (5, 7)],
            'f': [(3, 5), (3, 7), (5, 7)],
            'a': [(3, 5), (3, 7), (5, 7)],
            'b': [(3, 5)],
            'c': [(3, 7)],
            'd': [(5, 7)],
            'e': [(5, 7)]},
        'current': {
            (3, 5): {'g', 'f', 'a', 'b'},
            (3, 7): {'g', 'f', 'c', 'a'},
            (5, 7): {'d', 'e', 'g', 'a', 'f'}
            }
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