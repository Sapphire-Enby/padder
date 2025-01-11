#!/usr/bin/env python3
class nodepad:
    L_MAR = 49  # space before row
    T_MAR = 134 # space above row 1
    B_WID = 63  # Box width
    B_HIG = 63  # box height
    H_PAD = 14  # between boxes
    V_PAD = 14  # between rows
    N_OF_ROW = 8# rows to make
    N_OF_BOX = 8 # boxes in row
    # section
    NodeArray=[[]]
    
    def __init__(self):
        raise NotImplimentedError("Not allowed. use Create Instead")
    # @classmethod
    # def _getx(cls,n_of_x):
    #     return cls.L_MAR + ( n_of_x * (cls.B_WID + cls.H_PAD))
    # @classmethod
    # def _gety(cls,n_of_y): #generates y position for nodes
    #     return cls.T_MAR +( n_of_y * (cls.B_HIG+ cls.V_PAD))
    @classmethod
    def printArray(cls):
        for row in cls.NodeArray:
            for cell in row:
                print(cell)
    def _getx(cls,n_of_x):
        return cls.L_MAR + ( n_of_x * (cls.B_WID + cls.H_PAD))
    def _gety(cls,n_of_y): #generates y position for nodes
        return cls.T_MAR +( n_of_y * (cls.B_HIG+ cls.V_PAD))
    @classmethod
    def check(cls,ch):
        for row in cls.NodeArray:
            for square in row:
                if square.bounds("x",ch[0]) and square.bounds("y",ch[1]):
                    return square.index
    @classmethod # makes a 2d array of nodes sorted by row 
    def create(cls):
        """
        makes a custome class for the nodes to place
        in the 2d array of the grid
        """
        class Node:
            """
            init method only needs a tuple for its x  and y index in 2d arr

            """
            def __init__ (self,index):
                #  clones index (x pos y pos) locally
                self.index = index
                # store temp x and y origin coordinate calculations 
                tx = cls._getx(cls,self.index[0])
                ty = cls._gety(cls,self.index[1])
                #store origins and boundarie coordinates in tuple
                self.x=(tx,tx+cls.B_WID) #  start and ending x val
                self.y=(ty,ty+cls.B_HIG) #  same for y
            
            def bounds(self,axis,val):  # checks if arg pos is in axis boudnds
                # -     needs axis to check and value for checking

                #check for invalid axis
                if axis not in ["x","y"]:
                    raise ValueError("first arg needs to be x or y")
                # check for invalid value
                elif not isinstance(val, int):
                    raise TypeError(f"second param needs to be a float it is {type(val)}")
                else:  # if all pass return calculation
                    return getattr(self,axis)[0] <= val <= getattr(self,axis)[1]  #tell if in bounds
            def __str__(self):  # format print string
                return f"ID/CO-ORDS:{self.index}, X-VALUES:{self.x}, Y-VALUES:{self.y}"
        # after declaring class for nodes
        # fill gridClass 2d array with instance nodes
        cls.NodeArray=[[Node((x,y))\
            for x in range(cls.N_OF_BOX)]\
            for y in range(cls.N_OF_ROW)]
        return cls
nodepad.create()
nodepad.printArray()
