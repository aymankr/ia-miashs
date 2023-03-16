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
        return self.support(tg + td, ()) / self.support(tg, ())

    def lift(self, tg : tuple, td : tuple) -> float:
        return self.support(tg, td) / \
            (self.support(tg, ())*self.support(td, ()))

    def leverage(self, tg : tuple, td : tuple) -> float:
        # 
        pass

    def conviction(self, tg : tuple, td : tuple) -> float:
        return (1 - self.support((), td)) / \
            (1 - self.confidence(tg, td))