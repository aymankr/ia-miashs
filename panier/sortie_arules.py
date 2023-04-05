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

## generate
print("{0} generate_rules {0}".format('*=*'))
data = {100:[1, 3, 4], 200:[2, 3, 5], 300:[1, 2, 3, 5], 400:[2, 5]}
db = Apriori(data)
br = Arules(db.main(.5), db.support_history)
for k in (.75, .5, .25, .1):
    print("min confiance", k)
    print("rules before generation", br.rules)
    _out = br.generate_rules( k )
    print("rules after generate_rules", br.rules)
    print("return of generate_rules ?", _out)
    print("*"*17)
## validate 
data = {100:[1, 3, 4], 200:[2, 3, 5], 300:[1, 2, 3, 5], 400:[2, 5]}
db = Apriori(data)
br = Arules(db.main(.5), db.support_history)
print("rules before validation", br.rules)
_candidates = [(2,), (3,), (5,), (2,3), (2,5), (3,5)]
threshold = 3/4
print("candidates {} and minConfidence is {:.2f}"
"".format(_candidates, threshold))
_out = br.validation_rules((2,3,5), _candidates, threshold)
print("rules after validation", br.rules)
print("accepted rhs", _out)

print("#" * 40)

## verif build_rules
"""
data = {1: ([[(1,), (2,), (3,), (4,)], [ (1,2), (1,4), (2,3)]], 
		{(1,): .5, (2,): .5, (3,): .5, (4,): .5, 
		 (1,2): .3, (1,4): .25, (2,3): .4}),
           2: ([[(1,), (2,), (3,), (5,)],
                [(1, 3), (2, 3), (2, 5), (3, 5)], [(2, 3, 5)]],
               {(1,): 0.5, (3,): 0.75, (2,): 0.75, (5,): 0.75,
                (1, 3): 0.5, (2, 3): 0.5, (2, 5): 0.75, (3, 5): 0.5,
                (2, 3, 5): 0.5}),
           3: ([[(3,), (5,), (7,)], [(5, 7)]],
               {(3,): 0.71, (5,): 0.86, (7,): 0.86, (5, 7): 0.71}),
           4: ([[(1,), (2,), (3,), (4,), (5,), (6,), (7,)],
                [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4),
                 (3, 4), (3, 5), (4, 5), (6, 7)],
                [(1, 2, 3), (1, 2, 4), (3, 4, 5)]],
               {(1,): 0.43, (2,): 0.57, (3,): 0.43, (4,): 0.57,
                (5,): 0.43, (6,): 0.29, (7,): 0.29, (1, 2): 0.43,
                (1, 3): 0.29, (1, 4): 0.29, (2, 3): 0.29, (2, 4): 0.29,
                (3, 4): 0.29, (3, 5): 0.29, (4, 5): 0.43, (6, 7): 0.29,
                (1, 2, 3): 0.29, (1, 2, 4): 0.29, (3, 4, 5): 0.29}),
           5: ([[(1,), (2,), (3,), (4,), (5,)], [(1, 2), (4, 5)]],
               {(1,): 0.43, (2,): 0.57, (3,): 0.43, (4,): 0.57, (5,): 0.43,
                (1, 2): 0.43, (4, 5): 0.43}),
           }

for items in data.items():
    ar = Arules(*items[1])
    lk = (2,3,5)
    rhs_p = [(2,), (3,), (5,)]
    min_conf = 0.5
    ar.build_rules(lk, rhs_p, min_conf)
    print("Liste des itemsets après build_rules :", ar.list_itemsets)
    print("Support des itemsets après build_rules :", ar.support_itemsets)
    print("Règles après build_rules :", ar.rules)
    for conf in [1.0, 0.75, 0.5]:
        print(f"minConf: {conf}")
        ar.generate_rules(conf)
        print(f"Nombre de règles générées: {len(ar.rules)}")
        print("Règles générées :", ar.rules)
        print(items[0])
        print("#" * 30)
"""

## main
data = {100:[1, 3, 4], 200:[2, 3, 5], 300:[1, 2, 3, 5], 400:[2, 5]}
db = Apriori(data)
br = Arules(db.main(.5), db.support_history)
for k in range(1, 7):
    _ = br.main(1/k)
    print("min confidence 1/{}={:.3f}".format(k,1/k))
    print(_.head())
    print('*'*7)
