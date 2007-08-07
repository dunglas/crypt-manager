#!/bin/bash
echo "Unit tests for conceal"
echo "-------------------------------------------------------------------------"
echo "GTK interface"
echo "-------------------------------------------------------------------------"
echo "Install the gtk interface..."
sudo rm -rf build
find . -name '*.py[co]' | xargs rm -f
sudo python setup.py build
sudo python setup.py install
conceal-gtk --version
conceal-gtk --info

if [ -e dontexists ]
then
    rm -Rf dontexists
fi

echo "Open a directory that don't exists..."
conceal-gtk --open dontexists
echo "Encrypt a directory that don't exists..."
conceal-gtk --crypt dontexists
echo "Close a directory that don't exists..."
conceal-gtk --close dontexists
echo "Decrypt a directory that don't exists..."
conceal-gtk --decrypt dontexists

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
conceal-gtk --crypt testencrypt
echo "Close it..."
conceal-gtk --close testencrypt


echo "Open it... Please enter a BAD password."
conceal-gtk --open testencrypt
echo "Open it... Please enter the GOOD password."
conceal-gtk --open testencrypt
echo "Decrypt it... Please enter a BAD password."
conceal-gtk --decrypt testencrypt
echo "Decrypt it... Please enter the GOOD password."
conceal-gtk --decrypt testencrypt
