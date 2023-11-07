class calculator:
    """calculator class"""
    def __init__(self, object) -> None:
        """initialisation of class"""
        self.object = object

    @classmethod
    def dotproduct(self, V1: list[float], V2: list[float]) -> None:
        """function dot product"""
        result = 0.0
        for i in range(len(V1)):
            result = result + V1[i] * V2[i]
        print(f"Dot product is : {int(result)}")

    @classmethod
    def add_vec(self, V1: list[float], V2: list[float]) -> None:
        """function that add vector"""
        new_vector = []
        for i in range(len(V1)):
            new_vector.append(float(V1[i] + V2[i]))
        print(f"Add Vector is : {[x for x in new_vector]}")

    @classmethod
    def sous_vec(self, V1: list[float], V2: list[float]) -> None:
        """function that apply sub"""
        new_vector = []
        for i in range(len(V1)):
            new_vector.append(float(V1[i] - V2[i]))
        print(f"Sous Vector is : {new_vector}")
