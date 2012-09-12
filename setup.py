import os

# Global variables
HOME = os.path.expanduser('~')
DOTDIR = os.path.expanduser('~/.dotfiles')

# All the tests
iscopy = os.getcwd() == DOTDIR
isthere = os.path.isdir(DOTDIR)
isvim = os.path.isfile("%s/.vimrc" % HOME)

print isvim
print "%s/.vimrc" % DOTDIR
