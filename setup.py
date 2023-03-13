from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."
def GetRequirements(filePath:str)->List[str]:
    reqs = []
    with open(filePath) as fileObj:
        reqs = fileObj.readlines()
        reqs = [req.replace("\n", "") for req in reqs]

        if HYPEN_E_DOT in reqs:
            reqs.remove(HYPEN_E_DOT)
    return reqs

setup(
name="FirstEndToEndProject",
version="0.0.1",
author="BuvaneshSrinivasan",
author_email="srinivasan.buvanesh@gmail.com",
packages=find_packages(),
requires=GetRequirements("requirement.txt")


)