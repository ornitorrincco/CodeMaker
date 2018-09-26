import json
import os
import subprocess


class ConfigManager():

    def __init__(self, config='config.json'):
        self.typeProject = config['typeProject']
        self.name = config['name']
        self.dependencies = config['dependencies']

    def change_folder(self,folderName):
        try:
            if not os.path.exists(folderName):
                os.mkdir(folderName)
            os.chdir(folderName)
        except:
            print('Some Error Happen while change_folder')

    def configLoader():
        try:
            if not os.path.exists('config.json'):
                print('config.json is not found')
                return
            with open('config.json', "r") as jsonFile:
                config = json.load(jsonFile)
                jsonFile.close()
                return config
        except:
            print('Some Error Happen while config.json was Loaded')

def run_command(command):
    # trim the newline
    command == command.rstrip()
    # run the command and get the output back
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except:
        output = 'Failed to execute command.\r\n'
    # send back output to the client
    return output

def change_folder(folderName):
    if not os.path.exists(folderName):
        os.mkdir(folderName)
    os.chdir(folderName)

def enviroment():
    return os.environ.copy()

def create_virtual_enviroment(nameProject, filename='logs.txt'):
    with open(filename, 'wb') as file:
        subprocess.run('virtualenv ' + str(nameProject) + 'Env', stdout = file, shell = True)

def dependencie_installer(config):
    for key in config['dependencies'].keys():
        config['dependencies'][key] == ''
        print(key)

def createProjectPython(config):
    type_project = 'typeProject'
    change_folder('build')
    if config[type_project] == 'React':
        pass
    elif config[type_project] == 'React-Native':
        pass
    elif config[type_project] == 'Electron':
        pass
    elif config[type_project] == 'Angular':
        pass
    elif config[type_project] == 'Django':
        pass
    elif config[type_project] == 'Flask':
        pass
    elif config[type_project] == 'Python':
        importer(config)
        importerAll(config)

def importer(config):
    extention = '.py'
    for library in config['dependencies']:
        with open(config['name'] + extention,'a+') as file:
            file.write('import'+ ' ' + library)
            newLine(file)
            file.close()

def importerAll(config):
    extention = '.py'
    for library in config['libraries']:
        with open(config['name'] + extention,'a+') as file:
            file.write('from' + ' ' + library + ' ' + 'import *')
            newLine(file)
            file.close()
    with open(config['name'] + extention,'a+') as file:
        newLine(file)
        file.close()

def createProjectReactNative(config):
    extention = '.js'
    change_folder('build')
    with open(config['name'] + extention,'w') as file:
        file.write('hello')

def createProjectReact(config):
    extention = '.js'
    change_folder('build')
    with open(config['name'] + extention,'w') as file:
        file.write('hello')


def indent(file,numberOfTabs = 0):
    file.write(numberOfTabs*'\t')

def newLine(file):
    file.write('\n')

def ifPython(file, condition, numberOfTabs = 0):
    indent(file,numberOfTabs)
    file.write('if ' + condition + ':')

def ifJS(file, condition, numberOfTabs = 0):
    indent(file,numberOfTabs)
    file.write(spaces + 'if (' + condition + ') ')

if __name__ == "__main__":
    # try:
    config = configLoader()
    installer = ConfigManager(config)
    # dependencie_installer(config)
    # create_virtual_enviroment(config['name'])
    # createProjectPython(config)
    # except:
    #     print('Something Bad happen')
else:
    print('Nothing to do with import')
