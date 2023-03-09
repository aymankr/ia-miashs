
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

    def support(self, minsupp: float) -> dict:
        assert 0 <= minsupp <= 1
        """on fait le nombre d'occurrences divisées par la taille de la base
        len(dbase) taille de la base 
        pr connaitre nb de transactions on calcule la longueur de current(x)
        """
        a = {x: len(v) / len(self.dbase) for x, v in self.current.items()}
        return {x: v for x, v in a.items() if v >= minsupp}

    def scan_dbase(self, minsupp: float):
        """
        mettre à jour support_history avec update en fonction de la
        fréquence en paramètre, mettre à jour current
        """
        new_support = self.support(minsupp)
        self.support_history.update(new_support)
        self.current = {x: v for x, v in self.current.items(
        ) if x in new_support.keys()}

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
        for i in range(p):
            for j in range(i+1, p):
                if (Lk[i][:k-1] == Lk[j][:k-1]):
                    new = Lk[i] + (Lk[j][-1], )
                    if all(new[:m]+new[m+1:] in Lk for m in range(k+1)):
                        tid_i = self.current[Lk[i]]
                        tid_j = self.current[Lk[j]]
                        futur[new] = tid_i.intersection(tid_j)

        if futur:
            self.current = futur
            self.candidates = {}
    
            tids = list({x for v in self.current.values() for x in v})
            for tid in tids:
                self.candidates[tid] = [
                    w for w, v in self.current.items() if tid in v]
            self.candidates_sz += 1

    def main(self, minsupp: float) -> list:
        self.reset()
        main = []
        sz = self.candidates_sz
        while sz == self.candidates_sz:
            self.scan_dbase(minsupp)
            Lk = list(self.Lk())
            if Lk:
                main.append(Lk)
                self.cross_product()
            sz += 1
        return main
