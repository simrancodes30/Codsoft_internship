from setuptools import setup, find_packages

setup(
    name='titanic-survival-predictor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'scikit-learn'
        
    ],
    author='Bharti Simran',
    author_email='sb529702@gmail.com',
    description='Predicting Titanic Passenger Survival',
    url='https://github.com/simrancodes30/Codsoft_internship',
    
)