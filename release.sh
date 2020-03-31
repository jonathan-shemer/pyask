#!/usr/bin/env bash
export RED='\033[0;31m';
export BLUE='\033[1;34m';
export DEFAULT='\033[0m';

rm -rf ./build ./dist;
pip install --upgrade -r requirements.txt;
tox || exit $?;
if [ -z "$1" ]
  then
      echo -e "${RED}Must provide bump argument. Options include:${DEFAULT}
  ${BLUE}-M${DEFAULT}, ${BLUE}--major${DEFAULT}     Bump major number
  ${BLUE}-m${DEFAULT}, ${BLUE}--minor${DEFAULT}     Bump minor number
  ${BLUE}-p${DEFAULT}, ${BLUE}--patch${DEFAULT}     Bump patch number"
      exit 1;
fi
bump "$1";
python setup.py sdist bdist_wheel;
python -m twine upload --config-file ~/.pypirc dist/* --verbose;
