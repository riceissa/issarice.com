#!/usr/bin/env python3

import csv
import sys
import datetime


print("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
  <meta name="author" content="Issa Rice">""")
print("""<meta name="dcterms.date" content="{}">""".format(
      datetime.date.today().strftime("%Y-%m-%d")))
print("""<meta property="og:title" content="Account names" />
  <meta property="og:locale" content="en_US" />
  <meta property="article:author" content="https://www.facebook.com/riceissa" />
  <link rel="stylesheet" href="theme.default.css">
  <script src="jquery-latest.min.js"></script>
  <script src="jquery.tablesorter.js"></script>""")

with open("css/solarized_light.css", "r") as f:
    for line in f:
        print(line, end='')

with open("css/responsive_table.css", "r") as f:
    for line in f:
        print(line, end='')

print("""<title>Account names</title>
  <script src="change-theme.js"></script>
</head>
<body class="bigtable">
<script>
  set_theme_from_cookies();
</script>
    <nav id="site_navigation"><a href="./index">Home</a>
    | <a href="./about">About</a>
    | <a href="./_all_date">Newest changes</a>
    <span id="changeThemeMenu" style="display: none;">| Change
    {<a href="#" onclick="change_theme_text_width()">text width</a>,
     <a href="#" onclick="change_theme_color()">color</a>,
     <a href="#" onclick="change_theme_font_family()">font</a>,
     <a href="#" onclick="change_theme_table()">table</a>}</span>
    </nav>
    <main>
    <header>
      <h1>Account names</h1>
    </header>
<p>The following table lists the account names I use on various websites. It can be used as an authoritative guide of my online presence; if you are ever unsure if an account on a website is me, you can check this table. (However, there might be a bit of a lag between when I sign up for a service and when I add it to this table.)</p>
<p>As with <a href="software">software</a>, I like to sign up for a lot of online services to try them out, even though I know I won’t continue using most of them.</p>
<p>I usually use “riceissa” on most sites. This is a historical accident: when I tried to sign up for my Gmail account, “issarice” was already taken, so I picked “riceissa” instead. Since then, I’ve sort of standardized on “riceissa” for most services, although I also use “issarice”.</p>
<p>The “current activity” column describes how much I use the service now (the past six months, say). The numbers mean:</p>
<ul>
<li>0: No activity or close to no activity (not even signed in, hardly check the site).</li>
<li>1: Use around once per month.</li>
<li>2: More than once per week.</li>
</ul>
<p>The “total activity” column describes how much I have used the service across all time. This is an easier measure to score higher on, because it just requires that at some point in time I used a service moderately/regularly, or that I have used the service on and off over a long period of time. The numbers mean:</p>
<ul>
<li>0: No activity or close to no activity.</li>
<li>1: A small to moderate amount of activity.</li>
<li>2: More than a moderate amount of activity.</li>
</ul>
<p>For activity columns, the first number is “as consumer” and the second is “as producer”.</p>
<p>Regarding “forecasting” as a subject area versus “prediction” as a service type, at the moment they seem identical, but e.g. if a wiki about forecasting emerged, it would have a “forecasting” subject area but a “wiki” service type.</p>
<p>The “sphere” column says something about my motivation for caring about the service or how I came to know about the service in the first place. For instance, the Machine Learning Subwiki has “Vipul Naik” as its sphere rather than “Technology” because my account creation on that wiki was a direct result of being in contact with Vipul Naik rather than my general interest in technology.</p>
<p>The “EA/R” sphere refers to the <a href="effective-altruism">effective altruism</a> and <a href="rationality-community">rationality communities</a>.</p>
<p>With JavaScript enabled, it is possible to sort the table by each column.</p>
<p>If you like tables like these, you might enjoy looking at the <a href="https://contractwork.vipulnaik.com/worker.php?worker=Issa+Rice">contract work I’ve done for Vipul Naik</a>.</p>
  <table>
    <thead>
        <tr>
        <th>Service</th>
        <th>Account name</th>
        <th>Subject area</th>
        <th>Sphere</th>
        <th>Service type</th>
        <th>Join date</th>
        <th>Current activity (as consumer)</th>
        <th>Current activity (as producer)</th>
        <th>Total activity (as consumer)</th>
        <th>Total activity (as producer)</th>
        <th>Notes</th>
        </tr>
        </thead>
        <tbody>""")

with open("data/online-presence.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print("<tr>")
        # print("on", row["service"], len(row), file=sys.stderr)
        print('<td data-label="Service"><a href="{}">{}</a></td>'.format(row["service_url"], row["service"]))
        print('<td data-label="Account name"><a href="{}">{}</a></td>'.format(row["account_url"], row["account_name"]))
        print('<td data-label="Subject area">' + row["subject_area"] + "</td>")
        print('<td data-label="Sphere">' + row["sphere"] + "</td>")
        print('<td data-label="Service type">' + row["service_type"] + "</td>")
        print('<td data-label="Join date">' + row["join_date"] + "</td>")
        print('<td data-label="Current activity (as consumer)" style="text-align: right;">' + row["current_activity_as_consumer"] + "</td>")
        print('<td data-label="Current activity (as producer)" style="text-align: right;">' + row["current_activity_as_producer"] + "</td>")
        print('<td data-label="Total activity (as consumer)" style="text-align: right;">' + row["total_activity_as_consumer"] + "</td>")
        print('<td data-label="Total activity (as producer)" style="text-align: right;">' + row["total_activity_as_producer"] + "</td>")
        print('<td data-label="Notes">' + row["notes"] + "</td>")
        print("</tr>")

print("""  </tbody>
</table>
</main>
<footer>
  <br />
  <hr />
  <p>
  <a rel="license" href="https://creativecommons.org/publicdomain/zero/1.0/">
    <img src="./cc_public_domain.png" style="border-style: none;" alt="CC0" />
  </a>
  <br />
  To the extent possible under law, Issa Rice has waived all copyright and
  related or neighboring rights to the content on this page. This work is
  published from: United States.
  See the
  <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0
    1.0 Universal Public Domain Dedication</a>
  for more information.
  </p>
</footer>
<script>
  document.getElementById('changeThemeMenu').style.display='inline';
  $(function(){
    $("table").tablesorter();
  });
</script>
        </body></html>""")
