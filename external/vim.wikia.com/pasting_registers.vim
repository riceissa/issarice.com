" Pick one
inoremap <C-V> <C-R><C-R>+
inoremap <C-V> <C-R><C-O>+
inoremap <C-V> <C-\><C-O>"+gP
inoremap <C-V> <C-R>=<SID>paste1()<CR>
inoremap <C-V> <C-R>=<SID>paste2()<CR>
inoremap <C-V> <C-R><C-O>=<SID>paste3()<CR>
inoremap <C-V> <C-R><C-O>=<SID>paste4()<CR>
inoremap <C-V> x<Esc>:<C-U>call setreg('+', getreg('+', 1, 1), 'c')<CR>"+gP"_s
inoremap <C-V> x<Esc>"=@+.'xy'<CR>gPFx"_2x"_s
exe 'inoremap <script> <C-V> ' . g:paste#paste_cmd['i']

function! s:paste1()
  if col('.') >= col('$')
    normal! "+gp
    return "\<Right>"
  else
    normal! "+gP
    return ''
  endif
endfunction

function! s:paste2()
  " Force the register to be characterwise
  call setreg('+', getreg('+', 1, 1), 'c')

  if col('.') >= col('$')
    normal! "+gp
    return "\<Right>"
  else
    normal! "+gP
    return ''
  endif
endfunction

function! s:paste3()
  return join(getreg('+', 1, 1), "\n")
endfunction

function! s:paste4()
  return getreg('+', 1, 1)
endfunction
