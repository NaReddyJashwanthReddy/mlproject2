from setuptools import find_packages,setup

def get_requirements(file_path:str):
    # return all the packages in the requirements.txt
    
    with open(file_path,'rb',encoding='utf-8') as file_object:
        requirements=file_object.read()
        requirements=requirements.replace('\n','.').split(".")
        
    return requirements

setup(
    name='titanic spaceship survival',
    version='0.0.1',
    author='N.Jashwanth Reddy',
    author_email='tangwulinggd@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)