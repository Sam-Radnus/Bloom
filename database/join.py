from multiprocessing import get_all_start_methods
from .table import Table

class Join:
    def __init__(self, left:Table, right:Table):
        self.left_table = left
        self.right_table = right

    def left_join(self):
        ans = []

        lfk = self.left_table.foreign_attr[0]
        rfk = self.left_table.foreign_attr[1]

        for l_el in self.left_table.all():
            for r_el in self.right_table.all():
                pass
        return ans


    def right_join(self):
        pass

    def natural_join(self):
        pass