# Here we do all other jizz jazz
xcompmgr -c &
xrdb -merge ~/.Xresources &
#nitrogen --restore &
eval `cat ~/scripts/fehbg`
mpd &

# fonts
xset +fp /usr/share/fonts/local
xset fp rehash

exec ~/dwm/dwm
