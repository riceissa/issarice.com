---
title: Anki templates
author: Issa Rice
created: 2023-11-21
date: 2023-11-21
---
Here's the main template I use in [[Anki]]. Below, "Notes" is just an extra field I like to use for extra notes (e.g. source of where I got the info in the card, or non-essential things that are still useful to have, or questions I have).

Front:

```
<div id="front">{{#Tags}}{{Tags}}: {{/Tags}}{{Front}}</div>
<script type="text/javascript">
  var fonts = ["Arial", "Helvetica", "Charter", "Georgia", "Times", "Verdana", "Segoe UI"];
  var randomIndex = Math.floor(Math.random() * fonts.length);
  document.getElementById("front").style.fontFamily = fonts[randomIndex];

  var sizes = ["10pt", "11pt", "12pt", "13pt", "14pt", "15pt", "16pt"];
  var randomIndex = Math.floor(Math.random() * sizes.length);
  document.getElementById("front").style.fontSize = sizes[randomIndex];
</script>
```

Back:

```
{{FrontSide}}

<hr id=answer>

{{Back}}
<br/><br/>
<div class="notes">
{{Notes}}
</div>
```

Styling:

```
.card {
 font-family: "Segoe UI";
 font-size: 20px;
 text-align: center;
 color: black;
 background-color: white;
}

.notes {
 text-align: left;
 font-size: 18px;
 color: #444444;
}

.nightMode .notes {
 color: #888888;
}

code {
 color: #c7254e;
 background-color: #f9f2f4;
 font-family: Consolas, monospace;
}
```

The idea with the random index is that every time I get a card, a random font and random font size will be chosen.  This is to prevent "pattern matching" on the way the card looks.  I found the idea somewhere on Reddit and modified it.  I'm not actually sure if it's helping in any meaningful sense, but I don't think it's hurting, and I *feel* like it might be helping, so I've decided to keep it for now.

The left-aligning and making text gray for extra notes was something I saw on one of Andy Matuschak's Patreon posts and I decided I liked it.