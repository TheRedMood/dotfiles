#!/bin/bash

xrdb -merge .Xresources

exec dwm
