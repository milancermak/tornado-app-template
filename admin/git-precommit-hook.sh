#!/bin/sh
#

# make sure requirements.txt is up to date with every commit
# by comparing the output of pip freeze
pip freeze | diff requirements.txt - > /dev/null
if [ $? != 0 ]
then
    echo "Missing python module dependencies in requirements.txt. Run 'pip freeze > requirements.txt' to update."
    exit 1
fi
