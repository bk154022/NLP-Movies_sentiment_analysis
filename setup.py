from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements


setup(
    name='movie_sentinement_analysis',
    version='0.0.1',
    description='this project will work on movies as sentiment analysis',
    author='bilal khan',
    author_email='bilalkhan154022@gmail.com',
    packages=find_packages(),
    install_require_packages=get_requirements('requirements.txt')
)