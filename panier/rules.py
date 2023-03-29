class Arules:
    """

    """

    def __init__(self, list_itemsets: list, support_itemsets: dict):
        self.list_itemsets = list_itemsets
        self.support_itemsets = support_itemsets
        self.reset()

    def reset(self) -> None:
        """
        """
        self.rules = []

    def support(self, tg: tuple, td: tuple) -> float:
        return self.support_itemsets.get(tuple(set(tg).union(set(td))), 0)

    def confidence(self, tg: tuple, td: tuple) -> float:
        try:
            return self.support(tg, td) / self.support(tg, ())
        except ZeroDivisionError:
            return 0

    def lift(self, tg: tuple, td: tuple) -> float:
        return self.support(tg, td) / \
            (self.support(tg, ())*self.support(td, ()))

    def leverage(self, tg: tuple, td: tuple) -> float:
        return self.support(tg, td) - (self.support(tg, ()) * self.support((), td))

    def conviction(self, tg: tuple, td: tuple) -> float:
        if (1 - self.confidence(tg, td)) != 0:
            return (1 - self.support((), td)) / \
                (1 - self.confidence(tg, td))
        else:
            return 0
    
    def lift_diag(self, tg: tuple, td: tuple) -> str:
        value = self.lift(tg, td)
        
        if value == 1:
            message = f"{tg} -> {td} ne pas utiliser"
        elif value < 1:
            message = f"{tg} et {td} ne peuvent pas co-exister dans une règle"
        else:
            message = f"{tg} -> {td} est prédictive"

        return message
        
    def cross_product(self, rhs_list: list) -> list:
        new_rhs_list = []
        for i in range(len(rhs_list)):
            for j in range(i+1, len(rhs_list)):
                if rhs_list[i][:-1] == rhs_list[j][:-1]:
                    new_rhs = rhs_list[i] + (rhs_list[j][-1],)
                    new_rhs_list.append(new_rhs)
                else:
                    break
        return new_rhs_list

    def validation_rules(self, itemset: tuple, rhs_list: list, min_confidence: float) -> list:
        accepted_rhs = []
        for rhs in rhs_list:
            lhs = tuple(sorted(set(itemset) - set(rhs)))
            confidence = self.support_itemsets[itemset] / self.support_itemsets[lhs]
            if confidence >= min_confidence:
                self.rules.append((lhs, rhs))
                accepted_rhs.append(rhs)
        return accepted_rhs

    def build_rules(self, itemset: tuple, rhs_list: list, min_confidence: float) -> list:
        generated_rules = []
        size_itemset = len(itemset)
        size_rhs = 1

        while len(rhs_list) > 1 and size_itemset > size_rhs + 1:
            rhs_list = self.cross_product(rhs_list)
            rhs_list = self.validation_rules(itemset, rhs_list, min_confidence)
            generated_rules += [(tuple(sorted(set(itemset) - set(rhs))), rhs) for rhs in rhs_list]
            size_rhs += 1

        return generated_rules    
    
    def generate_rules(self, min_confidence: float) -> None:
            self.rules = []
            for itemsets_of_size_k in self.list_itemsets[1:]:
                for itemset in itemsets_of_size_k:
                    rhs_list = [(item,) for item in itemset]
                    if len(itemset) == 2:
                        self.rules += self.validation_rules(itemset, rhs_list, min_confidence)
                    else:
                        self.rules += self.build_rules(itemset, rhs_list, min_confidence)