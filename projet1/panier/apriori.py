
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
        
        newcurrent = {}
        for x, v in self.current.items():
            if x in self.support_history.keys():
                newcurrent