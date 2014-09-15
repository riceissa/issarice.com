---
layout: default
title: How to use platex to typeset Japanese documents (Debian Wheezy)
comments: "yes"
disqus-id: 870d28e40a661cde90d2a1f30bb9d18cd987d023
math: ""
last-major-revision-date:
license: "CC-BY"
tags: computing
---


## How-to

It easy enough to simply download and install the entire TeXLive 2012 distribution with `sudo aptitude install texlive-full`; however, I am pretty sure only the CJK support is necessary for the following.
To begin, therefore, install the CJK support package with:

~~~~
sudo aptitude install texlive-lang-cjk
~~~~

Check to see that the above installed `platex`; type `platex` into the terminal and see if you get:

~~~~
This is e-pTeX, Version 3.1415926-p3.3-110825-2.4 (utf8.euc) (TeX Live 2012/Debi
an)
 restricted \write18 enabled.
**
~~~~

(`Ctrl`-`D` to escape.)

We are now ready for our first document.
This how-to will assume that the filename is called `hello_world.tex`.

Enter the following body of text using any text editor (copy-pasting is fine); assuming you are familiar with the syntax of LaTeX (or similar), the following should also look familiar:

~~~~latex
\documentclass[mingoth,12pt]{jarticle}
%\documentclass[mingoth,12pt]{jsarticle}
    %% See http://oku.edu.mie-u.ac.jp/~okumura/jsclasses/ for the
    %% differences between jarticle and jsarticle, but beware, the page
    %% is in Japanese.
\usepackage[letterpaper,margin=1in]{geometry}
\usepackage{otf}
\usepackage{okumacro}
    %% For useful features such as `\ruby{漢字}{かんじ}` for furigana and
    %% `\kenten{}` for dots above characters for emphasis.
\newcommand{\jdash}{\――}
    %% For the Japanese double-width dash; this is much easier than hunting
    %% around for the right type of dash.
\newcommand{\jell}{⋯\penalty10000⋯}
    %% Again, this is easier than looking for the correct unicode
    %% character.
%% When compiling, use the command (on the command line):
    %%`platex hello_world.tex && dvipdfmx -f /usr/share/texlive/texmf-dist/fonts/map/dvipdfmx/jfontmaps/otf-ipaex.map hello_world.dvi`

\begin{document}

\section{\LaTeX\ 入門}

こんにちは。
強調するには、\emph{ゴシック体}を使うか、\kenten{圏点}をつけるか、いろいろ選べます。
数学もできます：
\[
    \int_1^x \frac{1}{t}\,dt = \log x。
\]
もちろんルビを\ruby{振}{ふ}ることもできます。
この他にも「\jell 」や「\jdash 」などの記号が、\LaTeX のコマンドを入力することによって出力できます。

\section{Introduction to \LaTeX}

Hello world.
To emphasize words, one can use the gothic font or dots above the characters---either one will work.
Mathematics is also possible:
\[
    \int_1^x \frac{1}{t}\,dt = \log x.
\]
One can also produce special typographic symbols such as ``\jell'' and ``\jdash'' by entering the correct \LaTeX\ commands.

\end{document}
~~~~

To compile the document, run:

    platex hello_world.tex && dvipdfmx hello_world.dvi

([Example output](http://riceissa.files.wordpress.com/2014/04/example1.pdf).)

However, we notice that the font is all gothic (sans-serif).
To fix this, i.e., to use a mincho (serif) font, we must use a “font mapping”.
I’m not entirely sure how font mappings work, but I think the general idea is that one wants to replace each character in the DVI file in succession using a “map” file and a font file, so that the desired font appears in the final PDF.
Therefore, we use:

    platex hello_world.tex && dvipdfmx -f /usr/share/texlive/texmf-dist/fonts/map/dvipdfmx/jfontmaps/otf-ipaex.map hello_world.dvi

([Example output](http://riceissa.files.wordpress.com/2014/04/example2.pdf).)

If the `.map` file is not located in the same place, use `locate filename`.

## References

Below are sources that were especially helpful in finding out how to use `platex`.
One thing that will be noticed is that all sources are in Japanese; this is to be expected, as `platex` was designed specifically to deal with Japanese typesetting.
One goal in writing this article was to provide some of the material available in Japanese in English, so that English speakers may also typeset Japanese documents (for whatever reason).

* “IPA fontをLaTeXで使う”. (Japanese.)
<http://hisashim.org/2009/11/30/ipafont-latex.html>

* “pLaTeX のフォント設定”. (Japanese.)
<http://d.hatena.ne.jp/vividcode/20091207/1260211166>

* “IPA フォントに関して”. (Japanese.)
<http://www.fugenji.org/~thomas/texlive-guide/ipa_font.html>

* “LaTeX—Atwiki”. (Japanese.)
<http://www10.atwiki.jp/shirayuu/pages/26.html>

* “ptetex3 のフォントの集中管理”. (Japanese.)
<http://tutimura.ath.cx/ptetex/?%A5%D5%A5%A9%A5%F3%A5%C8%A4%CE%BD%B8%C3%E6%B4%C9%CD%FD>

## License

This document is licensed under the CC0 1.0 Universal license.  That is,
“You can copy, modify, distribute and perform the work, even for
commercial purposes, all without asking permission.” See [the license
page](https://creativecommons.org/publicdomain/zero/1.0/) for more
information.
