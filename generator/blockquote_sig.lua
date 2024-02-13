-- Return the nth utf8 codepoint.
-- I have no idea why, but Lua's utf8 library does not allow you to just
-- index into the string and grab the nth utf8 character. Instead, all you get
-- is a way to loop over the utf8 characters in the string. So we are
-- implementing a way to index into the string.
function nth_codepoint(n, str)
    local i = 1
    for _, c in utf8.codes(str) do
        if i == n then
            return c
        end
        i = i + 1
    end
    error("string is too short and does not have an nth codepoint")
end

-- Basically Python's str[start_idx:end_idx], except per Lua convention, the
-- first index is 1 and end_idx is inclusive, so utf8_slice(str, 1, #str) grabs
-- the whole string.
function utf8_slice(str, start_idx, end_idx)
    local result = ""
    local i = 1
    for _, c in utf8.codes(str) do
        if i > end_idx then
            break
        end
        if i >= start_idx then
            result = result .. utf8.char(c)
        end
        i = i + 1
    end
    return result
end

function BlockQuote(elem)
    local xs = elem.content
    local last_block = xs[#xs]
    if last_block.t == "Para" and last_block.content[1].t == "Str" then
        local str_text = last_block.content[1].text
        if nth_codepoint(1, str_text) == 8212 then
            -- This replaces the pure m-dash with an m-dash followed by a hair
            -- space, which, according to the Wikipedia manual of style, is the
            -- correct way to display an attribution for a blockquote
            -- https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style#Other_uses_(em_dash_only)
            local str = pandoc.Str(utf8.char(8212) .. utf8.char(8202) .. utf8_slice(str_text, 2, #str_text))
            last_block.content[1] = str
            -- We wrap up the last block inside a special div, and then replace
            -- the original last block with our new div block
            xs[#xs] = pandoc.Div(last_block, {class = 'blockquote-source'})
            -- Return the new modified BlockQuote element
            return elem
        end
        -- Otherwise, this blockquote did not contain a final line beginning with
        -- an m-dash, so it's not an attribution-style quote, so just return the
        -- original blockquote.
        return elem
    end
end
