--------------------------------------------------------------------------------
{-# LANGUAGE OverloadedStrings #-}
import           Data.Monoid (mappend, mconcat, (<>))
import           Hakyll
import Prelude hiding (id)
import           System.FilePath
import           Text.Pandoc.Options


--------------------------------------------------------------------------------
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
            {->>= loadAndApplyTemplate "templates/default.html" defaultContext-}
            {->>= relativizeUrls-}

    -- See http://vapaus.org/text/hakyll-configuration.html#fnref1 .
    --let pandocOptions = defaultHakyllWriterOptions { writerHTMLMathMethod = MathJax "" }
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
    let pandocOptions = defaultHakyllWriterOptions
             { writerTableOfContents = True
               , writerTOCDepth = 3
               , writerStandalone = True
               , writerTemplate = "$toc$\n$body$"
             }

    -- build tags
    tags <- buildTags "pages/*" (fromCapture "tags/*")

    match "pages/*" $ do
        -- Below, route is adapted from
        -- http://ethanschoonover.com/source/bin/site.hs see the
        -- function stripTopDir there. Essentially, we want the files in
        -- pages to *not* clutter up our git repository's root
        -- directory, but at the same time, when we're serving the
        -- compiled files, we want them in the root directory of the
        -- domain. Therefore, we first (from right to left) get the file
        -- page, break it up into lists split by directories, remove the
        -- first directory (the "page" directory) with tail, join it
        -- back together, then drop the .html extension in favor of Cool
        -- URIs.
        route $ customRoute $ dropExtension . joinPath . tail . splitPath . toFilePath
        -- route $ setExtension ""
        compile $ pandocCompilerWith defaultHakyllReaderOptions pandocOptions
            >>= loadAndApplyTemplate "templates/tags.html" (pageCtx tags)
            >>= loadAndApplyTemplate "templates/default.html" defaultContext
            >>= relativizeUrls

    tagsRules tags $ \tag pattern -> do
        let title = "Tag: " ++ tag
        route idRoute

        {-compile $ pageOfPages tags title pattern-}
        compile $ do
            pages <- loadAll pattern
            let ctx = constField "title" title <>
                        listField "pages" (pageCtx tags) (return pages) <>
                        defaultContext
            makeItem ""
                >>= loadAndApplyTemplate "templates/page-list.html" ctx
                >>= loadAndApplyTemplate "templates/default.html" ctx
                >>= relativizeUrls

    {-match "posts/*" $ do-}
        {-route $ setExtension "html"-}
        {-compile $ pandocCompiler-}
            {->>= loadAndApplyTemplate "templates/post.html"    postCtx-}
            {->>= loadAndApplyTemplate "templates/default.html" postCtx-}
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
                >>= loadAndApplyTemplate "templates/default.html" archiveCtx
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
                {->>= loadAndApplyTemplate "templates/default.html" indexCtx-}
                {->>= relativizeUrls-}

    match "templates/*" $ compile templateCompiler


--------------------------------------------------------------------------------
postCtx :: Context String
postCtx =
    dateField "date" "%B %e, %Y" `mappend`
    defaultContext

pageCtx :: Tags -> Context String
pageCtx tags = mconcat
    [tagsField "tags" tags
    , defaultContext
    ]

-- See postList on https://github.com/brianshourd/brianshourd.com/blob/master/hakyll.hs .
{-pageList :: Tags -> Pattern -> ([Item String] -> Compiler [Item String]) -> Compiler String-}
{-pageList tags = do-}
    {-postItemTpl <- loadBody "templates/default.html"-}
    {-posts <- loadAll-}
    {-applyTemplateList postItemTpl (pageCtx tags) posts-}

-- Make a page from a list of pages. See postPage on  https://github.com/brianshourd/brianshourd.com/blob/master/hakyll.hs .
{-pageOfPages :: Tags -> String -> Pattern -> Compiler (Item String)-}
{-pageOfPages tags title = do-}
    {-list <- pageList tags-}
    {-makeItem ""-}
        {->>= loadAndApplyTemplate ""-}
                {-(constField "posts" list <> constField "title" title <>-}
                    {-defaultContext)-}
        {->>= finish (titleCtx title)-}

{-titleCtx :: String -> Context String-}
{-titleCtx title = constField "siteTitle" title-}

{-finish :: Context String -> Item String -> Compiler (Item String)-}
{-finish context item = loadAndApplyTemplate-}
        {-"templates/default.html" (context <> defaultContext) item-}
    {->>= relativizeUrls-}
