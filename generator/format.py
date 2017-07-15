#!/usr/bin/env python3
# LICENSE: CC0

import sys
import re


def main():
    print("""<!DOCTYPE html>
          <html lang="en">
          <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <title></title>
          </head>
          <body>""")
    for line in sys.stdin:
        result = line.replace('&', '&amp;').replace('<', '&lt;') \
                    .replace('>', '&gt;')
        m = re.match(r"^[ ]+", result)
        if m is not None:
            result = "&nbsp;" * len(m.group(0)) + result.lstrip()
        result = re.sub(r"""(https?://[^\t "'<>|]+[A-Za-z0-9/])""",
                        r"""<a href="\1">\1</a>""", result)
        result += "<br />"
        print(result)
    print("""</body>
          </html>""")


if __name__ == "__main__":
    main()
