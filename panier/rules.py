import pandas as pd

class Arules:
    """

    """

    def __init__(self, list_itemsets: list, support_itemsets: dict):
        self.list_itemsets = list_itemsets
        self.support_itemsets = support_itemsets
        self.reset()

    def reset(self):
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
        deno = self.support(tg, ()) * self.support(td, ())
        return self.support(tg, td) / deno if deno != 0 else 0

    def leverage(self, tg: tuple, td: tuple) -> float:
        return self.support(tg, td) - (self.support(tg, ()) * self.support((), td))

    def conviction(self, tg: tuple, td: tuple) -> float:
        conf = self.confidence(tg, td)
        if conf == 1:
            return None
        else:
            return (1 - self.support((), td)) / (1 - conf) if (1 - conf) != 0 else 0

    
    def lift_diag(self, tg: tuple, td: tuple) -> str:
        value = self.lift(tg, td)
        
        if value == 1:
            message = f"{tg} -> {td} ne pas utiliser"
        elif value < 1:
            message = f"{tg} et {td} ne peuvent pas co-exister dans une règle"
        else:
            message = f"{tg} -> {td} est prédictive"

        return message

    def validation_rules(self, itemset: tuple, rhs_list: list, min_confidence: float) -> list:
        accepted_rhs = []
        for rhs in rhs_list:
            lhs = tuple(sorted(set(itemset) - set(rhs)))
            confidence = self.confidence(lhs, rhs)
            if confidence >= min_confidence:
                self.rules.append((lhs, rhs))
                accepted_rhs.append(rhs)
        return accepted_rhs


    def cross_product(self, L: list, k: int) -> list:
        new_itemsets = []
        for i in range(len(L)):
            for j in range(i + 1, len(L)):
                if L[i][:k - 1] == L[j][:k - 1]:
                    new_itemset = L[i] + (L[j][k - 1],)
                    new_itemsets.append(new_itemset)
                else:
                    break
        return new_itemsets

    def build_rules(self, lk:tuple, rhs_list: list, min_confidence: float):
        size_lk = len(lk)
        size_rhs = 1
        local = rhs_list

        while len(local) > 1 and size_lk > size_rhs + 1:
            local = self.cross_product(local, size_rhs)
            local = self.validation_rules(lk, local, min_confidence)
            size_rhs += 1

    def generate_rules(self, min_confidence: float):
        self.rules = []
        for itemsets_of_size_k in self.list_itemsets[1:]:
            for itemset in itemsets_of_size_k:
                rhs_list = [(item,) for item in itemset]
                if len(itemset) == 2:
                    self.validation_rules(itemset, rhs_list, min_confidence)
                else:
                    self.build_rules(itemset, rhs_list, min_confidence)

    def main(self, min_confidence: float) -> pd.DataFrame:
        results = []
        self.generate_rules(min_confidence)
        for lhs, rhs in self.rules:
            lhs_support = self.support(lhs, ())
            rhs_support = self.support((), rhs)
            support = self.support(lhs, rhs)
            confidence = self.confidence(lhs, rhs)
            lift = self.lift(lhs, rhs)
            leverage = self.leverage(lhs, rhs)
            conviction = self.conviction(lhs, rhs)
            if conviction is None:
                conviction = float('inf')
            results.append((lhs, rhs, lhs_support, rhs_support, support, confidence, lift, leverage, conviction))

        df = pd.DataFrame(results, columns=['lhs', 'rhs', 'lhs_support', 'rhs_support', 'support', 'confidence', 'lift', 'leverage', 'conviction'])
        return df[df['confidence'] >= min_confidence].reset_index(drop=True)
