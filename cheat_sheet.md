# Guide to start project in Python

# to check info
which virtualenv / which python


# to create new virtualenv
cmd:
virtualenv ~/.venv
source ~/.venv/bin/activate

# how to set new virtualenv for all termianls 
# solution: edit bash - bashrc

cmd:
vim ~/.bashrc 

# go to bottom of file and add lines:
source ~/.venv/bin/activate


# How to create a scaffolding of a project?

cmd: 
touch Makefile
touch requirements.txt

# Let's look on Makefile to have blueprint

# To execute file 
cmd: 
make 

# List all version installed on project 

cmd: 
pip freeze | less