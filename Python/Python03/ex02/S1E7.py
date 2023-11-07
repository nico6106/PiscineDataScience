from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False

    def __str__(self):
        """__str__ for class"""
        return f"Vector ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """__repr__ for class"""
        return f"Vector ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """Creating a lannister"""
        cls.first_name = first_name
        cls.is_alive = is_alive
        return cls(first_name, is_alive)

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False

    def __str__(self):
        """__str__ for class"""
        return f"Vector ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """__repr__ for class"""
        return f"Vector ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
