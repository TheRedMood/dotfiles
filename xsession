#!/bin/bash

xrdb -merge .Xresources
xcompmgr -c &
nitrogen --restore &
mpd &

# fonts
xset +fp /usr/share/fonts/local
xset fp rehash

exec ~/dwm/dwm
