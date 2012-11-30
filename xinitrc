#exec ck-launch-session dbus-launch wmfs &
#exec wmfs &
#wmpid=$! # Here, we save the PID of wmfs
exec awesome
# Here we do all other jizz jazz
xcompmgr -c &
xrdb -merge ~/.Xresources &
#nitrogen --restore &
eval `cat ~/scripts/fehbg`
mpD &

# fonts
xset +fp /usr/share/fonts/local
xset fp rehash
#wait $wmpid # Here we are wainting for the end of WMFS, wmfs -c quit
