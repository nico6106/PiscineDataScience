class calculator:
    """calculator class"""
    def __init__(self, object) -> None:
        """initialisation of class"""
        self.object = object

    def __add__(self, value) -> None:
        """addition"""
        for i in range(len(self.object)):
            self.object[i] = self.object[i] + value
        print(self.object)
        return

    def __mul__(self, value) -> None:
        """multiplication"""
        for i in range(len(self.object)):
            self.object[i] = self.object[i] * value
        print(self.object)
        return

    def __sub__(self, value) -> None:
        """soustraction"""
        for i in range(len(self.object)):
            self.object[i] = self.object[i] - value
        print(self.object)
        return

    def __truediv__(self, value) -> None:
        """division"""
        if value == 0:
            print('Error: Division by 0')
            return
        for i in range(len(self.object)):
            self.object[i] = self.object[i] / value
        print(self.object)
        return
