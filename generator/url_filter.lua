-- License: CC0
-- A URL filter to allow wikilinks, for use with Pandoc.
-- See http://pandoc.org/lua-filters.html for more information about Lua
-- Filters.

pandoc.utils = require 'pandoc.utils'

-- For debugging. From https://stackoverflow.com/a/27028488/3422337
function dump(o)
   if type(o) == 'table' then
      local s = '{ '
      for k,v in pairs(o) do
         if type(k) ~= 'number' then k = '"'..tostring(k)..'"' end
         s = s .. '['..tostring(k)..'] = ' .. dump(v) .. ','
      end
      return s .. '} '
   else
      return tostring(o)
   end
end

-- Use `pandoc -f markdown -t native test.md` to get the document structure
-- Here the "k" values are just numbers 1, 2, 3, and so on.
-- Using "-t json" rather than "-t native" also works.


-- Slugify the string x. Unicode support isn't too good at the moment and must
-- be hard-coded into the map.
function slug(x)
  local x = x:lower()
  local blacklist = "- !@#$%^&*()_=+,<>.?/'\"[]{}\\|`~:;‘’“”§"
  local ret = ""
  -- Loop over utf-8 characters rather than bytes; see
  -- https://stackoverflow.com/a/13238257/3422337
  for _, c in utf8.codes(x) do
    if not blacklist:find(utf8.char(c)) then
      ret = ret .. utf8.char(c)
    elseif not(#ret == 0 or string.sub(ret, -1) == "-") then
      ret = ret .. "-"
    end
  end
  if string.sub(ret, -1) == "-" then
    return string.sub(ret, 1, #ret - 1)
  else
    return ret
  end
end

function Link(elem)
  local target = elem.target
  if elem.target == "!w" then
    target = "https://en.wikipedia.org/wiki/" ..
      pandoc.utils.stringify(elem.content):gsub(" ", "_")
  elseif elem.target:find("^!w%%20") then
    target = "https://en.wikipedia.org/wiki/" ..
      string.sub(elem.target:gsub("%%20", "_"), 1 + #"!w_")
  elseif elem.target:find("^!wja%%") then
    target = "https://ja.wikipedia.org/wiki/" ..
      string.sub(elem.target:gsub("%%20", "_"), 1 + #"!wja_")
  elseif elem.target:find("^!") then
    target = "http://duckduckgo.com/?q=" .. elem.target .. "+" ..
      pandoc.utils.stringify(elem.content):gsub(" ", "+")
  elseif elem.target == "" then
    target = slug(pandoc.utils.stringify(elem.content))
  elseif elem.title == "wikilink" then
    target = slug(pandoc.utils.stringify(elem.target))
  end
  return pandoc.Link(elem.content, target, elem.title, elem.attr)
end
