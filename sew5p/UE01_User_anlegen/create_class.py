import argparse
import random

from openpyxl import load_workbook


def generate_script(filepath):
    with open('create_script.txt', 'w') as file:
        del_script = open('delete_script.txt', 'w')
        logins = open('logins.txt', 'w')
        wb = load_workbook(f"{filepath}/Klassenraeume_2023.xlsx", read_only=True)
        ws = wb[wb.sheetnames[0]]
        for a in ws.iter_rows(min_row=2):
            if a[0].value is None:
                break
            classes = {
                "class": a[0].value,
                "RaumNr": a[1].value,
                "KV": a[2].value
            }
            pw = f"{classes['class']}:{classes['class']}{random.choice('!%&(),._-=^#')}{classes['RaumNr']}{classes['KV']}"
            file.write(f"useradd -d /home/klassen/{classes['class'].lower()} -c \"Klasse {classes['class']}\" -m -g {classes['class'].lower()} -G cdrom,plugdev,sambashare -s /bin/bash k{classes['class'].lower()} \n")
            file.write(f"echo '{pw}'| chpasswd\n")
            del_script.write(f"userdel k{classes['class'].lower()} \n")
            logins.write(f"k{classes['class'].lower()}: {pw} \n")
        wb = load_workbook(f"{filepath}/Klassenraeume_2023.xlsx")
        ws = wb[wb.sheetnames[0]]
        for user in ws.iter_rows(min_row=2):
            if user[0].value is None:
                break
            a = {
                "firstname": user[0],
                "lastname": user[1],
                "group": user[2],
                "class": user[3]
            }
            if a['group'] == 'teacher':
                file.write(f"useradd -d /home/lehrer/{a['firstname']} -c \"{a['firstname']} {a['lastname']}\" -m -g {a['group']} -G cdrom,plugdev,sambashare -s /bin/bash {a['firstname'][0].lower()}{a['lastname'].lower()} \n")
            else:
                file.write(f"useradd -d /home/klassen/k{a['class'].lower()}/{a['firstname']} -c \"{a['firstname']} {a['lastname']}\" -m -g {a['group']} -G cdrom,plugdev,sambashare -s /bin/bash {a['firstname'][0].lower()}{a['lastname'].lower()} \n")


parser = argparse.ArgumentParser()
parser.add_argument("filepath")
parser.add_argument("-v", "--verbosity")
parser.add_argument("-q", "--quite")
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")
if args.filepath:
    generate_script(args.filepath)