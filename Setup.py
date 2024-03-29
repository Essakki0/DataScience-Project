from typing import List
from setuptools import find_packages,setup


link='-e .'
def GetRequirements (file_name:str)->List[str]:

    '''Returns the list of requirements from file'''
    requirements=[]
    with open(file_name,'r') as req:
        requirements=req.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if link in requirements:
            requirements.remove(link)
    
    return requirements

print(GetRequirements('requirements.txt'))

setup(
    name="ML Project",
    version='0.1',
    author='Essakki',
    author_email='essakkiappanm.0@gmail.com',
    packages=find_packages(),
    install_requires=GetRequirements("requirements.txt")
)
        