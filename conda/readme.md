## conda commands


#### conda create env

```bash
conda create -p ./envs python=3.10 -y
```
or (if not create env in current path)
```bash
conda create -n envs python=3.10 -y
```
</br>

#### conda activate env

```bash
conda activate envs/
```
or (if not create env in current path)
```bash
conda activate envs
```
</br>

#### conda list env

```bash
conda env list
```
</br>

#### conda remove long prefix path in terminal shell
* without any prefix
```bash
conda config --set env_prompt '($(basename {default_env})) '
```
or
* with just parent directory as prefix
```bash
conda config --set env_prompt '($(basename $(dirname {prefix}))) '
```
</br>



## conda or miniconda installation link ubuntu [article link](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html) and for step by step guide [article link](https://medium.com/@mustafa_kamal/a-step-by-step-guide-to-installing-conda-in-ubuntu-and-creating-an-environment-d4e49a73fc46)

## conda env commands [article link](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)