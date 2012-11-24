call pathogen#infect()

filetype plugin indent on
filetype plugin on

"Powerline stuff
set nocompatible
set laststatus=2
set encoding=utf-8
let g:Powerline_symbols = 'compatible'

" Tabs
set tabstop=4
set shiftwidth=4
set expandtab

" Autoindent
set autoindent

" Line numbers
set nu

" Looks
"set background=light " you can use `dark` or `light` as your background
syntax on
color mango

" NERDtree stuff
map <F4> :NERDTreeToggle<cr>

" ColorChooser stuff
map <silent><F3> :NEXTCOLOR<cr> 
map <silent><F2> :PREVCOLOR<cr>

" automatically open and close the popup menu / preview window
au CursorMovedI,InsertLeave * if pumvisible() == 0|silent! pclose|endif

" Backup files, is puted in a sorted directory to not cluter it up.
set backupdir=~/.dotfiles/vim/tmpfiles,.
set directory=~/.dotfiles/vim/tmpfiles,.

" Setting up Tags list settings
nnoremap <silent> <F8> :TlistToggle<CR>
