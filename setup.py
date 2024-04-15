from setuptools import setup,find_packages
from typing import List


def get_requirements(file_name:str) -> List[str]:
     res = []
     with open(file_name,"r") as file_obj:
          for elem in file_obj:
               if elem == '-e.  \n':break
               else:
                    res.append(elem.replace("\n",""))
     return res

get_requirements("requirements.txt")


setup(name="MLproject",version="0.0.1",
     author='Pragyan',author_email="tiwaripragyan099@gmail.com",
     packages=find_packages(), # find packages wherever __init__.py is present
     install_requires=get_requirements("requirements.txt"))