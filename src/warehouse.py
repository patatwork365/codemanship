from .cd import CD
from typing import Dict

class Warehouse:
    def __init__(self, cd_dict: Dict[CD, int]):
        self.cd_dict = cd_dict

    def search(self, artist: str = '', title: str = ''):

        for cd in self.cd_dict:
            if cd.artist == artist or cd.title == title:
                return 'Match found.'
        return 'Match not found.'
