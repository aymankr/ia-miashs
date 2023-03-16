from apriori import Apriori
from rules import Arules

"""
sortie reset()
"""
ar = Arules([[(1,), (2,), (3,), (4,)], [ (1,2), (1,4), (2,3)]],
{(1,): .5, (2,): .5, (3,): .5, (4,): .5,
(1,2): .3, (1,4): .25, (2,3): .4})
print("items", ar.list_itemsets)
print("support", ar.support_itemsets)
print("regles", ar.rules)
print("{0} Exemple 2 {0}".format("="*7))
data = {100:[1, 3, 4], 200:[2, 3, 5], 300:[1, 2, 3, 5], 400:[2, 5]}
db = Apriori(data)
br = Arules(db.main(.5), db.support_history)
print("items", br.list_itemsets)
print("support", br.support_itemsets)
print("regles", br.rules)

"""
sortie lift()
"""
data = {100:[1, 3, 4], 200:[2, 3, 5], 300:[1, 2, 3, 5], 400:[2, 5]}
db = Apriori(data)
br = Arules(db.main(.5), db.support_history)
print("#=== Evaluation des règles à partir du triplet (2,3,5) ===#")
for lhs,rhs in [ [(2,5), (3,)], [(2,3), (5,)], [(3,5), (2,)] ]:
    print("evaluation de {} -> {}".format(lhs, rhs))
    for m in "support confidence conviction leverage lift lift_diag".split():
        _r = getattr(br, m)(lhs, rhs)
        _r = round(_r, 3) if isinstance(_r, float) else _r
        print("{} : {}".format(getattr(br, m).__name__, _r))
        print("#"+"="*73+"#")