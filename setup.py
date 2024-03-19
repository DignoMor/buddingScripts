from setuptools import setup

setup(
    name='buddingScripts',
    version='0.1',
    packages=['buddingScripts'],
    entry_points={
    'console_scripts': [
        'buddingScripts=buddingScripts.buddingScripts:main'
    ]
})
