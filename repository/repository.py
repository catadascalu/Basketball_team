'''
Created on Jan 30, 2018

@author: catad
'''

from domain.Player import Player
from domain.Player import PlayerValidator

from repository.RepositoryException import RepositoryException




class Repository:
    
    def __init__(self):
        self._objects = []
    
    def store(self, object):
        if self.find(object.getFirstName()) != None:
            raise Exception("Name not unique.")
        self._objects.append(object)
        
    def find(self, firstname):
        for e in self._objects:
            if firstname == e.getFirstName():
                return e
            
        return None
    
    def update(self, object):
        el = self.find(object.getFirstName())
        if el == None:
            raise RepositoryException("Player not found.")
        idx = self._objects.index(el)
        self._objects.remove(el)
        self._objects.insert(idx, object)
        return object
    
    def delete(self, firstname):
        object = self.find(firstname)
        if object == None:
            raise ValueError("Object not in Repo")
        self._objects.remove(object)
        return object
    
    
    def getAll(self):
        return self._objects
    
    def __len__(self):
        return len(self._objects)
    
    def printAll(self):
        for e in self._objects:
            print(e)
            
    def __str__(self):
        for e in self._objects:
            if isinstance(e, Player):
                print(e)
            else:
                print("Invalid object.")
                
                
                
            
        
                
            
    
            
            
        
        