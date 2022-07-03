<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet
  exclude-result-prefixes="atom xhtml"
  version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:atom="http://www.w3.org/2005/Atom"
>
  <xsl:output method="html" version="1.0" encoding="UTF-8" indent="yes"/>
  <xsl:variable name="godecoding">go_decoding();</xsl:variable>
  <xsl:variable name="title" select="/atom:feed/atom:title"/>

  <xsl:template match="/">
    <html>
      <head>
        <title><xsl:value-of select="atom:feed/atom:title"/> Feed</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1"/>
        <xsl:element name="script">
          <xsl:attribute name="type">text/javascript</xsl:attribute>
          <xsl:attribute name="src">https://issarice.com/bf30.js</xsl:attribute>
        </xsl:element>
        <style type="text/css">
          body {
            margin: auto;
            max-width: 41rem;
            text-align: left;
            word-wrap: break-word;
          }
          div.entry-box {
            border: 1px solid black;
            margin-bottom: 25px;
            padding-left: 10px;
            padding-right: 10px;
          }
          img {
              max-width: 100%;
              height: auto;
          }
        </style>
      </head>
      <body id="browserfriendly" onload="go_decoding()">
       <div id="cometestme" style="display:none;">
         <xsl:text disable-output-escaping="yes" >&amp;amp;</xsl:text>
       </div>
        <h1>Atom feed for issarice.com</h1>
        <p>This file is mainly meant to be used by an RSS feed reader/aggregator. Just use the URL of this page, <code>https://issarice.com/atom.xml</code>, for the subscription URL.</p>
        <p>This Atom feed is updated whenever the “substantive revision date” on a page is updated, which happens whenever I believe that a page has had enough changes to qualify as a new version. If you would like to see more incremental changes, check out the <a href="https://github.com/riceissa/riceissa.com/commits/master.atom">Atom feed for this website’s GitHub repository</a>. For more information about my activity feeds, check out the <a href="https://issarice.com/feed">feed</a> page on my website.</p>
        <xsl:apply-templates select="atom:feed/atom:entry"/>
      </body>
    </html>
  </xsl:template>

  <xsl:template match="atom:entry">
    <div class="entry-box">
      <h2><a href="{atom:link/@href}"><xsl:value-of select="atom:title"/></a></h2>
      <div name="decodeable">
        <xsl:value-of select="atom:content" disable-output-escaping="yes"/>
      </div>
    </div>
  </xsl:template>
</xsl:stylesheet>
