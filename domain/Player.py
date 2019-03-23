'''
Created on Jan 30, 2018

@author: catad
'''
from ftplib import all_errors


class Player:
    def __init__(self, firstname, lastname, height, position):
        self._firstname = firstname
        self._lastname = lastname
        self._height = height
        self._position = position
        
    def getFirstName(self):
        return str(self._firstname)
    
    def getLastName(self):
        return str(self._lastname)
    
    def getHeight(self):
        return int(self._height)
    
    def getPosition(self):
        return str(self._position)
    
    def __eq__(self, z):
        if isinstance(z, Player) is False:
            return False
        return str(self.getFirstName()) == str(z.getFirstName())
    
    def __str__(self):
        return "Player "+ str(self._firstname) + " " + str(self._lastname) + ", " + str(self._height) + " cm, playing as "+ str(self._position) + "."
        
    
    
    
class PlayerValidator:   
    
    def validate(self, player):
        if isinstance(player, Player) is False:
            raise Exception("Can only validate players.")
        Positions = ['Extremum', 'Shooter', 'Quarterback']
        ok = 0
        _errors = []
        if player.getFirstName() == "" or player.getLastName() == "":
            _errors.append("Name or surname not valid.")
        if player.getHeight() <= 0:
            _errors.append("Height not valid. Must be a positive number.")
        for pos in Positions:
            if player.getPosition() == pos:
                ok = 1
                break
        if ok == 0:
            _errors.append("Position not valid. Must be one of Extremum, Shooter, Quarterback.")
        if len(_errors) != 0:
            raise Exception(_errors)
            
        
                                 
                