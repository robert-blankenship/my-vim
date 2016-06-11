#!/usr/bin/python
import os
import subprocess
import shutil
import getpass
import sys

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

def setupGit():
    answer = raw_input("Would you like to set up Git? (y/n)")

    if answer == "y":
        subprocess.check_call(["git", "config", "--global", "-e"])
    elif answer =="n":
        pass
    else:
        raise Exception("Invalid response")

def main():
    setupPathogen()
    installPlugins()
    setupGit()

if __name__ == '__main__': main()


