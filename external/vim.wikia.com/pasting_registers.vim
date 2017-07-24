" Pick one of the following mappings.

" Mapping 1
inoremap <C-V> <C-R><C-R>+

" Mapping 2
inoremap <C-V> <C-R><C-O>+

" Mapping 3
inoremap <C-V> <C-\><C-O>"+gP

" Mapping 4
inoremap <C-V> <C-\><C-O>:<C-U>call setreg('+',getreg('+',1,1),'c')<CR><C-R><C-O>+

" Mapping 5
inoremap <C-V> <C-R>=<SID>paste1()<CR>

function! s:paste1()
  if col('.') >= col('$')
    normal! "+gp
    return "\<Right>"
  else
    normal! "+gP
    return ''
  endif
endfunction


" Mapping 6
inoremap <C-V> <C-R>=<SID>paste2()<CR>

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

" Mapping 7
inoremap <C-V> <C-R><C-O>=<SID>paste3()<CR>

function! s:paste3()
  return join(getreg('+', 1, 1), "\n")
endfunction

" Mapping 8
inoremap <C-V> x<Esc>:<C-U>call setreg('+',getreg('+',1,1),'c')<CR>"+gP"_s

" Mapping 9
inoremap <C-V> x<Esc>"=@+.'xy'<CR>gPFx"_2x"_s

" Mapping 10
" Assuming has('virtualedit'); otherwise it is identical to the mapping above
exe 'inoremap <script> <C-V> ' . g:paste#paste_cmd['i']
