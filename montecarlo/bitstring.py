import numpy as np
import math      
import copy as cp       

class BitString:
    """
    Simple class to implement a config of bits
    """
    def __init__(self, N):
        self.N = N
        self.config = np.zeros(N, dtype=int) 

    def __repr__(self):
        out = ""
        for i in self.config:
            out += str(i)
        return out

    def __eq__(self, other):        
        return all(self.config == other.config)
    
    def __len__(self):
        return len(self.config)

    def on(self):
        """
        Return number of bits that are on
        """
        result = 0
        for i in range(len(self.config)):
            if (self.config[i] == 1):
                result += 1
        return result

    def off(self):
        """
        Return number of bits that are off
        """
        result = 0
        for i in range(len(self.config)):
            if (self.config[i] == 0):
                result += 1
        return result


    def flip_site(self,i):
        """
        Flip the bit at site i
        """
        if (self.config[i] == 0):
            self.config[i] = 1
        elif (self.config[i] == 1):
            self.config[i] = 0
    
    def integer(self):
        """
        Return the decimal integer corresponding to BitString
        """
        result = 0
        for i in range(len(self.config)):
            power = len(self.config) - i - 1
            result += self.config[i] * (2 ** power)

        return result
 

    def set_config(self, s:list[int]):
        """
        Set the config from a list of integers
        """
        for i in range(len(self.config)):
            self.config[i] = s[i]


    def set_integer_config(self, dec:int):
        """
        convert a decimal integer to binary
    
        Parameters
        ----------
        dec    : int
            input integer
            
        Returns
        -------
        Bitconfig
        """
        for i in range(len(self.config)):
            power = len(self.config) - i - 1
            self.config[i] = (dec // (2 ** power)) % 2