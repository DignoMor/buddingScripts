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

## Usage

### Preparation

To use buddingScripts, one should prepare 
a template file and a certain number of 
`.list` files.

Here is an example:

`hello_world.template.sh`:

```{bash}
echo "Hello <header1>."
```

`jobNames.list`: 

```
greet_allen
greet_xiuqi
```

`people.list`

```
Allen
Xiuqi
```

### budding

The following command will multiply the scripts 
for slurm usage.

```{bash}
mkdir scripts

buddingScripts slurm \
    --job_name jobNames.list \
    --header1 people.list \
    --template hello_world.template.sh \
    --opath scripts
```

The output will be 2 slurm scripts as following.

`scripts/greet_allen.slurm`

```{slurm}
#!/bin/bash
#SBATCH --job-name=greet_allen
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH --time=4:00:00
#SBATCH -p CPU
#SBATCH -output=greet_allen.out
#SBATCH -error=greet_allen.err


echo "Hello Allen."
```

`scripts/greet_xiuqi.slurm`

```{slurm}
#!/bin/bash
#SBATCH --job-name=greet_allen
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH --time=4:00:00
#SBATCH -p CPU
#SBATCH -output=greet_xiuqi.out
#SBATCH -error=greet_xiuqi.err


echo "Hello Xiuqi."
```
