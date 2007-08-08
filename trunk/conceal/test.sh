#!/bin/bash
echo "Unit tests for conceal"
echo "-------------------------------------------------------------------------"
echo "Command line tool"
echo "-------------------------------------------------------------------------"
echo "Install the command line tool..."
sudo rm -rf build
find . -name '*.py[co]' | xargs rm -f
sudo python setup.py build
sudo python setup.py install
conceal --version
conceal --help
conceal
if [ -e dontexists ]
then
    rm -Rf dontexists
fi

echo "Open a directory that don't exists..."
conceal -o dontexists
echo "Encrypt a directory that don't exists..."
conceal -e dontexists
echo "Close a directory that don't exists..."
conceal -c dontexists
echo "Decrypt a directory that don't exists..."
conceal -d dontexists
echo "Change the password of a directory that don't exists..."
conceal -p dontexists

echo "Create a directory with some files and subdirecotries and encrypt it..."

if [ -e testencrypt ]
then
    rm -Rf testencrypt
fi

mkdir testencrypt
mkdir testencrypt/sub1
mkdir testencrypt/sub2
mkdir testencrypt/sub1/sub3
echo "test1" > testencrypt/haha
echo "test2" > testencrypt/sub1/haha
echo "test3" > testencrypt/sub2/plop
echo "test4" > testencrypt/hohoooo
echo -e "keyes\n" | conceal -s -e testencrypt
echo "Close it..."
conceal -c testencrypt
echo "Change password: BAD password..."
echo -e "plop\nlapin\nlapin\n" | conceal -s -p testencrypt
echo "Change password: passwords DO NOT match..."
echo -e "keyes\nlapin\npinla\n" | conceal -s -p testencrypt
echo "Change password: GOOD password and passwords match..."
echo -e "keyes\nlapin\nlapin\n" | conceal -s -p testencrypt
echo "Open it: BAD password..."
echo -e "plop\n" | conceal -s -o testencrypt
echo "Open it: GOOD password..."
echo -e "lapin\n" | conceal -s -o testencrypt
conceal
echo "Decrypt it: BAD password..."
echo -e "plop\n" | conceal -s -d testencrypt
echo "Decrypt it: GOOD password..."
echo -e "lapin\n" | conceal -s -d testencrypt
conceal
