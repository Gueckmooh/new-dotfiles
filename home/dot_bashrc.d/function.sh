# -*- mode: shell-script; -*-

me()
{
    TMUX_S=$(tmux display-message -p "#S")
    if test "$TMUX_S" != "0"; then
        DAEMONIZE="--daemon=$TMUX_S"
        SOCKET="--socket=$TMUX_S"
    else
        DAEMONIZE="--daemon"
    fi
    if [[ $(ps aux | grep "emacs $DAEMONIZE" | wc -l) == 1 ]]; then
        return
    fi
    emacsclient "$SOCKET" -n $*
}
