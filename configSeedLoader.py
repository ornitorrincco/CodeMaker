import json
import os


def createProject(name):
    if not os.path.exists('build'):
        os.mkdir('build')
    os.chdir(build)

def configLoader():
    try:
        if not os.path.exists('configSeed.json'):
            print('configSeed.json is not found')
            return
        jsonFile = open('configSeed.json', "r")
        config = json.load(jsonFile)
        jsonFile.close()
        return config
    # return 0
    except:
        print('Some Error Happen while configSeed.json was Loaded')

def indent(file):
    file.write('    ')

def newLine(file):
    file.write('\n')


if __name__ == "__main__":
    configLoader()
    
