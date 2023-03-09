class Arules:
    """

    """

    def __init__(self, list_itemsets : list, support_itemsets: dict):
        self.list_itemsets = list_itemsets
        self.support_itemsets = support_itemsets
        self.reset()
        self.support((), ())

    def reset(self):
        """
        """
        self.rules = []

    def support(self, tg : tuple, td : tuple) -> float:
        print("xDDD 1  ", self.list_itemsets)
        print("XDDD 2", self.support_itemsets)
        # faire union
        # [(2,5), (3,)
        # dans {100:[1, 3, 4], 200:[2, 3, 5], 300:[1, 2, 3, 5], 400:[2, 5]}
        return 0

    def confidence(self, tg : tuple, td : tuple) -> float:
        pass

    def lift(self, tg : tuple, td : tuple) -> float:
        pass

    def leverage(self, tg : tuple, td : tuple) -> float:
        pass

    def conviction(self, tg : tuple, td : tuple) -> float:
        pass