'''
Created on Jan 30, 2018

@author: catad
'''
from domain.Player import Player
from domain.Player import PlayerValidator
from repository.RepositoryException import RepositoryException
from controller.UndoController import UndoController
from controller.UndoController import FunctionCall
from controller.UndoController import Operation
from controller.UndoController import CascadedOp
from test.test_asyncio.test_futures import BaseFutureDoneCallbackTests


class PlayerController:
    
    def __init__(self, validator, repository, undoController):
        self._validator = validator
        self._repository = repository
        self._undoController = undoController
        
    
    def create(self, firstname, surname, height, position, recordForUndo = True):
        player = Player(firstname, surname, height, position)
        try:
            self._validator.validate(player)
            self._repository.store(player)
        except Exception as e:
            print(e)
        
        if recordForUndo == True:
            undo = FunctionCall(self.delete, firstname, False)
            redo = FunctionCall(self.create, firstname, surname, height, position, True)
            casOP = CascadedOp(Operation(redo, undo))
            self._undoController.recordOperation(casOP)
        
        
    def delete(self, firstname, recordForUndo = True):
        try:
            player = self._repository.delete(firstname)
        
            if recordForUndo == True:
                undo = FunctionCall(self.create, firstname, player.getLastName(), player.getHeight(), player.getPosition(), False)
                redo = FunctionCall(self.delete, firstname, True)
                casOP = CascadedOp(Operation(redo, undo))
                self._undoController.recordOperation(casOP)
            
                return player
            
        except Exception as e:
            print(e)
                
        
            
        
    def update(self, player, recordForUndo = True):
        old_player = self._repository.find(player.getFirstName())
        new_player = self._repository.update(player)
        
        if recordForUndo == True:
            undo = FunctionCall(self.update, new_player, False)
            redo = FunctionCall(self.update, old_player, True)
            casOP = CascadedOp(Operation(redo, undo))
            self._undoController.recordOperation(casOP)
            
            
            
        return new_player
        
        
    def getPlayerCount(self):
        return len(self._repository)
    
    def findByName(self, name):
        return self._repository.find(name)
    
    def getAll(self):
        return self._repository.getAll()
    
    def filter(self):
        extremums = []
        shooters = []
        quarterbacks = []
        for player in self._repository.getAll():
            if player.getPosition() == 'Extremum\n':
                extremums.append(player)
            elif player.getPosition() == 'Shooter\n':
                shooters.append(player)
            elif player.getPosition() == 'Quarterback\n':
                quarterbacks.append(player) 
                
       
                
        return extremums, shooters, quarterbacks
    
    
    def createTeam(self):
        team = []
        if self.getPlayerCount() >=5:
            extremums, shooters, quarterbacks = self.filter()
                    
            if len(extremums) >= 2 and len(shooters) >=1 and len(quarterbacks) >= 2:
                sortedEx = []
                for p in extremums:
                    sortedEx.append((p.getHeight(), p.getFirstName(), p.getLastName()))
                sortedEx = sorted(sortedEx)
                
                team.append(sortedEx[-1])
                team.append(sortedEx[-2])
                sortedS = []
                for p in shooters:
                    sortedS.append((p.getHeight(), p.getFirstName(), p.getLastName()))
                sortedS = sorted(sortedS)
                
                team.append(sortedS[-1])
                sortedQ = []
                for p in quarterbacks:
                    sortedQ.append((p.getHeight(), p.getFirstName(), p.getLastName()))
                sortedQ = sorted(sortedQ)
                
                team.append(sortedQ[-1])
                team.append(sortedQ[-2])
                
            else:
                print("Not enough positions.")
                
        else:
            print("Not enough players.")
            
        return team
                
                
                
    def importPlayers(self):
        return self._repository.importPlayers()               
                            
                    
                 
        