

OS="`uname`"

case $OS in
    'Linux')
        echo 'Linux'
        alias ls='ls --color=auto'
        ;;
    'FreeBSD')
        echo 'FreeBSD'
        alias ls='ls -G'
        ;;
    'MINGW64_NT-10.0-18363')
        echo "Executing on Windows. Version: $OS"
        py ./driver.py
        ;;
    'Darwin') 
        echo "Executing on MacOS. Version: $OS"
        realpath() {
            [[ $1 = /* ]] && echo "start${1}end" || echo "$PWD/${1#./}"
        }

        python3 "${0/execute.sh.command/driver.py}"
        ;;
    'SunOS')
        echo 'Solaris'
        ;;
    'AIX') 
        echo AIX;;

    *) ;;
esac
