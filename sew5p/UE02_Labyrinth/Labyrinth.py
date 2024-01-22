import argparse
import time


def read_from_file(filepath: str) -> [[str]]:
    """
    Liest Labyrinth aus Datei ein
    :param filepath: Datei aus der Labyrinth ausgelesen werden soll
    :return: 2d array mit Labyrinth
    """
    with open(filepath) as file:
        return [[a for a in line.strip()] for line in file.readlines()]


def print_labyrinth(lab: [[str]]) -> None:
    """
    Gibt Labyrinth zeichen für zeichen aus
    :param lab: Labyrinth, das augegeben werden soll
    """
    for line in lab:
        print("".join(line))


def suchen(zeile: int, spalte: int, lab: [[str]], should_print: bool, delay: int):
    if lab[zeile][spalte] == 'A':
        if should_print:
            print_labyrinth(lab)
            time.sleep(delay/1000)
        return True
    if lab[zeile][spalte] == '#' or lab[zeile][spalte] == 'x':
        return False
    lab[zeile][spalte] = 'x'
    n1 = suchen(zeile - 1, spalte, lab, should_print, delay)
    n1 += suchen(zeile + 1, spalte, lab, should_print, delay)
    n1 += suchen(zeile, spalte - 1, lab, should_print, delay)
    n1 += suchen(zeile, spalte + 1, lab, should_print, delay)
    lab[zeile][spalte] = ' '
    return n1


def sucheAlle(zeile: int, spalte: int, lab: [[str]]):
    """
    sucht alle möglichen Wege zu einem Ausgang
    :param zeile:
    :param spalte:
    :param lab:
    :return:
    """
    if lab[zeile][spalte] == 'A':
        print_labyrinth(lab)
        return 1
    if lab[zeile][spalte] == '#' or lab[zeile][spalte] == 'x':
        return 0
    lab[zeile][spalte] = 'x'
    n1 = sucheAlle(zeile - 1, spalte, lab)
    n2 = sucheAlle(zeile + 1, spalte, lab)
    n3 = sucheAlle(zeile, spalte - 1, lab)
    n4 = sucheAlle(zeile, spalte + 1, lab)
    lab[zeile][spalte] = ' '
    return n1 or n2 or n3 or n4


parser = argparse.ArgumentParser()
parser.add_argument("filename", help="file containing the labyrinth to solve")
parser.add_argument("-x", "--xstart", help="x-coordinate to start")
parser.add_argument("-y", "--ystart", help="y-coordinate to start")
parser.add_argument("-p", "--print", help="print output of every solution", action="store_true")
parser.add_argument("-t", "--time", help="print total calculation time (in milliseconds)", action="store_true")
parser.add_argument("-d", "--delay", help="delay after printing a solution (in milliseconds)")
args = parser.parse_args()

lab = read_from_file(args.filename)
start_time = int(time.time()*1000)
suchen(int(args.xstart), int(args.ystart), lab, args.print, int(args.delay))
end_time = int(time.time()*1000)
if args.time:
    print(f'Time Elapse: {(end_time-start_time)/1000} ms')


