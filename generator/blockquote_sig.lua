function BlockQuote(elem)
    local xs = elem.content
    local last_block = xs[#xs]
    -- I have no idea why, but Lua's utf8 library does not allow you to just
    -- index into the string and grab the first utf8 character. Instead, you
    -- need to loop over it.
    for _, c in utf8.codes(pandoc.utils.stringify(last_block)) do
        -- Check for m-dash
        if c == 8212 then
            -- We wrap up the last block inside a special div, and then replace
            -- the original last block with our new div block
            xs[#xs] = pandoc.Div(last_block, {class = 'source'})
            -- Return the new modified BlockQuote element
            return elem
        end
        break
    end
    -- Otherwise, this blockquote did not contain a final line beginning with
    -- "---", so it's not an attribution-style quote, so just return the
    -- original blockquote.
    return elem
end
