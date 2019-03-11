#!/bin/bash 

function _setup_screenkey {
    pip install -e bzr+lp:python-distutils-extra#egg=distutils-extra
    pip install -e git+https://gitlab.com/wavexx/screenkey#egg=screenkey

    #local dest=$1
    #if [ -n "${dest}" ]; then
    #    dest="./src"
    #fi
    #if [ ! -d "${dest}" ]; then
    #    mkdir -p "${dest}"
    #fi
    #sudo dnf install -y bzr
    #bzr branch lp:python-distutils-extra
    #cd python-distutils-extra/
    #cd ..
    #git clone https://gitlab.com/wavexx/screenkey
    #cd screenkey/
    #pip install .
    #cd ..
}

function _setup_simplescreenrecorder {
    rpm -Uvh https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-stable.noarch.rpm
    sudo dnf install -y slop simplescreenrecorder
}

function _setup_editors {
    sudo dnf install -y openshot lives
}

function main {
    _setup_screenkey
    _setup_simplescreenrecorder
    #_setup_editors
}

if 
