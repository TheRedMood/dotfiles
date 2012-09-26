#!/usr/bin/python2.7
# Script was first made the 
# 15. sep 2012
# And it was made by: TheRedMood < Teodor Spaeren >
#
# This aims to be the setup file for my confiurations. It is based around the
# idea that linking everything will make updating the main repo much easier.
# I hope that you all have a nice day and enjoy the script!

import os
import sys

# Global variables
HOME = os.path.expanduser('~')
DOTDIR = os.path.expanduser('~/.dotfiles')

# Functions
def warn():
    answer = raw_input("(Y/N): ")
    if answer.lower() == 'y':
        return True
    else:
        return False 

# All the tests
iscopy  = os.getcwd() == DOTDIR
isthere = os.path.isdir(DOTDIR)

# We need to test the files to not overwrite anything!
isvim   = os.path.isfile("%s/.vimrc"  % HOME)
iszsh   = os.path.isfile("%s/.zshrc"  % HOME)
isbash  = os.path.isfile("%s/.bashrc" % HOME)
isourico = os.path.isfile("%s/.ouricorc" % HOME)
isXresources = os.path.isfile("%s/.Xresources" % HOME)
isconky = os.path.isfile("%s/.conkyrc" % HOME)
isxinit = os.path.isfile("%s/.xinitrc" % HOME)

# Testing the dirs is also important
iscanto   = os.path.isdir("%s/.canto"   % HOME)
ismpd     = os.path.isdir("%s/.mpd"     % HOME)
isncmpcpp = os.path.isdir("%s/.ncmpcpp" % HOME)
isechinus = os.path.isdir("%s/.echinus" % HOME)
isscripts = os.path.isdir("%s/scripts"  % HOME)
isvimdir  = os.path.isdir("%s/.vim"     % HOME)
ismusic   = os.path.isdir("%s/music"    % HOME)
isimages   = os.path.isdir("%s/images"   % HOME)

# Having all the values in a dict makes it easier to test.
tests = {'vimrc': isvim, 'bashrc': isbash, 'canto': iscanto,
        'zshrc': iszsh, 'ourico': isourico, 'Xresources': isXresources,
        'mpd': ismpd, 'ncmpcpp': isncmpcpp}

# We would not want to copy over the .dotfiles directory
if not iscopy:
    # Giving out error messages.
    if isthere : 
        print "You already have a .dotfiles dictonary."
    else: 
        print "Copy this to %s" % DOTDIR
    sys.exit()

# Disabled due to testing purposes
#for k, v in tests.iteritems():
#    print k, v

#--------------------ADD ITEMS TO LINK OR LIST HERE---------------#
# VIM
print "Linking .vimrc...",
if not isvim and warn():
    os.system("ln -s %s/vimrc %s/.vimrc" % (DOTDIR, HOME))
else:
    print "Skipping."

# ZSH
print "Linking .zshrc...",
if not iszsh and warn():
    os.system("ln -s %s/zshrc %s/.zshrc" % (DOTDIR, HOME)) 
else:
    print "Skipping."

# CANTO
print "Linking .canto...",
if not iscanto and warn():
    os.system("ln -s %s/canto/ %s/.canto" % (DOTDIR, HOME))
else:
    print "Skipping."

# XRESOURCES
print "Linking .Xresources...",
if not isXresources and warn():
    os.system("ln -s %s/Xresources %s/.Xresources" % (DOTDIR, HOME))
else:
    print "Skipping."

# ECHINUS
print "Linking .echinus...",
if not isechinus and warn():
    os.system("ln -s %s/echinus %s/.echinus" % (DOTDIR, HOME))
else:
    print "Skipping."

# MPD
print "Linking .mpd...",
if not ismpd and warn():
    os.system("ln -s %s/mpd %s/.mpd" % (DOTDIR, HOME))
else: 
    print "Skipping."

# NCMPCPP
print "Linking .ncmpcpp...",
if not isncmpcpp and warn():
    os.system("ln -s %s/ncmpcpp %s/.ncmpcpp" % (DOTDIR, HOME))
else: 
    print "Skipping."

# CONKY 
print "Linking .conkyrc...",
if not isconky and warn():
    os.system("ln -s %s/conkyrc %s/.conkyrc" % (DOTDIR, HOME))
else: 
    print "Skipping."

# OURICO
print "Linking .ouricorc...",
if not isourico and warn():
    os.system("ln -s %s/ouricorc %s/.ouricorc" % (DOTDIR, HOME))
else: 
    print "Skipping."

# XINIT
print "Linking .xinitrc...",
if not isxinit and warn():
    os.system("ln -s %s/xinitrc %s/.xinitrc" % (DOTDIR, HOME))
else: 
    print "Skipping."

# XINIT
print "Linking scripts...",
if not isscripts and warn():
    os.system("ln -s %s/scripts %s/scripts" % (DOTDIR, HOME))
else: 
    print "Skipping."

# VIM DIR
print "Linking .vim...",
if not isvimdir and warn():
    os.system("ln -s %s/vim %s/.vim" % (DOTDIR, HOME))
else: 
    print "Skipping."

#------------------NON LINKING OPERATIONS---------------------#
# I need to initalize the modules
print "Starting git submodule init:"
os.system("git submodule init")

# Now we need to update them
print "Starting git submodule update:"
os.system("git submodule update")


#-----------------THEREDMOOD SPECIFIC-----------------------------#
done = raw_input("Are you TheRedMood? (Y/N): ")
if done.lower() != "y":
    sys.exit()
# MUSIC
print "Creating music/...",
if not ismusic and warn():
    os.system("mkdir %s/music" % (HOME))
else: 
    print "Skipping."

print "Creating images/...",
if not isimages and warn():
    os.system("mkdir %s/images" % (HOME))
else: 
    print "Skipping."
