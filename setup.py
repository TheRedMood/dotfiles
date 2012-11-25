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
    answer = input("(Y/N): ")
    if answer.lower() == 'y':
        return True
    else:
        return False 

# All the tests
iscopy  = os.getcwd() == DOTDIR
isthere = os.path.isdir(DOTDIR)

# We need to test the files to not overwrite anything!
isvim        = os.path.isfile("%s/.vimrc"          % HOME)
iszsh        = os.path.isfile("%s/.zshrc"          % HOME)
isbash       = os.path.isfile("%s/.bashrc"         % HOME)
isXresources = os.path.isfile("%s/.Xresources"     % HOME)
isconky      = os.path.isfile("%s/.conkyrc"        % HOME)
isxinit      = os.path.isfile("%s/.xinitrc"        % HOME)
ismpd        = os.path.isfile("%s/.mpd/mpd.conf"   % HOME)
iscanto      = os.path.isfile("%s/.canto/conf.py"  % HOME)
isncmpcpp    = os.path.isfile("%s/.ncmpcpp/config" % HOME)
# Testing the dirs is also important
isscripts = os.path.isdir("%s/scripts"             % HOME)
isvimdir  = os.path.isdir("%s/.vim"                % HOME)

# Having all the values in a dict makes it easier to test.
#tests = {'vimrc': isvim, 'bashrc': isbash, 'canto': iscanto,
#        'zshrc': iszsh, 'ourico': isourico, 'Xresources': isXresources,
#        'mpd': ismpd, 'ncmpcpp': isncmpcpp}

# We would not want to copy over the .dotfiles directory
if not iscopy:
    # Giving out error messages.
    if isthere : 
        print("You already have a .dotfiles dictonary.")
    else: 
        print("Copy this to %s" % DOTDIR)
    sys.exit()

# Disabled due to testing purposes
#for k, v in tests.iteritems():
#    print k, v

#--------------------ADD ITEMS TO LINK OR LIST HERE---------------#
# VIM
print("Linking .vimrc...", end=' ')
if not isvim and warn():
    os.system("ln -s %s/vimrc %s/.vimrc" % (DOTDIR, HOME))
else:
    print("Skipping.")

# ZSH
print("Linking .zshrc...", end=' ')
if not iszsh and warn():
    os.system("ln -s %s/zshrc %s/.zshrc" % (DOTDIR, HOME)) 
else:
    print("Skipping.")

# CANTO
print("Linking .canto...", end=' ')
if not iscanto and warn():
    if not os.path.isdir("{0}/.canto/".format(HOME)):
        os.system("mkdir {0}/.canto".format(HOME))
    os.system("ln -s %s/config/cantoconf.py %s/.canto/conf.py" % (DOTDIR, HOME))
else:
    print("Skipping.")

# XRESOURCES
print("Linking .Xresources...", end=' ')
if not isXresources and warn():
    os.system("ln -s %s/Xresources %s/.Xresources" % (DOTDIR, HOME))
else:
    print("Skipping.")

# MPD
print("Linking .mpd...", end=' ')
if not ismpd and warn():
    if not os.path.isdir("{0}/.mpd".format(HOME)):
        os.system("mkdir {0}/.mpd".format(HOME))
    os.system("ln -s %s/config/mpd.conf %s/.mpd/mpd.conf" % (DOTDIR, HOME))
else: 
    print("Skipping.")

# NCMPCPP
print("Linking .ncmpcpp...", end=' ')
if not isncmpcpp and warn():
    if not os.path.isdir("{0}/.ncmpcpp".format(HOME)):
        os.system("mkdir {0}/.ncmpcpp".format(HOME))
    os.system("ln -s %s/config/ncmpcppconf %s/.ncmpcpp/config" % (DOTDIR, HOME))
else: 
    print("Skipping.")

# CONKY 
print("Linking .conkyrc...", end=' ')
if not isconky and warn():
    os.system("ln -s %s/conkyrc %s/.conkyrc" % (DOTDIR, HOME))
else: 
    print("Skipping.")

# XINIT
print("Linking .xinitrc...", end=' ')
if not isxinit and warn():
    os.system("ln -s %s/xinitrc %s/.xinitrc" % (DOTDIR, HOME))
else: 
    print("Skipping.")

# SCRIPTS 
print("Linking scripts...", end=' ')
if not isscripts and warn():
    os.system("ln -s %s/scripts %s/scripts" % (DOTDIR, HOME))
else: 
    print("Skipping.")

# VIM DIR
print("Linking .vim...", end=' ')
if not isvimdir and warn():
    os.system("ln -s %s/vim %s/.vim" % (DOTDIR, HOME))
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
