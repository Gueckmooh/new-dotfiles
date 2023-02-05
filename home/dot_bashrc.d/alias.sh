# colors
if [ -x /usr/bin/dircolors ]; then
    alias ls='ls --color=auto'
    alias grep='grep --color=auto'
    alias egrep='egrep --color=auto'
    alias fgrep='fgrep --color=auto'
fi

# ls
alias l='ls -CF'
alias ll='ls -CFlh'
alias la='ls -ACF'

alias ma='emacs -nw'
alias c='caja . &'

# grep
alias rgrep='grep -R'

alias wl='echo $[`ls -l | wc -l`-1]'
alias clipboard='xclip -selection clipboard'

# Get screenshots
alias cdscreen='[[ -d ~/Images/screenshots/$(date +%F)-screenshots ]] && cd ~/Images/screenshots/$(date +%F)-screenshots || echo "No screenshots taken today"'

# If the os is arch, use `see` as in debian
if [[ "$(awk -vFS== '/^ID/ {print $2}' /etc/os-release)" = arch ]]; then
    alias see='run-mailcap'
fi

# Minimize terminal in awesome
alias n='echo client.focus.minimized = true | awesome-client'

# Stop and enable goautolock
alias autolock-off='kill -s SIGSTOP $(pgrep goautolock) 2> /dev/null'
alias autolock-on='kill -s SIGCONT $(pgrep goautolock) 2> /dev/null'

# SSH
alias ssh="TERM=xterm-256color ssh"
