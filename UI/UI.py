'''
Created on Jan 30, 2018

@author: catad
'''


from controller.PlayerController import PlayerController
from controller.UndoController import UndoController
from controller.UndoController import FunctionCall
from controller.UndoController import CascadedOp
from controller.UndoController import Operation
from domain.Player import Player
from domain.Player import PlayerValidator

from repository.repository import Repository
from repository.RepositoryException import RepositoryException
from repository.CSVPlayers import CSVPlayers

import csv
from test.test_trace import traced_func_importing

class UI:
    
    def __init__(self, player, undo):
        self._player = player
        self._undo = undo
        
    def start(self):
        while True:
            option = str(input("Enter option: "))
            if option == '1':
                print("You chose to add a player")
                name = str(input("Enter first name: "))
                surname = str(input("Enter surname: "))
                height = int(input("Enter height(cm): "))
                position = str(input("Enter position(Extremum/Shooter/Quarterback): "))
                player = self._player.create(name, surname, height, position)
                
            elif option == '2':
                print("You chose to print all players.")
                players = self._player.getAll()
                for player in players:
                    print(player)
                    
            elif option == '3':
                print("Updating a player.")
                name = str(input("Enter first name: "))
                surname = str(input("Enter last name: "))
                height = int(input("Enter new height: "))
                position = str(input("Enter player post: "))
                player = Player(name, surname, height, position)
                self._player.update(player)
                
                
            elif option == '4':
                print("Creating a team.")
                team = self._player.createTeam()
                for p in team:
                    print(p)
                    
            elif option == '5':
                print("Importing players.")
                print(self._player.importPlayers())
                
            elif option == '6':
                self._undo.undo()
                
            elif option == '7':
                self._undo.redo()
                
            elif option == '0':
                break
            else:
                print("Invalid option. Enter * for help.")
                
                
                
                



validator = PlayerValidator()
repository = CSVPlayers('players.csv', 'imported.csv')
undo = UndoController()
player = PlayerController(validator, repository, undo)

menu = UI(player, undo)
menu.start()