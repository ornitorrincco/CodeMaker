import json
import os




def createProject(name):
    if not os.path.exists('build'):
        os.mkdir('build')
    os.chdir(build)


def indent(file):
    file.write('    ')

def newLine(file):
    file.write('\n')
