
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

print_labyrinth(read_from_file("l1.txt"))
suchen(1, 1, read_from_file('./l1.txt'))