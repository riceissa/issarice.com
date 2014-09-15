---
layout: default
title: Setting up Jekyll on GitHub
comments: "yes"
disqus-id: 9dfd2e7767fc36827692b6a194433f1d96fe58d4
math: "yes"
last-major-revision-date: 2014-04-15
license: "CC-BY"
tags: computing
---


There are already well-written guides for setting up Jekyll on GitHub Pages, and it would be pointless for me to add another.
This page is here mostly as a quick reference for myself.
See the references at the bottom for actual tutorials.

I think Jekyll is designed to run automatically on GitHub, as long as you are in your website repository (<code>USERNAME.github.io</code>) or in the <code>gh-pages</code> branch in any other repository.

The most important file is called <code>\_config.yml</code>, and must be placed in the main directory.
If one is using GitHub pages on one’s website repository, it should look like:

```
markdown: redcarpet
baseurl: ""
exclude: ['README.md']
```

For any other repository, the <code>baseurl</code> must be modified:

    markdown: redcarpet
    baseurl: /REPONAME
    exclude: ['README.md']

This website itself is created using Jekyll and is hosted on GitHub, so looking at the [source](https://github.com/riceissa/riceissa.github.io) may be useful.

To generate the Jekyll site locally run:

``` bash
jekyll serve --watch --baseurl ""
```

## Typesetting math

See <http://cwoebker.com/posts/latex-math-magic>, <http://doswa.com/2011/07/20/mathjax-in-markdown.html>, and <http://rangerway.com/way/2013/10/05/latex-note-and-jekyll/> for more (they should be identical).

See [this page](http://stackoverflow.com/a/11093303/3422337) for the “big picture”.
The idea is that we want the Markdown processor to leave potential LaTeX code untouched so that MathJax can access it.

See [here](/math/math-test.html) for an extensive list of what works and what doesn’t.

<h3 id="examples">Examples</h3>

Enter

{% highlight tex %}
`\(\int_a^b f(x) \, dx\)`
{% endhighlight %}

to obtain `\(\int_a^b f(x) \, dx\)`.

Enter

{% highlight tex %}
`\[\begin{aligned}
\nabla \times \vec{\mathbf{B}} -\, \frac1c\, \frac{\partial\vec{\mathbf{E}}}{\partial t}
& = \frac{4\pi}{c}\vec{\mathbf{j}} \\
\nabla \cdot \vec{\mathbf{E}}
& = 4 \pi \rho \\
\nabla \times \vec{\mathbf{E}}\, +
\, \frac1c\, \frac{\partial\vec{\mathbf{B}}}{\partial t}
& = \vec{\mathbf{0}} \\
\nabla \cdot \vec{\mathbf{B}} & = 0 \end{aligned}\]`
{% endhighlight %}

to obtain

`\[\begin{aligned}
\nabla \times \vec{\mathbf{B}} -\, \frac1c\, \frac{\partial\vec{\mathbf{E}}}{\partial t}
& = \frac{4\pi}{c}\vec{\mathbf{j}} \\
\nabla \cdot \vec{\mathbf{E}}
& = 4 \pi \rho \\
\nabla \times \vec{\mathbf{E}}\, +
\, \frac1c\, \frac{\partial\vec{\mathbf{B}}}{\partial t}
& = \vec{\mathbf{0}} \\
\nabla \cdot \vec{\mathbf{B}} & = 0 \end{aligned}\]`

(modified from Maxwell’s Equations as given [here](http://www.mathjax.org/demos/tex-samples/))

## References

- See [Thomas Bradley’s guide](https://github.com/algonquindesign/jekyll) (there are also video tutorials, which can be accessed from that page).

- See also [my own Quora post about static page generation](https://www.quora.com/Issa-Rice/Data-Archiving/Static-page-generation).
