MY_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PYENV_HOME=$MY_PATH/venv

VERSION=$1
BUILD_NUMBER=$2

echo "Current version number is $VERSION and the build number is $BUILD_NUMBER"

# Delete previously built virtualenv
if [ -d $PYENV_HOME ]; then
    rm -rf $PYENV_HOME
fi

# Create virtualenv and install necessary packages
python3 -m venv $PYENV_HOME
. $PYENV_HOME/bin/activate

$PYENV_HOME/bin/python -m pip install -r requirements.txt
$PYENV_HOME/bin/pip install -e .
$PYENV_HOME/bin/pytest -vra --junitxml=testreport.xml

#deactivate the venv once completed
deactivate
