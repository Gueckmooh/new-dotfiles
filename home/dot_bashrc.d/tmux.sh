if which fzf 2>&1 > /dev/null; then
    __ta_projects__() {
        if [[ -z "$TMUX" ]]
        then
            ta -c ~/projects/
        else
            tmux popup -w30% -h30% -E "~/bin/ta -c ~/projects"
        fi
    }

    bind -m emacs-standard -x '"\C-g": __ta_projects__'
fi
