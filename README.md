# riceissa.com

This repository hosts the files needed to compile my website, <http://riceissa.com>.
The website is compiled using the static site generator [Hakyll](http://jaspervdj.be/hakyll/).
Assuming one has the prerequisites to compile the site, just do:

~~~~bash
git clone https://github.com/riceissa/riceissa.com.git
cd riceissa.com
ghc --make site.hs
./site rebuild
~~~~

This will generate a folder, `_site`, which will contain all the files that are eventually served on the site.
Note that in the interest of [Cool URIs](http://www.w3.org/TR/cooluris/), the compiled files have no file extensions (which would usually be `.html`).
Therefore simply opening the files in your browser may not work as expected.
