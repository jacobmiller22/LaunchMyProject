#!/bin/sh
realpath() {
    [[ $1 = /* ]] && echo "start${1}end" || echo "$PWD/${1#./}"
}

python3 "${0/execute.sh.command/driver.py}"

