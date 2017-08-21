import mysql.connector

def notes_transform(text):
    if not text:
        return "&ndash;"
    words = []
    for word in text.split():
        if word.startswith("http"):
            words.append("""<a style="font-variant: small-caps;" href="{}">link</a>""".format(word))
        else:
            words.append(word)
    return " ".join(words)

cnx = mysql.connector.connect(user='issa', database='contractwork')
cursor = cnx.cursor()

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
            order by completion_date desc
        """

cursor.execute(query)

print("""
<!DOCTYPE html>
<html lang="en">
<head>
  <link rel="stylesheet" href="theme.default.css">
  <script src="jquery-3.2.1.min.js"></script>
  <script src="jquery.tablesorter.js"></script>
  <style type="text/css">
    table td {
        word-wrap: break-word;
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
</head>
<body>
<table>
    <thead>
        <tr>
            <th>Task receptacle</th>
            <th>Completion date</th>
            <th>Payment</th>
            <th>Topic</th>
            <th>Notes</th>
        </tr>
    </thead>
    <tbody>
        """)

for (task_receptacle, task_receptacle_url, task_type, task_venue,
     completion_date, payment, payer, topic, format_, notes) in cursor:
    print("    <tr>")
    print("""<td data-label="Task receptacle"><a href="{}">{}</a></td>""".format(task_receptacle_url,
        task_receptacle))
    print("""<td data-label="Completion date">{}</td>""".format(completion_date))
    print("""<td data-label="Payment" class="payment" title="Payer: {}">{}</td>""".format(payer, payment))
    print("""<td data-label="Topic">{}</td>""".format(topic))
    print("""<td data-label="Notes">{}</td>""".format(notes_transform(notes)))
    print("    </tr>")

print("""</tbody>
        </table>
<script>
  $(function(){
    $("table").tablesorter();
  });
</script>
        </body></html>""")

cursor.close()
cnx.close()
