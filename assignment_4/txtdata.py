from helper import *
import copy

class TxtData :
    """ docstring """
    def __init__(self, data) :
        """ docstring """
        self.data = copy.deepcopy(data)
        self.rows = len(data)
        self.cols = len(data[0])
        
    def __str__(self) :
        """ docstring """
        rows = str(self.rows)
        cols = str(self.cols)
        
        return "This TxtData object has " + rows + " rows and " + cols + " columns."

    def get_pixels(self) :
        """ docstring """
        pixels = self.rows * self.cols
        
        return pixels

    def get_data_at(self,row, col) :
        """ docstring """
        if row in range(len(self.data)) and col in range(len(self.data[0])) :
            position_item = self.data[row][col]
        else :
            raise ValueError("Index out of bound!")

        return position_item


    def pretty_save(self, file_name) :
        """ docstring """
        pretty_file = open(file_name, 'w')
        for row in self.data :
            pretty_line = ""
            for value in row :
                if value == 1 :
                    pretty_line += "\u2588" * 2
                elif value == 0 :
                    pretty_line += "  "
            pretty_file.write(pretty_line + '\n')
        pretty_file.close()
        
    def equals(self, another_data) :
        """ docstring """
        return another_data.data == self.data

    def approximately_equals(self, another_data, precision) :
        """ docstring """
        inconsistents = 0
        pixels = int(another_data.get_pixels())
        if another_data.get_pixels() != self.get_pixels() :
            return False
        
        for i in range(len(self.data)) :
            for j in range(len(self.data[i])) :
                if self.data[i][j] != another_data.data[i][j] :
                    inconsistents += 1
        
        if (inconsistents / pixels) > precision :
            return False
        
        return True       
        
        
        
        
        
        
        
