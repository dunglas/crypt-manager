#!/bin/bash
echo "Unit tests for foldercrypt"
echo "-------------------------------------------------------------------------"
echo "GTK interface"
echo "-------------------------------------------------------------------------"
echo "Install the gtk interface..."
sudo rm -rf build
find . -name '*.py[co]' | xargs rm -f
sudo python setup.py build
sudo python setup.py install
foldercrypt-gtk --version
foldercrypt-gtk --info

if [ -e dontexists ]
then
    rm -Rf dontexists
fi

echo "Open a directory that don't exists..."
foldercrypt-gtk --open dontexists
echo "Encrypt a directory that don't exists..."
foldercrypt-gtk --crypt dontexists
echo "Close a directory that don't exists..."
foldercrypt-gtk --close dontexists
echo "Decrypt a directory that don't exists..."
foldercrypt-gtk --decrypt dontexists

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
foldercrypt-gtk --crypt testencrypt
echo "Close it..."
foldercrypt-gtk --close testencrypt


echo "Open it... Please enter a BAD password."
foldercrypt-gtk --open testencrypt
echo "Open it... Please enter the GOOD password."
foldercrypt-gtk --open testencrypt
echo "Decrypt it... Please enter a BAD password."
foldercrypt-gtk --decrypt testencrypt
echo "Decrypt it... Please enter the GOOD password."
foldercrypt-gtk --decrypt testencrypt
