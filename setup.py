# why setup.py is required ?
# ans: if we want to use our project as a packages , thats why we are use setup.py file.

#  -e . , will triger the setup.py file from requirments.txt file and all setup will done 
from  setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
# can read our requirments.txt file . and this can automatically install all the library from the requirments.txt
def get_requiremnts(file_path:str)-> List[str]:
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        #  -e . , will not install from setup.py 
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements


setup(
    # name of the package 
    name='DiamondPricePrediction', 
    # version of the package
    version='0.0.1',
    # author of the package
    author='sourav shukla',
    # author email 
    author_email='souravshukla985@gmail.com',
    # all requirent  for the package 
    install_requires=get_requiremnts('requirments.txt'),
    # package should read all the modules from the project 
    packges=find_packages()
    )