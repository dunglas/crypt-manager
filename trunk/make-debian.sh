#!bin/bash
cd deb/
rm -Rf *
svn checkout http://crypt-manager.googlecode.com/svn/trunk/ crypt-manager
cd crypt-manager
bash clean-svn.sh
cd ..
mv crypt-manager/debian .
mv crypt-manager conceal-0.0.5
tar -czvf conceal_0.0.5.orig.tar.gz conceal-0.0.5
cd conceal-0.0.5
debuild -us -uc
