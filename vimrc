syntax on
set tabstop=4
set shiftwidth=4
set expandtab
set autoindent
set number
set ruler
set title
set ttyfast " Prettier

" Search settings
set incsearch
set ignorecase
set smartcase
set hlsearch
nmap \q :nohlsearch<CR>
nmap \e :NERDTreeToggle<CR>

filetype plugin on
filetype plugin indent on
let $PS1='(vim) [\u@\h \W]# '

execute pathogen#infect() 

let g:NERDTreeWinSize=40
autocmd VimEnter * NERDTree

set background=dark
colorscheme solarized

