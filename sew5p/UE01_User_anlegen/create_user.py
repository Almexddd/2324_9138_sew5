import argparse
import logging
from unicodedata import normalize, category
from logging.handlers import RotatingFileHandler
from sys import stdout as out
from openpyxl import load_workbook


def sonderzeichen(s: str):
    umlaute = {
        'ä': 'ae',
        'ö': 'oe',
        'ü': 'ue',
        'Ä': 'Ae',
        'Ö': 'Oe',
        'Ü': 'Ue',
        'ß': 'ss',
        ' ': '_'
    }
    for a, b in umlaute.items():
        s = s.replace(a, b)
    return s


def generate_script(filepath):
    with open('create_script.txt', 'w') as file:
        wb = load_workbook(filepath)
        ws = wb[wb.sheetnames[0]]
        user_cnt = dict()
        for user in ws.iter_rows(min_row=2):
            if user[0].value is None:
                break
            data = {
                "firstname": user[0].value,
                "lastname": user[1].value,
                "group": user[2].value,
                "class": user[3].value
            }
            data['firstname'] = sonderzeichen(data['firstname'])
            data['lastname'] = sonderzeichen(data['lastname'])
            data['firstname'] = ''.join(a for a in normalize('NFKD', data['firstname']) if category(a) != 'Mn')
            data['lastname'] = ''.join(a for a in normalize('NFKD', data['lastname']) if category(a) != 'Mn')
            if data['lastname'] not in user_cnt:
                if data['group'] == 'teacher':
                    file.write(f"useradd -d /home/lehrer/{data['lastname']} -c \"{data['firstname']} {data['lastname']}\" -m -g {data['group']} -G cdrom,plugdev,sambashare -s /bin/bash {data['lastname'].lower()} \n")
                else:
                    file.write(f"useradd -d /home/klassen/k{data['class'].lower()}/{data['lastname']} -c \"{data['firstname']} {data['lastname']}\" -m -g {data['group']} -G cdrom,plugdev,sambashare -s /bin/bash {data['lastname'].lower()} \n")
                user_cnt[data['lastname']] = 1
            else:
                if data['group'] == 'teacher':
                    file.write(f"useradd -d /home/lehrer/{data['lastname']} -c \"{data['firstname']} {data['lastname']}\" -m -g {data['group']} -G cdrom,plugdev,sambashare -s /bin/bash {data['lastname'].lower()}{user_cnt[data['lastname']]} \n")
                else:
                    file.write(f"useradd -d /home/klassen/k{data['class'].lower()}/{data['lastname']} -c \"{data['firstname']} {data['lastname']}\" -m -g {data['group']} -G cdrom,plugdev,sambashare -s /bin/bash {data['lastname'].lower()}{user_cnt[data['lastname']]} \n")
                user_cnt[data['lastname']] += 1


parser = argparse.ArgumentParser()
parser.add_argument("filepath")
parser.add_argument("-v", "--verbosity")
parser.add_argument("-q", "--quite")
args = parser.parse_args()

logging.basicConfig(level=logging.DEBUG if args.verbosity else logging.WARNING)
logger = logging.getLogger()
handler = RotatingFileHandler('logfile.log', maxBytes=10000, backupCount=5)
handler.setLevel(logging.DEBUG if args.verbosity else logging.WARNING)
logger.addHandler(handler)
stream_handler = logging.StreamHandler(out)
stream_handler.setLevel(logging.INFO)
logger.addHandler(stream_handler)
if args.filepath:
    generate_script(args.filepath)