import argparse


def read_from_file(filepath: str):
    """
    Liest Labyrinth aus Datei ein
    :param filepath: Datei aus der Labyrinth ausgelesen werden soll
    :return: 2d array mit Labyrinth
    """
    with open(filepath) as file:
        return [[a for a in line.strip()] for line in file.readlines()]

def print_labyrinth(lab: [[str]]):
    for line in lab:
        print("".join(line))

def suchen(zeile: int, spalte: int, lab: [[str]]):
    if lab[zeile][spalte] == 'A':
        print_labyrinth(lab)
        return True
    if lab[zeile][spalte] == '#' or lab[zeile][spalte] == 'x':
        return False
    lab[zeile][spalte] = 'x'
    n1 = suchen(zeile - 1, spalte, lab)
    n2 = suchen(zeile + 1, spalte, lab)
    n3 = suchen(zeile, spalte - 1, lab)
    n4 = suchen(zeile, spalte + 1, lab)
    lab[zeile][spalte] = ' '
    return n1 or n2 or n3 or n4

def sucheAlle(zeile: int, spalte: int, lab: [[str]]):
    if lab[zeile][spalte] == 'A':
        print_labyrinth(lab)
        return 1
    if lab[zeile][spalte] == '#' or lab[zeile][spalte] == 'x':
        return 0
    lab[zeile][spalte] = 'x'
    n1 = sucheAlle(zeile - 1, spalte, lab)
    n1 += sucheAlle(zeile + 1, spalte, lab)
    n1 += sucheAlle(zeile, spalte - 1, lab)
    n1 += sucheAlle(zeile, spalte + 1, lab)
    lab[zeile][spalte] = ' '
    return n1

print_labyrinth(read_from_file("l1.txt"))
print(sucheAlle(5, 5, read_from_file('./l1.txt')))

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="file containing the labyrinth to solve")
parser.add_argument("-h", "--help", help="show this help message and exit")
parser.add_argument("-x", "--xstart", help="x-coordinate to start")
parser.add_argument("-y", "--ystart", help="y-coordinate to start")
parser.add_argument("-p", "--print", help="print output of every solution",action="store_true")
parser.add_argument("-d", "--delay", help="delay after printing a solution")
args = parser.parse_args()