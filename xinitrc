#!/bin/bash


xrdb ~/.dotfiles/colors/Xresources-tommytiger
xrdb -merge ~/.Xresources

#xcompmgr -c &
nitrogen --restore &
mpd &
~/.dropbox-dist/dropboxd & 

# fonts
xset +fp /usr/share/fonts/local
xset fp rehash

setxkbmap no

#conky | while read -r; do xsetroot -name "$REPLY"; done &
#exec ~/.dwm/dwm
exec herbstluftwm
