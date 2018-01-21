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
  map = {["ó"] = "ó"}
  local x = x:lower()
  local ret = ""
  -- Loop over utf-8 characters rather than bytes; see
  -- https://stackoverflow.com/a/13238257/3422337
  for c in x:gmatch("[%z\1-\127\194-\244][\128-\191]*") do
    if c:match("%w") then
      ret = ret .. c
    elseif map[c] ~= nil then
      ret = ret .. map[c]
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
  end
  return pandoc.Link(elem.content, target, elem.title, elem.attr)
end
