---
title: Tabular presentation
author: Issa Rice
created: 2016-07-01
date: 2017-02-25
---

Some thoughts on how best to represent information on tables.

# Styling

- use grid lines or not?
- color alternation? -- cf. [this question about zebra stripes](http://tex.stackexchange.com/questions/33758/professional-looking-tables-with-alternating-row-colors) on TeX Stack Exchange and [To use or not to use "Zebra Stripes", or Alternating Row Colors for Tables](http://ux.stackexchange.com/questions/3562/to-use-or-not-to-use-zebra-stripes-or-alternating-row-colors-for-tables) (seems to cite some research on lookups) and [Is there a better way than zebra stripes](http://ux.stackexchange.com/questions/60715/is-there-a-better-way-than-zebra-stripes) (cites research on lookups and preference)
- use lots of examples.
- markup syntax for tables: pandoc has many, but they're all unintuitive for me because they optimize for appearance in the markup, not the ease of entering in the data or how memorable the syntax is.
(In fact, I keep having to go to the Pandoc documentation to read up on how to make a table.)
Compare this to the Mediawiki markup, which is quite easy to remember, even though in the source markup it doesn't look like a table.

From [Publication quality tables in LaTeX](http://texdoc.net/texmf-dist/doc/latex/booktabs/booktabs.pdf):

> You will not go far wrong if you remember two simple guidelines at all times:
>
> 1. Never, ever use vertical rules.
> 2. Never use double rules.
>
> These guidelines may seem extreme but I have never found a good argument in
> favour of breaking them. For example, if you feel that the information in the
> left half of a table is so different from that on the right that it needs to
> be separated by a vertical line, then you should use two tables instead. Not
> everyone follows the second guideline: I have worked for a publisher who
> insisted on a double light rule above a row of totals. But this would not
> have been my choice.
>
> There are three further guidelines worth mentioning here as they are
> generally not known outside the circle of professional typesetters and
> subeditors:
>
> 3. Put the units in the column heading (not in the body of the table).
> 4. Always precede a decimal point by a digit; thus 0.1 _not_ just .1.
> 5. Do not use ‘ditto’ signs or any other such convention to repeat a previous
>    value. In many circumstances a blank will serve just as well. If it won’t,
>    then repeat the value.
>
> Whether or not you wish to follow the minor niceties, if you use only the
> following commands in your formal tables your reader will be grateful. I
> stress that the guidelines are not just to keep the pedantic happy. The
> principal is that enforced structure of presentation enforces structured
> thought in the first instance.

[Butterick says](http://practicaltypography.com/tables.html):

> Cell borders are helpful as guides when you’re loading information into the
> table. They’re less useful once the table is full. The text in the cells will
> create an implied grid. Cell borders can make the grid cluttered and
> difficult to read, especially in tables with many small cells.

See also [Small Guide to Making Nice Tables](https://www.inf.ethz.ch/personal/markusp/teaching/guides/guide-tables.pdf).

But what about more complex tables like the [timeline of global health](https://en.wikipedia.org/wiki/Timeline_of_global_health)?
Surely sortability justifies tabulating the information, and having no grid lines would make lookups difficult (both time-consuming and mentally exhausting).

What are we trying to optimize for?

- Aesthetic appearance (how the table looks on the page or from afar)
- Lookup speeds
- Preventing mental exhaustion
- Obeying some principles handed down from "typographic elites"

See also [Beautiful table samples](http://tex.stackexchange.com/questions/112343/beautiful-table-samples) and [Tip on how to make a visually good table](http://tex.stackexchange.com/questions/238503/tip-on-how-to-make-a-visually-good-table).

# Function

Having worked on various timeline pages and tables on the English Wikipedia
(and beyond), I have developed some ideas about how tabular information should
function.

* I like to imagine each table as just the result of one possible SQL query out
  of numerous possible ones that could be pulling information from a database.
* Building off of the previous point, the table should give an *answer* based
  on the reader's *query*.
  But since the table is the result of just a *single* query, it only
  "answers" one thing!
  It seems too easy to assemble ["an indiscriminate collection of
  information"](https://en.wikipedia.org/wiki/Wikipedia:What_Wikipedia_is_not#Wikipedia_is_not_an_indiscriminate_collection_of_information)
  without answering the questions the readers are asking.
* It is useful to have rows that are sortable by each of the columns.
  Working off of the SQL analogy, each sorted state is a different query (you
  can think of it as tacking on different `ORDER BY` clauses to the query), so
  making the table sortable is a way to increase the number of queries readers
  can run -- and thus the number of questions they can answer.

# Examples

Here I list some examples of tabular things I have worked with.

- [My work page](https://issarice.com/work)
- [AI Watch](https://aiwatch.issarice.com/)
- [Timelines Wiki main page table](https://timelines.issarice.com/wiki/Main_Page)
- [Timelines Wiki timeline](https://timelines.issarice.com/wiki/Timeline_of_Machine_Intelligence_Research_Institute) (example timeline)
- [Beliefs site](https://beliefs.issarice.com/belief.php)
- [Donations List website](https://donations.vipulnaik.com/donor.php?donor=Open+Philanthropy+Project)
  (Vipul Naik's creation, but I have helped with some of the development)

# Acknowledgments

A conversation with Vipul Naik inspired the creation of this page (though I had been thinking about tables before the conversation).
