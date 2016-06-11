#!/usr/bin/python
import os
import subprocess
import shutil

def setupPathogen():
    for folder in ['bundle', 'autoload']:
        if os.path.isdir(folder):
            print "folder '%s' already exists" % folder 
            pass
        else:
            print "creating folder '%s'" % folder 
            os.mkdir(folder)
    os.chdir("autoload")
    subprocess.check_call(["curl", "-O", "https://raw.githubusercontent.com/tpope/vim-pathogen/master/autoload/pathogen.vim"])
    os.chdir("../")


def installPlugins():
    os.chdir("bundle")

    vimPlugins = [
        "https://github.com/scrooloose/nerdtree",
        "https://github.com/vim-airline/vim-airline",
        "https://github.com/chase/vim-ansible-yaml",
        "https://github.com/kchmck/vim-coffee-script",
        "https://github.com/altercation/vim-colors-solarized",
        "https://github.com/Glench/Vim-Jinja2-Syntax",
        "https://github.com/derekwyatt/vim-scala"
    ]

    for plugin in vimPlugins:
        try:
            subprocess.check_call(["git", "clone", plugin])
        except:
            pass

    os.chdir("../")

def installVimrc():
    print "Installing VIM configuration file."
    print "Creating symlink between vimrc and ../.vimrc"
    os.symlink("vimrc", ".vimrc")
    if not os.path.exists("../.vimrc"):
        os.rename(".vimrc", "../.vimrc")
        os.remove(".vimrc")
        print "Vimrc has been installed."
    else:
        print "../.vimrc already exists"

setupPathogen()
installPlugins()
installVimrc()

