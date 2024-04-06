function Link(elem)
    if elem.title == "wikilink" then
        io.write(elem.target .. "\n")
    end
end
