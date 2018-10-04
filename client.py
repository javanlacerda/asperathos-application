# coding: utf-8

import requests
from subprocess import call
import subprocess
import argparse
import os
import getpass
import sys
import string
import random


def shell(command):
    '''Funcao que executa comandos shell via python
    Args:
        command (string): Comando shell a ser executado.
    Returns:
        array: Uma lista de strings com a saida do comando shell
    '''
    subcommand = subprocess.Popen(
        [command], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = subcommand.stdout.read()
    if output.split() == []:
        error = subcommand.stderr.readlines()
        print >>sys.stderr, "ERROR: %s" % error
    else:
        return output




parser = argparse.ArgumentParser(usage='%(prog)s [options]')
parser.add_argument("path", help="Token do usuario")

args = parser.parse_args()


r = requests.get("http://10.11.4.253:8080/msgs")

while r.text != "-1":
    
    r = requests.get("http://10.11.4.253:8080/msgs")

    shell("echo %s >> %s" % (r, args.path))








