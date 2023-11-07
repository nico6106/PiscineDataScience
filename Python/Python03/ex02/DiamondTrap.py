from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King class"""
    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes):
        """setter for eyes"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """setter for hairs"""
        self.hairs = hairs

    def get_eyes(self):
        """getter for eyes"""
        return self.eyes

    def get_hairs(self):
        """getter for hairs"""
        return self.hairs
