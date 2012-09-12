autoload -U compinit promptinit
autoload -U colors && colors
compinit
promptinit

# Sets the compeltion to be menudriven
zstyle ':completion:*' menu select
# This will set the default prompt to the walters theme
prompt walters

export PROMPT="[%{$fg[yellow]%}%B%n@%m%b%{$reset_color%}]::[%{$fg[yellow]%}%B%~%b%{$reset_color%}] "
