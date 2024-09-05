---
title: What is the point of Lisp?
author: Issa Rice
created: 2024-03-02
date: 2024-03-02
---

(originally written on 2023-12-27)

i hate lisp, especially lisp-2, but even lisp-1, because my brain doesn't want to understand `quote`. what follows is some introspection i did to understand `quote` better; by the end i had a deeper appreciation of what the point of lisp was, and some thoughts on how to improve it.

i think the thing that's weird about scheme is that in most languages, many expressions (in particular, lists) evaluate to themselves. e.g. in both python and haskell, `[1,2,3]` evaluates to `[1,2,3]`, i.e., itself! but in scheme, `(1 2 3)` does not evaluate to itself... because it tries to call the function `1` on the arguments `2` and `3`, which errors because `1` is not a function. so to get the evaluated list `(1 2 3)`, you need to write `'(1 2 3)`. but importantly, `'(1 2 3)` does not evaluate to itself either; it evaluates to the list `(1 2 3)`. otoh, some things like the integer `2` still evaluate to themselves.

this "lists don't just evaluate to themselves" is what makes lisps very hard to work with, i think. and ultimately this comes from the abuse of notation -- using `(a b c)` for both function calls and for data (or as paul graham says "\[...] one of the most distinctive features of Lisp: code and data are made out of the same data structures"). that's why lisp needs the `'` (or `quote`) to distinguish between data and programs, because the programs look just like the data!

i wonder why michael nielsen did not make this point in his "maxwell's laws for computer science" essay. (update 2024-03-02: i guess he probably thought it was obvious because paul graham says it on page 3 of his lisp article...)

2024-01-09: maybe this is the whole point though? because then you can manipulate function calls as if they're data? (otherwise you'd need a separate syntax to be able to manipulate the syntax tree.) i don't have a good idea of where that'd be a useful thing to do though. like, you want to swap out the function but keep the arguments the same? why would you want to do that? in haskell or python you don't need to do this ever...

and i guess they chose the `'( ... )` notation because then you don't need to backslash-escape everything.

so in lisp, you can easily do things like "take this function, and anywhere it calls `sin(x)`, you should replace it with `sin(sin(x))`". but in haskell you can just replace `sin` with an argument `f` and then just pass in `sin . sin` instead of `sin`... **manipulating programs just doesn't seem very useful, because you can just edit the programs in your editor instead of modifying them in the interpreter!** whereas data can be very large so you don't want to manually edit it. that's the whole point of having a computer! so it seems to come down to this: programs are authored by humans, so by assumption they are compact enough to edit by hand, so therefore you don't benefit from having the same syntax for programs (esp. function calls) and data.

however, i should still go find some real examples of programs written in idiomatic lisp where the manipulation of programs is done in an essential manner, if such a thing even exists (no one has ever shown me such a thing, but then again i don't really hang out with people who know a lot about Lisp). like, if it did exist, then it would be much harder to write it in haskell or something. so i'm doubtful such a thing can exist.

ok i guess maybe a REAL example is if you're writing an interpreter? in that case, data=program. it's almost as if lisp was specifically designed to write its own interpreter...

but wait! michael nielsen wrote a lisp interpreter in python no problem. so lisp is a language that it's easy to write an interpreter _for_, but not necessarily easier to write an interpreter _in_.

(update 2024-03-02: after i wrote the above, i read paul graham's essay which says "The unusual thing about Lisp -- in fact, the defining quality of Lisp -- is that it can be written in itself." Is the whole point of Lisp just this self-referential madness of "it is the programming language such that it allows you to extremely trivially write an interpreter of that very programming language"?)

you know, i think the best of both worlds might have been using `[...]` for lists and `(...)` for function calls, and then just not having quote. then `[1 2 3]` evaluates to `[1 2 3]`. but `(f 1 2 3)` will do a function call. `[1 2 3]` is shorthand for `(cons 1 (cons 2 (cons 3 [])))`. `car` and `cdr` can only be used on `[...]` brackets (just like `(car 3)` errors in scheme, so would `(car ( ... ))` in this hypothetical language). then you can STILL easily write an interpreter for this language because all the brackets are there -- no need to do fancy parsing. BUT the big advantage would be that you don't have `quote`, and there is clear separation between data and code: data evaluate to themselves, code evaluates down to something else.

you wouldn't easily be able to write an interpreter in this language unless support for strings is added -- because there's no way to pass around function calls without evaluating them. but in python you would just as easily write one, i think.

2024-01-10: also, there'd be currying so `(f x y z)` would be the same thing as `(((f x) y) z)`. haskell does make this much nicer by not requiring the parentheses. but that makes parsing much harder.

2024-08-27: you can't implement a while loop using a for loop in python because `while_loop(condition, statements)` cannot be done; you can't pass a bunch of statements into a function. in lisp, you can quote it and pass it in! that's the difference.

2024-08-31: so lisp is more like a meta programming language. a simple language that you can use to make your own programming language. the only drawback is that you have to stick with ugly parentheses, so you can't change the overarching syntax of the language. but you can implement all the nice programming constructs that you would want, like list comprehension, different loops, etc.

2024-09-04: is there a useful example of such a thing? one example might be handling nested try-catch statements (although this whole style of error handling is debatable...). i think i've had situations where i wish i could pass groups of statements into a function, and couldn't, in python.