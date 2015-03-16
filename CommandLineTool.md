Command: crypt-manager

Options:
--crypt DIRECTORY       encrypt directory
--open DIRECTORY        open an encrypted folder
--help                  display this help message
--close DIRECTORY       close an encrypted folder
--decrypt DIRECTORY     decrypt encrypted folder
--version               display version information


Examples :

# Create some samples
root@kirk:~/Projects/crypt-manager# mkdir test
root@kirk:~/Projects/crypt-manager# echo "Bonjour" > test/bonjour
root@kirk:~/Projects/crypt-manager# echo "Aurevoir" > test/aurevoir

# Encrypt a directory
root@kirk:~/Projects/crypt-manager# ./crypt-manager --crypt test
Password: azerty

[...]

# List the content of the directory unmounted
root@kirk:~/Projects/crypt-manager# ls test

# Open the encrypted directory
root@kirk:~/Projects/crypt-manager# ./crypt-manager --open test
Password: azerty

# List the content of the mounted encrypted directory
root@kirk:~/Projects/crypt-manager# ls test
aurevoir  bonjour  lost+found

# Close it
root@kirk:~/Projects/crypt-manager# ./crypt-manager --close test
# List if content
root@kirk:~/Projects/crypt-manager# ls test

# Decrypt it
root@kirk:~/Projects/crypt-manager# ./crypt-manager --decrypt test
Password: azerty
aurevoir  bonjour  lost+found