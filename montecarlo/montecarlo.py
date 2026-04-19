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


class IsingHamiltonian:
    def __init__(self, Graph):
        self.Graph = Graph
        self.N = len(Graph)
        self.mus = np.zeros(self.N)
        self.bs = BitString(len(self.mus))
        self.bs.set_config(self.mus)
        self.J = Graph

    def energy(self, config: BitString):
        E = 0.0
        # spin up = +1 = 1
        # spin down = -1 = 0
        for e in self.Graph.edges:
            index_i = e[0]
            index_j = e[1]
            weight = self.Graph.edges[e]['weight']

            spin_i = config.config[index_i]
            spin_j = config.config[index_j]

            if (spin_i == 0):
                spin_i = -1
            
            if (spin_j == 0):
                spin_j = -1

            E += spin_i * spin_j * weight

        for i in range(len(config.config)):
            spin_i = config.config[i]
            if (spin_i == 0):
                spin_i = -1

            E += self.mus[i] * spin_i

        return E

    def set_mu(self, mus: np.array):
        self.mus = mus

    def compute_average_values(self, T: int):
        E  = 0.0
        M  = 0.0
        Z  = 0.0
        EE = 0.0
        MM = 0.0
        
        for i in range(2**len(self.bs.config)):
            self.bs.set_integer_config(i)
            energy_i = self.energy(self.bs)
            Z += math.exp(-energy_i / T)
            
        E_2 = 0.0
        M_2 = 0.0

        for i in range(2**len(self.bs.config)):
            self.bs.set_integer_config(i)
            energy_i = self.energy(self.bs)
            magnetization_i = self.bs.on() - self.bs.off()
            P_i = math.exp(-energy_i / T) / Z

            E += energy_i * P_i
            M += magnetization_i * P_i
            
            EE += energy_i**2 * P_i
            MM += magnetization_i**2 * P_i

            E_2 += energy_i * energy_i * P_i
            M_2 += magnetization_i * magnetization_i * P_i

        HC = (E_2 - E ** 2) * (T ** -2)
        MS = (M_2 - M ** 2) * (T ** -1)

        
        return E, M, HC, MS
    
class MonteCarlo:
    def __init__(self, hamiltonian):
        self.ham = hamiltonian
        self.config = BitString(self.ham.N)

    def step(self, T):
        i = np.random.randint(0, self.ham.N)

        old_energy = self.ham.energy(self.config)
        self.config.flip_site(i)
        new_energy = self.ham.energy(self.config)

        dE = new_energy - old_energy

        if (dE > 0 and np.random.rand() > np.exp(-dE / T)):
            self.config.flip_site(i)

    def run(self, T, n_samples=1000, n_burn=100):
        for _ in range(n_burn):
            self.step(T)

        energies = []
        magnetizations = []

        for _ in range(n_samples):
            self.step(T)
            energies.append(self.ham.energy(self.config))
            magnetizations.append(self.config.on() - self.config.off())

        return np.array(energies), np.array(magnetizations)