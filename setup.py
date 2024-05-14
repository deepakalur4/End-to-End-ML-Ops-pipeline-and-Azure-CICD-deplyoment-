from setuptools import find_packages,setup
from typing import list

def get_pack(file_path)->list:
    '''
    This function wil returns the list of packages from requirements file
    
    '''
    with open(file_path, 'r') as file_obj:
        pack=file_obj.readlines()
        pack=[i.replace("\n","") for i in pack if i.replace("\n","")  not in "-e ."]
        return (pack)

setup(
    name="ML end to end project",
    version="0.0.0.5",
    author="Deepak S Alur",
    author_email="deepakalur4@gmail.com",
    packages=find_packages(),
    install_requires=get_pack("requirements.txt")

)
