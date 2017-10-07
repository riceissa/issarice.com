#!/usr/bin/env python3

import csv
import sys


print("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
  <link rel="stylesheet" href="theme.default.css">
  <script src="jquery-latest.min.js"></script>
  <script src="jquery.tablesorter.js"></script>
  </head>
  <body>
  <table>
    <thead>
        <tr>
        <th>Service</th>
        <th>Account name</th>
        <th>Subject area</th>
        <th>Sphere</th>
        <th>Service type</th>
        <th>Join date</th>
        <th align="right">Current activity (as consumer)</th>
        <th align="right">Current activity (as producer)</th>
        <th align="right">Total activity (as consumer)</th>
        <th align="right">Total activity (as producer)</th>
        <th>Notes</th>
        </tr>
        </thead>
        <tbody>""")

with open("sql/online-presence.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print("<tr>")
        print("on", row["service"], len(row), file=sys.stderr)
        print('<td><a href="{}">{}</a></td>'.format(row["service_url"], row["service"]))
        print('<td><a href="{}">{}</a></td>'.format(row["account_url"], row["account_name"]))
        print("<td>" + row["subject_area"] + "</td>")
        print("<td>" + row["sphere"] + "</td>")
        print("<td>" + row["service_type"] + "</td>")
        print("<td>" + row["join_date"] + "</td>")
        print("<td>" + row["current_activity_as_consumer"] + "</td>")
        print("<td>" + row["current_activity_as_producer"] + "</td>")
        print("<td>" + row["total_activity_as_consumer"] + "</td>")
        print("<td>" + row["total_activity_as_producer"] + "</td>")
        print("<td>" + row["notes"] + "</td>")
        print("</tr>")
