--------------------------------------------------------------------------------
{-# LANGUAGE OverloadedStrings #-}
import           Data.Monoid (mappend)
import           Hakyll
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
    {-tags <- buildTags "pages/*" (fromCapture "tags/*")-}

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
            >>= loadAndApplyTemplate "templates/default.html" defaultContext
            >>= relativizeUrls

    {-match "posts/*" $ do-}
        {-route $ setExtension "html"-}
        {-compile $ pandocCompiler-}
            {->>= loadAndApplyTemplate "templates/post.html"    postCtx-}
            {->>= loadAndApplyTemplate "templates/default.html" postCtx-}
            {->>= relativizeUrls-}

    create ["archive.html"] $ do
        route idRoute
        compile $ do
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

