'''
Created on Jan 30, 2018

@author: catad
'''
from repository.repository import Repository
from repository.RepositoryException import RepositoryException
from domain.Player import Player
from domain.Player import PlayerValidator
import random

import csv

class CSVPlayers(Repository):
    
    def __init__(self, filename, filename2):
        super().__init__()
        
        self._filename = filename
        self._filename2 = filename2
        self.loadFromFile()
        self.importPlayers()
    def findPlayer(self, name):
        return super().find(name)
    
    def getAll(self):
        return super().getAll()
    
    def store(self, player):
        try:
            super().store(player)
            self.writeToFile()
            
        except Exception as e:
            print(e)
            
    def delete(self, firstname):
        super().delete(firstname)
        self.writeToFile()
        
    def update(self, new_player):
        super().update(new_player)
        self.writeToFile()
        
    def printAll(self):
        super().printAll()
        
        
    def importPlayers(self):
        Positions = ['Extremum', 'Shooter', 'Quarterback']
        added = 0
        file = open(self._filename2, 'r')
        for line in file:
            attributes = line.split(",")
            if len(attributes) != 2:
                continue
            height = random.randint(180, 215)
            position = random.randint(0,2)
            playerPost = Positions[position]
            player = Player(attributes[0], attributes[1], height, playerPost)
            self.store(player)
            added += 1
        return added
    def loadFromFile(self):
        
        """
        Loads data from a file and returns it
        :return: None
        
        """
        #try:
        file = open(self._filename, 'r')
        for line in file:
            attributes = line.split(",")
            if len(attributes) != 4:
                continue
            player = Player(attributes[0], attributes[1], attributes[2], attributes[3])
            self._objects.append(player)
               
        #except IOError as e:
            #raise RepositoryException(e)
                
    def writeToFile(self):
        
        """
        Write the list to the file
        :return: None
        
        """
        try:
            with open(self._filename, 'w') as file:
                
                
                for player in self._objects:
                    file.write(str(player.getFirstName())+","+str(player.getLastName())+","+str(player.getHeight())+","+str(player.getPosition())+"\n")
                
        except IOError as e:
            raise RepositoryException(e)
        
        
            
        
        
    
        
        
        