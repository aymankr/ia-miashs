
class Apriori:
    """

    """
    def __init__(self, param : dict):
        self.dbase = param
        self.reset()

    def reset(self):
        """
        candidates = table TID ensembles d'itemsets
        current = table itemsets TIDs
        """
        self.candidates_sz = 1
        self.support_history = {}

        self.candidates = {}
        # = (tid:[ (x,), (y, ), ...], ...)
        for x in self.dbase:
            self.candidates[x] = [(a,) for a in self.dbase[x]]

        self.current = {}
        for x, v in self.candidates.items():
            for itemset in v:
                if itemset in self.current:
                    self.current[itemset].add(x)
                else:
                    self.current[itemset] = set([x])

    def support(self, minsupp):
        """on fait le nombre d'occurrences divisées par la taille de la base
        len(dbase) taille de la base 
        pr connaitre nb de transactions on calcule la longueur de current(x)
        """
        a = {x:len(v) / len(self.dbase) for x, v in self.current.items()}
        return {x:v for x, v in a.items() if v >= minsupp}

    def scan_dbase(self, minsupp):
        self.support_history.update(self.support(minsupp))
        self.current = {x:v for x, v in self.current.items() if x in self.support_history.keys()}
        
    def Lk(self):
      """
      renvoie la liste triée des clefs de self.current
      """
      return sorted(self.current.keys())
  





"""
    def cross_product(self):
            Lk = self.Lk()
            k = self.candidates_sz
            p = len(self.current)
            
            futur = {}
            for i in range(p-1):
                for j in range(i+1, p):
                    itemset_i = list(self.current.keys())[i]
                    itemset_j = list(self.current.keys())[j]
                    if itemset_i[:k-1] == itemset_j[:k-1]:
                        new = tuple(sorted(set(itemset_i + itemset_j)))
                        print(new)
                        in_Lk = True
                        for m in range(k):
                            subitem = new[:m] + new[m+1:]
                            if subitem not in Lk:
                                in_Lk = False
                                break
                        if in_Lk:
                            tidset_i = self.current[itemset_i]
                            tidset_j = self.current[itemset_j]
                            intersection = tidset_i.intersection(tidset_j)
                            if intersection:
                                futur[new] = intersection
            self.current = futur
            self.candidates_sz += 1
"""


"""
    def cross_product(self):
        self.candidates = {}
        for k1, v1 in self.current.items():
            for k2, v2 in self.current.items():
                if k1 != k2 and list(k1)[:self.candidates_sz-1] == list(k2)[:self.candidates_sz-1]:
                    new = k1 + k2[-1:]
                    all_subitems_in_Lk = True
                    for subitem in [new[:i] + new[i+1:] for i in range(self.candidates_sz)]:
                        if subitem not in self.current:
                            all_subitems_in_Lk = False
                            break
                    if all_subitems_in_Lk:
                        intersection = v1.intersection(v2)
                        if intersection:
                            self.candidates[new] = intersection
        self.candidates_sz += 1
        self.current = self.candidates
"""

    

"""
récupérer les itemsets de l'itération précédente (Lk)
récupérer la taille des itemsets (k)
récupérer le nombre d'itemsets (p)
creer futur = {}
pour i de 1 à p-1
j = i+1
tant que (j <= p
ET
les k-1 premières valeurs de itemset[i] et itemset[j] sont
identiques)
construire nouveau = itemset[i] + itemset[j][-1]
si tous les sous-items de nouveau de longueur k sont dans Lk alors
    futur[nouveau] = intersection(tid de itemset[i], tid de itemset[j])
si
j = j+1Et voici ce qui se passe après un appel à cross_product
On obtient :
ftq
current <- futur
mettre à jour candidates
mettre à jour candidates_sz
"""

"""
dbase {100: [1, 3, 4], 200: [2, 3, 5], 300: [1, 2, 3, 5], 400: [2, 5]}
candidates_sz 2
support_history {(3,): 0.75, (2,): 0.75, (5,): 0.75}
candidates {200: [(2, 3), (2, 5), (3, 5)], 300: [(2, 3), (2, 5), (3, 5)],
400: [(2, 5)]}
current {(2, 3): {200, 300}, (2, 5): {200, 300, 400}, (3, 5): {200, 300}}
"""