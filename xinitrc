#!/bin/bash


xrdb ~/dotfiles/colors/Xresources-thayers
xrdb -merge ~/.Xresources

#xcompmgr -c &
nitrogen --restore &
mpd &
~/.dropbox-dist/dropboxd & 

# fonts
xset +fp /usr/share/fonts/local
xset fp rehash


#conky | while read -r; do xsetroot -name "$REPLY"; done &
#exec ~/.dwm/dwm
exec herbstluftwm
