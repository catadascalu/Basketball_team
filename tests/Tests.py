'''
Created on Jan 30, 2018

@author: catad
'''
from unittest import TestCase
from domain.Player import Player
from domain.Player import PlayerValidator
from controller.PlayerController import PlayerController
from repository.CSVPlayers import CSVPlayers

class ControllerTests(TestCase):
    def setUp(self):
        self._players = [('Sparks','Josh',203,'Shooter'), ('Anderson','James',200,'Extremum'),('Barnette','Sean',190,'Extremum'), ('Curry','Stephen',198,'Shooter')]
        self.player1 = Player(self._players[0][0], self._players[0][1], self._players[0][2], self._players[0][3])
        self.player2 = Player(self._players[1][0], self._players[1][1], self._players[1][2], self._players[1][3])
        self.player3 = Player(self._players[2][0], self._players[2][1], self._players[2][2], self._players[2][3])
        self.player4 = Player(self._players[3][0], self._players[3][1], self._players[3][2], self._players[3][3])
        self.validator = PlayerValidator() 
        self.repository = CSVPlayers('players_test.csv', 'imported_test.csv')
        self.Player = PlayerController(self.validator, self.repository)
        
        
    def test_create(self):
        
        self.Player.create('Brown', 'Dan', 205, 'Shooter')
        self.assertEqual(len(self.repository), 12, "Length not equal.")
        
        self.Player.create('Sparks', 'Josh', 203, 'Extremum')
        self.assertRaises(Exception)
        self.Player.create('', 'Dean', 201, 'Shooter')
        self.assertRaises(Exception)
        self.Player.create('Jameson', '', 200, 'Quarterback')
        self.assertRaises(Exception)
        self.Player.create('Mamba', 'Black', 201, 'Guard')
        self.assertRaises(Exception)
        self.Player.create('Durant', 'Kevin', -12, 'Shooter')
        self.assertRaises(Exception)
        
        
    def test_update(self):
        player_new = Player('Sparks','Josh',205,'Shooter')
        player = self.Player.update(player_new)
        self.assertEqual(player.getHeight, 205, "Not the same")