# LOADING IN THE DIFFRENT THINGS!
autoload -U compinit promptinit
autoload -U colors && colors
compinit
promptinit

# Sets the compeltion to be menudriven
zstyle ':completion:*' menu select

# CONFIGURING ALIASES
alias ls="ls --color=auto"   
alias grep="grep --color=auto"

# EXPORTING THE PROMPTS
prompt walters
export PROMPT="[%{$fg[yellow]%}%B%n%b%{$reset_color%}]::[%{$fg[yellow]%}%B%~%b%{$reset_color%}] "

# PATH SETTINGS
PATH=$PATH;$(ruby -rubygems -e "puts Gem.user_dir")/bin/
export PATH