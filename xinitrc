#!/bin/bash


xrdb ~/.dotfiles/colors/Xresources-tommytiger
xrdb -merge ~/.Xresources

#xcompmgr -c &
#compton &
nitrogen --restore &
mpd &
~/.dropbox-dist/dropboxd & 

# fonts
xset +fp /usr/share/fonts/local
xset fp rehash

setxkbmap -layout no

# this is xmonad stuff
xsetroot -cursor_name left_ptr

#conky | while read -r; do xsetroot -name "$REPLY"; done &
#exec dwm
#exec herbstluftwm
exec xmonad
#exec snapwm/snapwm
