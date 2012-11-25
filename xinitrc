#exec ck-launch-session dbus-launch wmfs &
exec wmfs &
wmpid=$! # Here, we save the PID of wmfs

# Here we do all other jizz jazz
#[[ -f ~/.Xresources ]] && xrdb -merge ~/.Xresources

xrdb -merge ~/.Xresources
nitrogen --restore &
mpd &

wait $wmpid # Here we are wainting for the end of WMFS, wmfs -c quit
