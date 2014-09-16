---
title: Configuration file for this site
license: CC BY
...

Below is the configuration file used to generate this site using Hakyll.
The source is written in literate Haskell, and is stored in `site.hs`.

Import prerequisites:

\begin{code}
{-# LANGUAGE OverloadedStrings #-}
import          Data.Monoid (mappend, mconcat, (<>))
import          Data.Map as M
import          Data.Char
import          Hakyll
import          Prelude hiding (id)
import          System.FilePath
import          Text.Pandoc.Options
import          Text.Pandoc (WriterOptions)
\end{code}

Main:

\begin{code}
main :: IO ()
main = hakyll $ do
    {-match "images/*" $ do-}
        {-route   idRoute-}
        {-compile copyFileCompiler-}

    match "css/*" $ do
        route   idRoute
        compile compressCssCompiler

    {-match (fromList ["about.rst", "contact.markdown"]) $ do-}
        {-route   $ setExtension ""-}
        {-compile $ pandocCompiler-}
            {->>= loadAndApplyTemplate "templates/skeleton.html" defaultContext-}
            {->>= relativizeUrls-}

    -- See http://vapaus.org/text/hakyll-configuration.html#fnref1 .
    --
    -- See all the options for defaultHakyllWriterOptions here:
    -- https://gist.github.com/shirataki/9538344 . To do all this, we
    -- need to import Text.Pandoc.Options:
    -- https://groups.google.com/forum/#!msg/hakyll/Fob_YFFh7kU/2uF3_Ihk3WoJ
    -- .  As for how to actually produce a ToC, there is discussion
    -- here:
    -- https://groups.google.com/forum/#!msg/hakyll/FFTGC4TsXo8/mueGzxg5o-kJ
    -- , which points to
    -- https://github.com/jaspervdj/hakyll/blob/master/web/site.hs ;
    -- there, look at how withToc is used as a writer passed to
    -- pandocCompilerWith, and how withToc contains the options listed
    -- below. I'm not exactly sure if all three are necessary, but just
    -- setting writerTableOfContents to True did *not* work.

    -- build tags
    tags <- buildTags "pages/*" (fromCapture "tags/*")

    let myHakyllReaderOptions = defaultHakyllReaderOptions -- {
                -- readerSmart = False
                -- }

    -- let lhsWriter = defaultWriterOptions { writerLiterateHaskell = True }
    let lhsWriter = defaultHakyllWriterOptions

    match "site.lhs" $ do
        route $ setExtension ""
        compile $ pandocCompilerWith myHakyllReaderOptions lhsWriter
            {->>= loadAndApplyTemplate "templates/tags.html" (pageCtx tags)-}
            >>= loadAndApplyTemplate "templates/skeleton.html" (licenseCtx `mappend` mathCtx `mappend` (pageCtx tags) `mappend` defaultContext)
            >>= relativizeUrls


    let pandocOptions = defaultHakyllWriterOptions
             { writerTableOfContents = True
               , writerTOCDepth = 3
               , writerStandalone = True
               , writerTemplate = "$toc$\n$body$"
               , writerHTMLMathMethod = MathJax ""
             }
\end{code}

\begin{code}

    match "pages/*" $ do
        route $ coolPageRoute
        -- route $ setExtension ""
        compile $ pandocCompilerWith myHakyllReaderOptions pandocOptions
            {->>= loadAndApplyTemplate "templates/tags.html" (pageCtx tags)-}
            >>= loadAndApplyTemplate "templates/skeleton.html" (licenseCtx `mappend` mathCtx `mappend` (pageCtx tags) `mappend` defaultContext)
            >>= relativizeUrls
\end{code}


The following is what actually makes the separate pages for each tag that go under `/tag/*`.

\begin{code}
    tagsRules tags $ \tag pattern -> do
        let title = "Tag: " ++ tag
        route idRoute
        compile $ do
            pages <- loadAll pattern
            let ctx = constField "title" title <>
                        listField "pages" (pageCtx tags) (return pages) <>
                        defaultContext
            makeItem ""
                >>= loadAndApplyTemplate "templates/page-list.html" ctx
                >>= loadAndApplyTemplate "templates/skeleton.html" (ctx)
                >>= relativizeUrls
\end{code}


\begin{code}
    {-match "posts/*" $ do-}
        {-route $ setExtension "html"-}
        {-compile $ pandocCompiler-}
            {->>= loadAndApplyTemplate "templates/post.html"    postCtx-}
            {->>= loadAndApplyTemplate "templates/skeleton.html" postCtx-}
            {->>= relativizeUrls-}

    -- automatically generate a page containing links to all other pages
    create ["all"] $ do
        route idRoute
        compile $ do
            {-let alphabetize = sortByM $ itemIdentifier-}
                                {-where-}
                                    {-sortByM f xs = liftM (map fst . sortBy (comparing snd)) $-}
                                                    {-mapM (\x -> liftM (x,) (f x)) xs-}
            {-pages <- alphabetize =<< loadAll "pages/*"-}
            pages <- loadAll "pages/*"
            let archiveCtx =
                    listField "pages" defaultContext (return pages) `mappend`
                    constField "title" "All pages" `mappend`
                    defaultContext
            makeItem ""
                >>= loadAndApplyTemplate "templates/page-list.html" archiveCtx
                >>= loadAndApplyTemplate "templates/skeleton.html" (archiveCtx)
                >>= relativizeUrls


    {-match "index.html" $ do-}
        {-route idRoute-}
        {-compile $ do-}
            {-posts <- recentFirst =<< loadAll "posts/*"-}
            {-let indexCtx =-}
                    {-listField "posts" postCtx (return posts) `mappend`-}
                    {-constField "title" "Home"                `mappend`-}
                    {-defaultContext-}

            {-getResourceBody-}
                {->>= applyAsTemplate indexCtx-}
                {->>= loadAndApplyTemplate "templates/skeleton.html" indexCtx-}
                {->>= relativizeUrls-}

    match "templates/*" $ compile templateCompiler


--------------------------------------------------------------------------------
postCtx :: Context String
postCtx =
    dateField "date" "%B %e, %Y" `mappend`
    defaultContext
\end{code}

Seriously, the stuff below is *really* messed up at the moment.

\begin{code}
-- See my StackOverflow question http://stackoverflow.com/questions/25845956/hakyll-how-can-one-delete-a-field-completely-after-checking-for-its-existence
-- tagCtx :: Tags -> Context String
-- tagCtx tags = field "tags" $ \item -> do
--     metadata <- getMetadata $ itemIdentifier item
--     return $ if "tags" `M.member` metadata
--                 then "bingo!"
--                 else ""

checkTags thing = constField "hello" "hello"

{-eliminate :: Context String -> String-}
{-eliminate (Context a) = a-}

{-checkTags :: Context String -> Context String-}
{-checkTags thing = do-}
        {-if eliminate thing == ""-}
            {-then constField "hello" "hello"-}
            {-else thing-}

pageCtx :: Tags -> Context String
pageCtx tags = tagsField "tags" tags <> defaultContext

{-\item -> do-}
    {-let metadata = getMetadata $ itemIdentifier item-}
    {-if "tags" `M.member` metadata-}
        {-then tagsField "tags" tags <> defaultContext-}
        {-else field "tags" $ return ""-}

-- pageCtx tags = field "tags" $ \item -> do
--                 metadata <- getMetadata $ itemIdentifier item
--                 if "tags" `M.member` metadata
--                 then
--                     return (tagsField "tags" tags) <> defaultContext
--                 else (return "untagged")

-- from http://qnikst.github.io/posts/2013-02-04-hakyll-latex.html
mathCtx :: Context a
mathCtx = field "math" $ \item -> do
    metadata <- getMetadata $ itemIdentifier item
    return $ if "math" `M.member` metadata
                then "<script type=\"text/javascript\" src=\"https://c328740.ssl.cf1.rackcdn.com/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML\"></script>"
                else ""
\end{code}

We create the `license` field below, which will automatically generate the correct license (currently at the bottom) on each page based on the value given to the YAML keyword `license`.
See "[Adding license notes to blog pages](http://qnikst.github.io/posts/2013-08-23-licenses-notes-in-hakyll.html)", from which this is adapted.

\begin{code}
licenseCtx :: Context a
licenseCtx = field "license" $ \item -> do
    {-f <- loadBody "templates/CC-BY.html"-}
    metadata <- getMetadata $ itemIdentifier item
    return $ case M.lookup "license" metadata of
                Nothing -> ""
                Just m -> case M.lookup (trim m) licenses of
                            Nothing -> "The license of this work is unknown."
                            Just (lTextUrl, lAltText, lImageUrl, lName) -> "<a rel=\"license\" href=\"" ++ lTextUrl ++ "\"><img alt=\"" ++ lAltText ++ "\" style=\"border-width:0\" src=\"" ++ lImageUrl ++ "\"/></a><br />" ++ "This page is <a rel=\"license\" href=\"" ++ lTextUrl ++ "\">" ++ lName ++ "</a>."
                            -- Just (lTextUrl, lAltText, lImageUrl, lName) -> "there is license."
    where
        trim = reverse . dropWhile isSpace . reverse . dropWhile isSpace

licenses = M.fromList
    [ ("CC0", ("https://creativecommons.org/publicdomain/zero/1.0/", "CC0", "https://i.creativecommons.org/p/zero/1.0/88x31.png", "Public Domain (Creative Commons CC0)"))
    , ("CC BY", ("https://creativecommons.org/licenses/by/4.0/", "Creative Commons License", "https://i.creativecommons.org/l/by/4.0/88x31.png", "licensed under a Creative Commons Attribution 4.0 International License"))]
\end{code}

We now implement a custom route.
This is adapted from <http://ethanschoonover.com/source/bin/site.hs>; see the function `stripTopDir` there.
Essentially, we want the files in pages to *not* clutter up our Git repository's root directory, but at the same time, when we're serving the compiled files, we want them in the root directory of the domain.
Therefore, we first (from right to left) get the file page, break it up into lists split by directories, remove the first directory (the "page" directory) with tail, join it back together, then drop the `.html` extension in favor of Cool URIs.

\begin{code}
coolPageRoute :: Routes
coolPageRoute = customRoute $ dropExtension . joinPath . tail . splitPath . toFilePath
\end{code}
