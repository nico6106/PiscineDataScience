from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'A sample test package'
URL = 'https://github.com/nico6106/PiscineDataScience'

# Setting up
setup(
        name="ft_package", 
        version=VERSION,
        author="nlesage",
        author_email="nlesage@42.fr",
        description=DESCRIPTION,
        packages=find_packages(),
		url=URL,
		license='MIT',
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        classifiers= [
        ]
)