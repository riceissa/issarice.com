#!/usr/bin/env python3
# License: CC0

import mysql.connector


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
            words.append("""<a style="font-variant: small-caps;" href="{}">link</a>""".format(word))
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
        links = task_receptacle_url.split(",")
        slinks = ", ".join(map(lambda x:
            """<a href="{}" style="font-variant: small-caps;">link</a>""" \
                    .format(x) if x.startswith("http") else x, links))
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
  <link rel="stylesheet" href="theme.default.css">
  <script src="jquery-latest.min.js"></script>
  <script src="jquery.tablesorter.js"></script>
  <style type="text/css">
    body {
        background-color: #fff;
        color: #222;
        font-family: Charter, "Bitstream Charter", Palatino, "Noto Serif", Georgia, serif;
    }
    h1 {
        font-size: 120%;
        text-transform: uppercase;
    }
    h2 { border-bottom: 1px solid #ccc; }
    h2, h3, h4, h5, h6 { font-size: 110%; }
    h1, h2, h3, h4, h5, h6 { font-family: Lato, Helvetica, sans-serif; }
    nav { font-family: Lato, Helvetica, sans-serif; }

    /* Hyphenate inside table cells;
     * from https://justmarkup.com/log/2015/07/dealing-with-long-words-in-css/
     */
    table td {
        overflow-wrap: break-word;
        word-wrap: break-word;
        -webkit-hyphens: auto;
        -ms-hyphens: auto;
        -moz-hyphens: auto;
        hyphens: auto;
    }

    table td.payment {
        text-align: right;
    }

    /* see https://techblog.livingsocial.com/blog/2015/04/06/responsive-tables-in-pure-css/
           https://codepen.io/anon/pen/QwPVNW */
    @media screen and (max-width: 600px) {
        tbody tr { border-bottom: none; }

        table {
          border: 0;
        }

        table td.payment {
            text-align: left;
        }

        table thead {
          display: none;
        }

        table tr {
          margin-bottom: 10px;
          display: block;
          border-bottom: 2px solid #ddd;
          padding-bottom: 5px;
        }

        table td {
          display: block;
          text-align: left;
          /*font-size: 13px;*/
          /*border-bottom: 1px dotted #ccc;*/
          text-indent: -30px;
          margin-left: 30px;
        }

        table td:last-child {
          border-bottom: 0;
        }

        table td:before {
          content: attr(data-label);
          float: left;
          padding-right: 40px;
          font-weight: bold;
        }
    }
  </style>
  <title>Task list for Issa Rice</title>
</head>
<body>
    <nav><a href="./index">Home</a>
    | <a href="./about">About</a></nav>
    <h1>Task list for Issa Rice</h1>
    <p>This page shows completed work that I have done. Most of the data is from <a href="https://contractwork.vipulnaik.com/worker.php?worker=Issa+Rice">Vipul Naik’s contract work portal</a>. I have also included other <a href="https://github.com/riceissa/issarice.com/blob/master/sql/work.sql">tasks not part of contract work</a>.
       There are other tasks that are not considered “complete” but which have significant work done on them; these are not included. I have also not included a lot of schoolwork and minor tasks.</p>
    <p><a href="https://github.com/riceissa/issarice.com/blob/master/generator/tasklist.py">Source code</a> for the script that prints this page is available.</p>
    <p>Hovering over the Payment column will show a tooltip giving the payer.</p>""")
print("<p>Showing {} tasks.</p>".format(count))
print("""<table style="table-layout: fixed;width:100%;">
  <thead>
    <tr>
      <th style="width:15%;">Task receptacle</th>
      <th>Venue</th>
      <th>Completion date</th>
      <th>Payment</th>
      <th>Topic</th>
      <th>Format</th>
      <th style="width:40%;">Notes</th>
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
    print("""      <td data-label="Payment" class="payment" title="Payer: {}">{}</td>""".format(payer, payment))
    print("""      <td data-label="Topic">{}</td>""".format(topic))
    print("""      <td data-label="Format">{}</td>""".format(format_))
    print("""      <td data-label="Notes">{}</td>""".format(notes_transformed(notes)))
    print("    </tr>")

print("""  </tbody>
</table>
<footer>
  To the extent possible under law, Issa Rice has waived all copyright and
  related or neighboring rights to the content on this page. This work is
  published from: United States.
  See the
  <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0
    1.0 Universal Public Domain Dedication</a>
  for more information.
</footer>
<script>
  $(function(){
    $("table").tablesorter();
  });
</script>
        </body></html>""")

cursor.close()
cnx.close()
