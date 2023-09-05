from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    """_summary_

    Args:
        file_path (str): requirements file path

    Returns:
        List[str]: requirements pachages from requirements
    """
    requirements =[]
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements
    
    
setup(
    name = "MLProject",
    version="0.0.1",
    author="Raktima",
    author_email="reddish.rb@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)