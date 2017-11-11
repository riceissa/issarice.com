#!/usr/bin/env python3
# License: CC0

import mysql.connector
import datetime


SEEN = {}


def notes_transformed(text):
    if not text:
        return "&ndash;"
    words = []
    for word in text.split():
        word = word[0].replace('"', '“') + word[1:]
        word = word[0].replace("'", '‘') + word[1:]
        word = word.replace('"', '”')
        word = word.replace("'", "’")
        if word.startswith("http"):
            if word not in SEEN:
                SEEN[word] = len(SEEN) + 1
            words.append("""<a href="{}">[{}]</a>""".format(word, SEEN[word]))
        elif word == "<=":
            words.append("&le;")
        elif word == ">=":
            words.append("&ge;")
        elif word == "--":
            words.append("&ndash;")
        else:
            words.append(word)
    return " ".join(words)


def task_receptacle_formatted(task_receptacle, task_receptacle_url):
    if (task_receptacle and task_receptacle_url and
        "," not in task_receptacle_url and not task_receptacle_url.startswith("N/A")):
        return """<a href="{}">{}</a>""".format(task_receptacle_url,
                task_receptacle)
    elif task_receptacle_url and not task_receptacle_url.startswith("N/A"):
        # Here a link can be a URL or be something like "others"
        links = task_receptacle_url.split(",")
        for link in links:
            if link.startswith("http") and link not in SEEN:
                SEEN[link] = len(SEEN) + 1
        slinks = ", ".join(map(lambda x:
            """<a href="{}">[{}]</a>""" \
                    .format(x, SEEN[x]) if x.startswith("http") else x, links))
        return """{} """.format(task_receptacle) + slinks
    else:
        return task_receptacle

cnx = mysql.connector.connect(user='issa', database='contractwork')
cursor = cnx.cursor()

# cursor.rowcount is supposed to give the number of rows but it seems to just
# return -1, possibly because it can't figure out the number of rows before
# iterating. For now it's easiest to just do a separate query
# https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-rowcount.html
count = 0
cursor.execute("""select count(*) from tasks where worker = 'Issa Rice'""")
count += cursor.fetchall()[0][0]
cursor.execute("""select count(*) from individual_tasks""")
count += cursor.fetchall()[0][0]

query = """
            select
                task_receptacle,
                task_receptacle_url,
                task_type,
                task_venue,
                completion_date,
                payment,
                payer,
                topic,
                format,
                notes
            from tasks
            where worker = 'Issa Rice'
            union
            select
                task_receptacle,
                task_receptacle_url,
                task_type,
                task_venue,
                completion_date,
                payment,
                payer,
                topic,
                format,
                notes
            from individual_tasks
            order by completion_date desc
        """

cursor.execute(query)

print("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
  <meta name="author" content="Issa Rice">""")
print("""<meta name="dcterms.date" content="{}">""".format(
      datetime.date.today().strftime("%Y-%m-%d")))
print("""<meta property="og:title" content="Task list for Issa Rice" />
  <meta property="og:locale" content="en_US" />
  <meta property="article:author" content="https://www.facebook.com/riceissa" />
  <link rel="stylesheet" href="theme.default.css">
  <script src="jquery-latest.min.js"></script>
  <script src="jquery.tablesorter.js"></script>
  """)

with open("css/solarized_light.css", "r") as f:
    for line in f:
        print(line, end='')

with open("css/responsive_table.css", "r") as f:
    for line in f:
        print(line, end='')

print("""<title>Task list for Issa Rice</title>
  <script src="change-theme.js"></script>
</head>
<body class="bigtable">
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
      <h1>Task list for Issa Rice</h1>
    </header>
    <p>This page shows completed work that I have done. Most of the data is from <a href="https://contractwork.vipulnaik.com/worker.php?worker=Issa+Rice">Vipul Naik’s contract work portal</a>. I have also included other <a href="https://github.com/riceissa/issarice.com/blob/master/data/work.sql">tasks not part of contract work</a>.
       There are other tasks that are not considered “complete” but which have significant work done on them; these are not included unless payment is processed for completing some portion of the overall work (e.g. ongoing development for the donations list website or adding rows to some timeline). I have also not included a lot of schoolwork and minor tasks.</p>
    <p>For the “Notes” column, some of the rows are entered by Vipul and
       some by me, so the “voice” of writing will be different.
       The way to tell who wrote a particular row is to look at the
       “Payment” column: if the value there is 0, I wrote it, and if
       it is a positive number, Vipul wrote it. I realize this is not
       the best user experience, but I don’t really want to go back
       and rewrite all the notes for the contract work columns, so
       you will just have to live with it.</p>
    <p><a href="https://github.com/riceissa/issarice.com/blob/master/generator/tasklist.py">Source code</a> for the script that prints this page is available.</p>
    <p>Hovering over the Payment column will show a tooltip giving the payer.</p>""")
print("<p>Showing {} tasks sorted by completion date. With JavaScript enabled, it is possible to sort by each column (unless the window is too narrow, in which case the table collapses into a “definition list” format for easier viewing).</p>".format(count))
print("<p>This table was last generated on {}.</p>".format(datetime.date.today().strftime("%B %-d, %Y")))
print("""<table>
  <thead>
    <tr>
      <th>Task receptacle</th>
      <th>Venue</th>
      <th>Completion date</th>
      <th>Payment</th>
      <th>Topic</th>
      <th>Format</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>""")

for (task_receptacle, task_receptacle_url, task_type, task_venue,
     completion_date, payment, payer, topic, format_, notes) in cursor:
    print("    <tr>")
    print("""      <td data-label="Task receptacle">{}</td>""" \
        .format(task_receptacle_formatted(task_receptacle, task_receptacle_url)))
    print("""      <td data-label="Venue">{}</td>""".format(task_venue))
    print("""      <td data-label="Completion date">{}</td>""".format(completion_date))
    print("""      <td data-label="Payment" style="text-align: right;" title="Payer: {}">{}</td>""".format(payer, payment))
    print("""      <td data-label="Topic">{}</td>""".format(topic))
    print("""      <td data-label="Format">{}</td>""".format(format_))
    print("""      <td data-label="Notes">{}</td>""".format(notes_transformed(notes)))
    print("    </tr>")

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
  set_theme_from_cookies();
  $(function(){
    $("table").tablesorter();
  });
</script>
        </body></html>""")

cursor.close()
cnx.close()
