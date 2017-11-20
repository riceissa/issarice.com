-- License: CC0
-- A simple Pandoc Lua filter to extract the links in a file.

function Link(elem)
  if elem.target:find("^https?://") then
    io.stdout:write(elem.target .. "\n")
  elseif elem.target:find("^mailto:") then
    -- Do nothing
  else
    -- Internal link
    io.stdout:write("https://issarice.com/" .. elem.target .. "\n")
  end
end
