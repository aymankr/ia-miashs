class Arules:
    """

    """

    def __init__(self, list_itemsets : list, support_itemsets: dict):
        self.list_itemsets = list_itemsets
        self.support_itemsets = support_itemsets
        self.reset()

    def reset(self):
        """
        """
        self.rules = []

    def support(self, tg : tuple, td : tuple) -> float:
        return self.support_itemsets.get(tuple(set(tg + td)))

    def confidence(self, tg : tuple, td : tuple) -> float:
        return self.support(tg, td) / self.support(tg, ())

    def lift(self, tg : tuple, td : tuple) -> float:
        return self.support(tg, td) / \
            (self.support(tg, ())*self.support(td, ()))

    def leverage(self, tg : tuple, td : tuple) -> float:
        return self.support(tg, td) - (self.support(tg, ()) * self.support((), td))

    def conviction(self, tg : tuple, td : tuple) -> float:
        if (1 - self.confidence(tg, td)) != 0:
            return (1 - self.support((), td)) / \
                (1 - self.confidence(tg, td))
        else:
            return 0
    
    def lift_diag(self, tg : tuple, td : tuple):
        value = self.lift(tg, td)
        
        if value == 1:
            message = f"{tg} -> {td} ne pas utiliser"
        elif value < 1:
            message = f"{tg} et {td} ne peuvent pas co-exister dans une règle"
        else:
            message = f"{tg} -> {td} est prédictive"

        return message
        
    def generate_rules(self, min_confidence):
        self.rules = []

        for itemset_list in self.list_itemsets[1:]:
            for ref_itemset in itemset_list:
                k = len(ref_itemset)
                ref_items = [(item,) for item in ref_itemset]

                if k == 2:
                    self.rules += self.validation_rules(ref_itemset, ref_items, min_confidence)
                else:
                    self.rules += self.build_rules(ref_itemset, ref_items, min_confidence)

        return self.rules

    def build_rules(self, ref_itemset, rhs_p, min_confidence):
        local_rules = []
        k = len(ref_itemset)

        if k > len(rhs_p[0]) + 1:
            rhs_q = self.cross_product(rhs_p)
            local_rules += self.validation_rules(ref_itemset, rhs_q, min_confidence)
            local_rules += self.build_rules(ref_itemset, rhs_q, min_confidence)

        return local_rules

    def validation_rules(self, itemset, candidates, min_confidence):
        valid_rules = []
        accepted_rhs = []
        for rhs in candidates:
            lhs = tuple(sorted(set(itemset) - set(rhs)))
            conf = self.confidence(lhs, rhs)
            if conf >= min_confidence:
                rule = (lhs, rhs)
                valid_rules.append(rule)
                self.rules.append(rule)
                accepted_rhs.append(rhs)

        return accepted_rhs

    def cross_product(self, L):
        rep = []
        taille = len(L)

        for i in range(taille - 1):
            j = i + 1
            while j < taille and L[i][:-1] == L[j][:-1]:
                nouveau = L[i] + (L[j][-1],)

                all_subsets_present = True
                for x in range(len(nouveau)):
                    sub_itemset = nouveau[:x] + nouveau[x + 1:]
                    if sub_itemset not in L:
                        all_subsets_present = False
                        break

                if all_subsets_present:
                    rep.append(nouveau)

                j = j + 1

        return rep
