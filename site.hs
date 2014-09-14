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

    --let pandocOptions = defaultHakyllWriterOptions { writerHTMLMathMethod = MathJax "" }
    let pandocOptions = defaultHakyllWriterOptions
             { writerTableOfContents = True
               , writerTOCDepth = 3
               , writerStandalone = True
               , writerTemplate = "$toc$\n$body$"
             }

    match "pages/*" $ do
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

    {-create ["archive.html"] $ do-}
        {-route idRoute-}
        {-compile $ do-}
            {-posts <- recentFirst =<< loadAll "posts/*"-}
            {-let archiveCtx =-}
                    {-listField "posts" postCtx (return posts) `mappend`-}
                    {-constField "title" "Archives"            `mappend`-}
                    {-defaultContext-}

            {-makeItem ""-}
                {->>= loadAndApplyTemplate "templates/archive.html" archiveCtx-}
                {->>= loadAndApplyTemplate "templates/default.html" archiveCtx-}
                {->>= relativizeUrls-}


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
