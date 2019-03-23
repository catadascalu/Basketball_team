'''
Created on Jan 30, 2018

@author: catad
'''


class RepositoryException:
    def __init__(self, message):
        self._message = message
        
    def getMessage(self):
        return self._message
    
    def __str__(self):
        return self._message