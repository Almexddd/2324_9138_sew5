
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

print_labyrinth(read_from_file("l1.txt"))