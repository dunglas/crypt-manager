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

if [ -e dontexists ]
then
    rm -Rf dontexists
fi

echo "Open a directory that don't exists..."
conceal --open dontexists
echo "Encrypt a directory that don't exists..."
conceal --crypt dontexists
echo "Close a directory that don't exists..."
conceal --close dontexists
echo "Decrypt a directory that don't exists..."
conceal --decrypt dontexists
echo "Change the password of a directory that don't exists..."
conceal --change-pass dontexists

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
conceal --crypt testencrypt
echo "Close it..."
conceal --close testencrypt
echo "Change password... Please enter a BAD password."
conceal --change-pass testencrypt
echo "Change password... Please DON'T match confirmation and password."
conceal --change-pass testencrypt
echo "Change password... Please enter a GOOD password."
conceal --change-pass testencrypt
echo "Open it... Please enter a BAD password."
conceal --open testencrypt
echo "Open it... Please enter the GOOD password."
conceal --open testencrypt
echo "Decrypt it... Please enter a BAD password."
conceal --decrypt testencrypt
echo "Decrypt it... Please enter the GOOD password."
conceal --decrypt testencrypt
