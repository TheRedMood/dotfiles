#!/bin/sh
LANG=C
FONT='envy code r:normal:pixelsize=12'
BG="#2e3436"
FG="#696969"

SW=1024
BAR=`xprop -root _OURICO_WINDOW|awk '{ print $5 }'`
DZEN="dzen2 -fn $FONT -fg $FG -bg $BG  -y 1 -em $BAR"
echo $DZEN
pkill dzen 
pkill conky
X=600
conky 2>/dev/null| $DZEN -x $X -w $(($SW-$X-2)) -ta r -fg "#696969" &
~/Scripts/tagnames.sh|$DZEN -p -w 235 -ta l -bg "#2e3436" -fg "#696969" -x 1

