# BuddingScritps

A lightweight command line tool to quickly multiply 
scripts for parallel job management.

## setup

### Install the package and console script

```{bash}
python setup.py install
```

The package is tested under Python 3.8.18.

### Configure

Before usage, a configure file should be set up 
at `${HOME}/.buddingScriptsRC.json`. 
A configure file describes the type of scripts 
buddingScripts can work with. An example configure 
can be found at `example_configs/buddingScriptsRC.json`. 
The example works with plain bash, plain python 
and slurm batch scripts. 