import os, sys
import json
import shutil
import zipfile
from zipfile import ZipFile
version = os.getenv('VERSION', '1.2.0') # get version from env if not set use default

files_prefix = ["a", "b", "c", "d"]

def create_files_and_zip(files_prefix): # create files based on list
    for files in files_prefix:
        with open('%s.txt' % files, "w") as new_file:
            new_file.write("Hey im File : %s " % files)
            new_file.close
            if not os.path.isfile('%s.txt' % files):
                print('File %s.txt not found exiting' % files)
                sys.exit()
            else:
                print( "file {}.txt created .... creating zip.. ".format(files))

    for file_to_zip in files_prefix: # ZIP files based on list + version
        with ZipFile('{}_{}.zip'.format(file_to_zip, version), 'w') as zipObj2:
            zipObj2.write(file_to_zip + '.txt')
            zipObj2.close()                            
            if not os.path.isfile('{}_{}.zip'.format(file_to_zip, version)):
                print('{}_{}.zip NOT exists... exiting '.format(file_to_zip, version))
                sys.exit()
    return True

def createArtiUplodTempalte(version): # create tempalte for artifactory upload

    target = "binary-storage/V_" + version + "/"

    template = {
        "files": [
            {
                "pattern": "$WORKSPACE/*.zip",
                "target": target,
            }
        ]
    }
    with open('template.json', 'w') as f:
        json.dump(template, f)


if __name__ == '__main__':

    createArtiUplodTempalte(version)
    create_files_and_zip(files_prefix)
    print("V_" + version)
