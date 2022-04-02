from typing import List, Dict, Optional, Tuple, Set
import sys


class Place:
    """
    A place that represents a village or a city in a board game.

    === Instance Attributes ===
    name: The name of this place
    type: Whether this place is a city, village, start port, or end port.
    travels: The current number of times allowed to travel through this place.
    neighbours: A list of adjacent cities or villages of this place.
    """
    name: str
    type: str
    travels: int
    neighbours: List[str]

    def __init__(self, name: int, type: str, travels: int,
                 neighbours: List[str]) -> None:
        self.name = name
        self.type = type
        self.travels = travels
        self.neighbours = neighbours

    def update_travels(self) -> None:
        """
        Decrease the number of travel times for this place once it has been
        travelled through.
        """
        self.travels -= 1


# class Graph:
#     """
#     A graph that represents a board game consisting of a set of cities and
#     villages.
#
#     === Instance Attributes ===
#     board: A dictionary of all the places on this graph. Each key is the name
#     of the place, and its value is a Place instance represented by its name.
#     start: A Place object representing the start port of this graph.
#     end: A Place object representing the end port of this graph.
#     """
#     board: Dict[str, Place]
#     start: Place
#     end: Place
#
#     def __init__(self, adj_lst: Dic):

def read_board(filename: str) -> Dict[str, Place]:
    """Read from <filename> to create a graph represented by a dictionary with
    key being the name of a place and the value being the corresponding Place
    object."""
    if len(sys.argv) != 2:
        print("Usage: python3 Routes.py <inputfilename>")
        sys.exit()
    f = open(filename)
    board = {}
    for line in f:
        key, value = line.strip().split(": ")
        values = value.split(" ")
        board[key] = values
        #TODO

    return board

def analyze_paths(start: Place, board: Dict[str, Place],
                  visited: Set[Place]) -> int:
    """Return the number of all possible routes of this board starting from
    <start>."""
    visited.add(start)
    if start.type == "end":
        return 1
    elif start.type != "end":
        count = 0
        for neighbor in start.neighbors:
            if board[neighbor].travels == 0:
                pass
            pass



if __name__ == "__main__":

    # if len(sys.argv) != 2:
    #     print("Usage: python3 Routes.py <inputfilename>")
    #     sys.exit()


    print(not all([0, 0, 0]))
