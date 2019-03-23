'''
Created on Jan 31, 2018

@author: catad
'''


class UndoController:
    def __init__(self):
        self._history = []
        self._index = -1
        
    def recordOperation(self, cascadedOp):
        self._history.append(cascadedOp)
        self._index += 1
        
    def undo(self):
        if self._index >= 0:
            self._history[self._index].undo()
            self._index -= 1
            return True
        return False
    
    def redo(self):
        if self._index < len(self._history):
            self._history[self._index].redo()
            self._index += 1
            return True
        return False
    
    
    
class FunctionCall:
    def __init__(self, functionRef, *parameters):
        self._functionRef = functionRef
        self._parameters = parameters
        
    def call(self):
        self._functionRef(*self._parameters)
        
class Operation:
    def __init__(self, functionDo, functionUndo):
        self._functionDo = functionDo
        self._functionUndo = functionUndo
        
    def undo(self):
        self._functionUndo.call()
        
    def redo(self):
        self._functionDo.call()
        
    
class CascadedOp:
    def __init__(self, op = None):
        self._operations = []
        
        if op !=  None:
            self.add(op)
            
            
    def add(self, op):
        self._operations.append(op)
        
    def undo(self):
        for i in range(len(self._operations)-1, -1, -1):
            self._operations[i].undo()
            
    def redo(self):
        for i in range(len(self._operations)-1, -1, -1):
            self._operations[i].redo()
            
    
            
        
        
        
            