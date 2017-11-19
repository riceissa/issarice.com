-- License: CC0
-- A simple Pandoc Lua filter to extract the links in a file.
-- To get all the links for my site, run:
--     rm -f links.txt && for filename in wiki/*; do pandoc -f markdown+smart -t html5 --mathjax $filename --lua-filter generator/url_filter.lua --lua-filter generator/list_links.lua -o temp >> links.txt; done && rm -f temp
-- You can then sort/make links unique as fit.

function Link(elem)
  io.stdout:write(elem.target .. "\n")
end
