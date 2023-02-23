
class Apriori:
    """

    """

    def __init__(self, param: dict):
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
        self.current = {}
        
        for x in self.dbase:
            self.candidates[x] = [(a,) for a in self.dbase[x]]
        
        for x, v in self.candidates.items():
            for itemset in v:
                if itemset in self.current:
                    self.current[itemset].add(x)
                else:
                    self.current[itemset] = set([x])

    def support(self, minsupp :float) -> dict:
        assert 0 <= minsupp <= 1
        """on fait le nombre d'occurrences divisées par la taille de la base
        len(dbase) taille de la base 
        pr connaitre nb de transactions on calcule la longueur de current(x)
        """
        a = {x: len(v) / len(self.dbase) for x, v in self.current.items()}
        return {x: v for x, v in a.items() if v >= minsupp}

    def scan_dbase(self, minsupp :float):
        assert 0 <= minsupp <= 1
        """
        mettre à jour support_history avec update en fonction de la
        fréquence en paramètre, mettre à jour current
        """
        self.support_history.update(self.support(minsupp))
        self.current = {x: v for x, v in self.current.items() if x in self.support_history.keys()}

    def Lk(self) -> list:
        """
        renvoie la liste triée des clés de self.current
        """
        return sorted(self.current.keys())

    def cross_product(self):
        Lk = self.Lk()
        k = self.candidates_sz
        p = len(self.current)

        futur = {}
        keys = sorted(self.current.keys())
        for i in range(p):
            for j in range(i+1, p):
                itemset_i = keys[i]
                itemset_j = keys[j]
                if (itemset_i[:k-1] == itemset_j[:k-1]):
                    new = itemset_i + (itemset_j[-1], )
                    if all((x,) in Lk for x in new):
                        tid_i = self.current[itemset_i]
                        tid_j = self.current[itemset_j]
                        futur[new] = tid_i.intersection(tid_j)

        self.current = futur
        self.candidates = {}

        tids = list({x for v in self.current.values() for x in v})
        for tid in tids:
            self.candidates[tid] = [k for k, v in self.current.items() if tid in v]
        self.candidates_sz += 1

    def main(self, minsupp) -> list:
        assert 0 <= minsupp <= 1