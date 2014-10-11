-- This is the Hakyll configuration file used to generate this site.
-- It is stored in `site.hs`, and can be compiled with `ghc --make site.hs`.

-- Import prerequisites
{-# LANGUAGE OverloadedStrings #-}
import Data.Monoid (mappend, mconcat, (<>))
import Data.Map as M
import Data.Char
import Hakyll
import Prelude hiding (id)
import System.FilePath
import Text.Pandoc.Options
import Text.Pandoc (WriterOptions)

-- Main
main :: IO ()
main = hakyll $ do

    -- Make this file available under "/site.hs".
    match "site.hs" $ do
        route idRoute
        compile copyFileCompiler

    match "css/*" $ do
        route idRoute
        compile compressCssCompiler

    match "images/favicon.ico" $ do
        route $ customRoute $ dropOneParentDir
        compile copyFileCompiler

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

    -- Build tags
    tags <- buildTags "pages/*" (fromCapture "tags/*")

    let myHakyllReaderOptions = defaultHakyllReaderOptions
    let myHakyllWriterOptions = defaultHakyllWriterOptions
             {   writerTableOfContents = True
               , writerTOCDepth = 3
               , writerStandalone = True
               , writerTemplate = "$toc$\n$body$"
               , writerHTMLMathMethod = MathJax ""
             }

    match "pages/*" $ do
        route $ coolPageRoute
        compile $ pandocCompilerWith myHakyllReaderOptions myHakyllWriterOptions
            >>= loadAndApplyTemplate "templates/skeleton.html" (licenseCtx <>
                    mathCtx <>
                    (pageCtx tags) <>
                    defaultContext)
            >>= relativizeUrls

    -- The following is what actually makes the separate pages for each
    -- tag that go under `/tag/*`.
    tagsRules tags $ \tag pattern -> do
        let title = "Tag: " ++ tag
        route idRoute
        compile $ tagPage tags title pattern

    -- Automatically generate a page containing links to all other
    -- pages. See
    -- <http://jaspervdj.be/hakyll/tutorials/04-compilers.html>. TODO:
    -- figure out how to alphabetically sort this list by title (in
    -- metadata), not by the filename.  The Hakyll docs seem to only
    -- show how to sort this by date.
    create ["all"] $ do
        route idRoute
        compile $ do
            pages <- loadAll "pages/*"
            let archiveCtx =
                    listField "pages" defaultContext (return pages) <>
                    constField "title" "All pages" <>
                    defaultContext
            makeItem ""
                >>= loadAndApplyTemplate "templates/page-list.html" archiveCtx
                >>= loadAndApplyTemplate "templates/skeleton.html" (archiveCtx)
                >>= relativizeUrls

    match "templates/*" $ compile templateCompiler

--------------------------------------------------------------------------------
-- Seriously, the stuff below is *really* messed up at the moment.

-- See my StackOverflow question http://stackoverflow.com/questions/25845956/hakyll-how-can-one-delete-a-field-completely-after-checking-for-its-existence
-- tagCtx :: Tags -> Context String
-- tagCtx tags = field "tags" $ \item -> do
--     metadata <- getMetadata $ itemIdentifier item
--     return $ if "tags" `M.member` metadata
--                 then "bingo!"
--                 else ""

pageCtx :: Tags -> Context String
pageCtx tags = tagsField "tags" tags <> defaultContext

{-\item -> do-}
    {-let metadata = getMetadata $ itemIdentifier item-}
    {-if "tags" `M.member` metadata-}
        {-then tagsField "tags" tags <> defaultContext-}
        {-else field "tags" $ return ""-}

-- From <http://qnikst.github.io/posts/2013-02-04-hakyll-latex.html>.
mathCtx :: Context a
mathCtx = field "math" $ \item -> do
    metadata <- getMetadata $ itemIdentifier item
    return $ if "math" `M.member` metadata
                then "<script type=\"text/javascript\" src=\"https://c328740.ssl.cf1.rackcdn.com/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML\"></script>"
                else ""

-- We create the `license` field below, which will automatically
-- generate the correct license (currently at the bottom) on each page
-- based on the value given to the YAML keyword `license`.  See "[Adding
-- license notes to blog
-- pages](http://qnikst.github.io/posts/2013-08-23-licenses-notes-in-hakyll.html)",
-- from which this is adapted.
licenseCtx :: Context a
licenseCtx = field "license" $ \item -> do
    {-f <- loadBody "templates/CC-BY.html"-}
    metadata <- getMetadata $ itemIdentifier item
    return $ case M.lookup "license" metadata of
                Nothing -> ""
                Just m -> case M.lookup (trim m) licenses of
                            Nothing -> "The license of this page is unknown."
                            Just (lTextUrl, lAltText, lImageUrl, lName) -> "<a rel=\"license\" href=\"" ++ lTextUrl ++ "\"><img alt=\"" ++ lAltText ++ "\" style=\"border-width:0\" src=\"" ++ lImageUrl ++ "\"/></a><br />" ++ "This page is <a rel=\"license\" href=\"" ++ lTextUrl ++ "\">" ++ lName ++ "</a>."
    where
        trim = reverse . dropWhile isSpace . reverse . dropWhile isSpace

licenses = M.fromList
    [ ("CC0", ("https://creativecommons.org/publicdomain/zero/1.0/", "CC0", "https://i.creativecommons.org/p/zero/1.0/88x31.png", "released to the public domain according to Creative Commons CC0"))
    , ("CC BY", ("https://creativecommons.org/licenses/by/4.0/", "Creative Commons License", "https://i.creativecommons.org/l/by/4.0/88x31.png", "licensed under a Creative Commons Attribution 4.0 International License"))]

-- We now implement a custom route.  This is adapted from
-- <http://ethanschoonover.com/source/bin/site.hs>; see the function
-- `stripTopDir` there.  Essentially, we want the files in pages to
-- *not* clutter up our Git repository's root directory, but at the same
-- time, when we're serving the compiled files, we want them in the root
-- directory of the domain.  Therefore, we first (from right to left)
-- get the file page, break it up into lists split by directories,
-- remove the first directory (the "page" directory) with tail, join it
-- back together, then drop the `.html` extension in favor of Cool URIs.
coolPageRoute :: Routes
coolPageRoute = customRoute $ dropExtension . dropOneParentDir

dropOneParentDir = joinPath . tail . splitPath . toFilePath

-- See <https://github.com/jaspervdj/jaspervdj/blob/master/src/Main.hs>, <http://www.gwern.net/hakyll.hs>, and <https://github.com/brianshourd/brianshourd.com/blob/master/hakyll.hs>.
tagPage tags title pattern = do
    pages <- loadAll pattern
    let ctx = constField "title" title <>
                listField "pages" (pageCtx tags) (return pages) <>
                defaultContext
    makeItem ""
        >>= loadAndApplyTemplate "templates/page-list.html" ctx
        >>= loadAndApplyTemplate "templates/skeleton.html" (ctx)
        >>= relativizeUrls
