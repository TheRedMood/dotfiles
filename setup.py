#!/usr/bin/python2.7
# Script was first made the
# 15. sep 2012
# And it was made by: TheRedMood < Teodor Spaeren >
#
# This aims to be the setup file for my confiurations. It is based around the
# idea that linking everything will make updating the main repo much easier.
# I hope that you all have a nice day and enjoy the script!

import os

# Global variables
HOME = os.path.expanduser('~')
DOTDIR = os.path.expanduser('~/.dotfiles')

dotfiles = []
class Dotfile:
    """ A object for each file or directory that needs to be setup. """
    def __init__(self, name, gitplace, sysplace, isdir=False, place=""):
        self.name     = name
        self.gitplace = gitplace
        self.sysplace = sysplace
        self.isdir    = isdir
        self.place    = place

        dotfiles.append(self)

    def exists(self):
        if self.isdir:
            return os.path.isdir(self.sysplace)
        else:
            return os.path.isfile(self.sysplace)

    def placetest(self):
        if self.place != "" and not os.path.isdir(self.place):
            os.system("mkdir {0}".format(self.place))

    def link(self):
        os.system("ln -s {0} {1}".format(self.gitplace, self.sysplace))

# Functions
def warn():
    answer = input("(Y/N): ")
    if answer.lower() == 'y': return True
    else: return False

# We need all the DotFile objects. Here we have all file objects
xres  = Dotfile("Xresources", "{0}/Xresources".format(DOTDIR),  "{0}/.Xresources".format(HOME))

vim   = Dotfile("vim"  , "{0}/vimrc".format(DOTDIR)  , "{0}/.vimrc".format(HOME)  )
zsh   = Dotfile("zsh"  , "{0}/zshrc".format(DOTDIR)  , "{0}/.zshrc".format(HOME)  )
bash  = Dotfile("bash" , "{0}/bashrc".format(DOTDIR) , "{0}/.bashrc".format(HOME) )
conky = Dotfile("conky", "{0}/conkyrc".format(DOTDIR), "{0}/.conkyrc".format(HOME))
xinit = Dotfile("xinit", "{0}/xinitrc".format(DOTDIR), "{0}/.xinitrc".format(HOME))

# We need to check directories to.
scripts = Dotfile("scripts", "{0}/scripts".format(DOTDIR), "{0}/scripts".format(HOME), True)
vimdir  = Dotfile("vimdir", "{0}/vim".format(DOTDIR), "{0}/.vim".format(HOME), True)

# Here we have the cases where theres extra checking to be done
mpd     = Dotfile("mpd", "{0}/config/mpd.conf".format(DOTDIR), "{0}/.mpd/mpd.conf".format(HOME), False, "{0}/.mpd/".format(HOME))
canto   = Dotfile("canto", "{0}/config/cantoconf.py".format(DOTDIR), "{0}/.canto/conf.py".format(HOME), False, "{0}/.canto/".format(HOME))
ncmpcpp = Dotfile("ncmpcpp", "{0}/config/ncmpcppconf".format(DOTDIR),  "{0}/.ncmpcpp/config".format(HOME), False, "{0}/.ncmpcpp".format(HOME))
wmfs    = Dotfile("wmfs", "{0}/config/wmfs".format(DOTDIR), "{0}/.config/wmfs".format(HOME), True, "{0}/.config".format(HOME))


# We need to use all the elements up there
for dotfile in dotfiles:
    print("Linking {0}...".format(dotfile.name), end=' ')

    if not dotfile.exists() and warn():
        dotfile.placetest()
        dotfile.link()
    else:
        print("Skipping.")

#------------------NON LINKING OPERATIONS---------------------#
# I need to initalize the modules
print("Starting git submodule init:")
os.system("git submodule init")

# Now we need to update them
print("Starting git submodule update:")
os.system("git submodule update")

# Getting archey
os.system("curl https://raw.github.com/djmelik/archey/master/archey > {0}/scripts/archey".format(HOME))
os.system("chmod +x {0}/scripts/archey".format(HOME))
