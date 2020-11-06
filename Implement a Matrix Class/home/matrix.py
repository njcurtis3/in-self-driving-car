import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
    
# This is the dot product for __mul__
def dot_product(vector_one, vector_two):
    if len(vector_one) != len(vector_two):
        print("vectors must have same length")

    n = len(vector_one)

    total = 0
    for i in range(n):
        vector_one_i = vector_one[i]
        vector_two_i = vector_two[i]
        total = total + vector_one_i * vector_two_i

    return total


# CLASS--------------------------------------------------------

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #----------------------------------------------------------------
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here ------------------------------------------------------------------------------------
        
        if self.h == 2:
            a = self.g[0][0] 
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            # ex.)∣A∣=1*1 - 0*0
            
            #determinant value mult.  diagonal elements of 2x2 matrix. subtract multiplied  elements of the diagonals. 
            determVal = a*d - b*c
            return determVal
        
        if self.h == 1:
            determVal = self.g[0][0]
            return determVal
        
        
        
        #END---------------------------------------------------------------------------------------------------------

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here -----------------------------------------------------------------------------------------
        
        
        sum_trace = 0
        
        for i in range(self.h):
            for j in range(self.w):
                if i == j:           # Diagonals are ones
                    sum_trace = sum_trace + self.g[i][j]
        
        return sum_trace       
        
        
        # END -----------------------------------------------------------------------------------------------------------

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here-------------------------------------------------------------------------------------------
      
    
        #1x1 Matrix
        if (self.h) == 1:
            inverse_m = zeroes(1,1) # create a matrix of zeroes for inverse_m
            inverse_m[0][0] = 1/self.g[0][0]
            
            
            return inverse_m
        
            
            # 2x2 Matrix
        if self.h == 2:
            inverse_m = zeroes(2,2) # create a matrix of zeroes for inverse_m
            determVal = self.determinant()
            # diagonal elements of 2x2 matrix, and referencing the determinant function
            inverse_m[0][0] = self.g[1][1] * (1/determVal)
            inverse_m[0][1] = -self.g[0][1] * (1/determVal)
            inverse_m[1][0] = -self.g[1][0] * (1/determVal)
            inverse_m[1][1] = self.g[0][0] * (1/determVal)    
            
            return inverse_m
        
       #attribution: https://integratedmlai.com/find-the-determinant-of-a-matrix-with-pure-  python-without-numpy-or-scipy/. Took understanding from sentence "For any 2 x 2 matrix, the determinant is a scalar value equal to the product of the main diagonal elements minus the product of it’s counter diagonal elements."
        
        
        #END -------------------------------------------------------------------------------------------------------------

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here ------------------------------------------------------------------------------------------
        
        tp_matrix = zeroes(self.w,self.h)
        
        for j in range(self.w):
            for i in range(self.h):
                tp_matrix[j][i] = self.g[i][j] # changing matrix[i][j] to matrix [j][i]
            
        return tp_matrix
        
        
        
      #END ---------------------------------------------------------------------------------------------------------------  
        
        

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here --------------------------------------------------------------------------------------------
        
  
        matrix_sum = zeroes(self.h, self.w)
        
        # iterate through rows [i]
        for i in range(self.h):
            # iterate through columns [j]
            for j in range(self.w):
                matrix_sum_add = self.g[i][j] + other.g[i][j] # add rows and columns together [i][j]
            return matrix_sum
        
        
        
        
        
        #END ---------------------------------------------------------------------------------------------------------------

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here --------------------------------------------------------------------------------------------
        
        matrix_neg = zeroes(self.h,self.w)
        
        for i in range(self.h):
            for j in range(self.w):
                matrix_neg[i][j] = (-1 * self.g[i][j]) #negate matrix[i][j]
            
        return matrix_neg
        
        
        
        
        #END ---------------------------------------------------------------------------------------------------------------

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here -----------------------------------------------------
        
        other_negative = - other
        
        result_subtract = self + zeroes(self.h,self.w)
        
        return result_subtract
        
        
        
        
        #END ------------------------------------------------------------------------

    def __mul__(self, other):
        
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here-------------------------------------------------------------------------------------------    
         
            
        result_mult = zeroes(self.h,other.w)
        
        other_transp = other.T()
        
        for i in range (self.h):
            for j in range (other_transp.h):
                result_mult[i][j] = dot_product(self.g[i],other_transp.g[j]) 
        return result_mult
    
    
        
        # END ------------------------------------------------------------------------------------------------------------

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here --------------------------------------------------
            
            result_rmul = zeroes(self.h,self.w)
            
            for i in range(self.h):
                for j in range(self.w):
                    result_rmul[i][j] = (other*self.g[i][j])
            
            return result_rmul
            
            #implemented if an attempt is made it call the left objects __mul__, and it doenst work with the right operand in question. Multiplication is commutative. 
            
            #END ---------------------------------------------------------------------
            