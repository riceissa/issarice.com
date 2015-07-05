#!/usr/bin/python3

import os
import sys
import subprocess
import shlex

def main():
    url = input("Enter URL for article: ").strip()
    open_editor = False
    if url.endswith(" -"):
        open_editor = True
    page = run_command("wget -qO- {}".format(url))
    title = run_command("""gawk -v IGNORECASE=1 -v RS='</title' 'RT{gsub(/.*<title[^>]*>/,"");print;exit}'""", pipe_in=page).strip()
    datetime = run_command("date +'%Y-%m-%d at %H:%M %p'").strip()
    if open_editor:
        pass
    else:
        print("Enter body text:")
        body = sys.stdin.read().strip() + "\n"
    print(make_entry(datetime, url, title, body))

def make_entry(datetime, url, title, body):
    template = '''
---

*{datetime}*

[{title}]({url})

{body}
'''
    return (template.format(datetime=datetime, title=title, url=url,
        body=body))

def run_command(command, pipe_in=None):
    '''
    Run command and return its output. Optionally pipe in string using
    pipe_in.  Same as
        command < pipe_in.txt
    where pipe_in.txt contains pipe_in.
    '''
    if pipe_in is None:
        process = subprocess.Popen(
            shlex.split(command),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, stderr = process.communicate()
    else:
        # See http://stackoverflow.com/a/165662/3422337
        process = subprocess.Popen(
            shlex.split(command),
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, stderr = process.communicate(input=bytes(pipe_in, 'utf-8'))
    if stderr not in ["None", "", None, b'']:
        print("On the command")
        print("    {command}".format(command=command))
        if pipe_in is not '':
            print("with the input line(s) beginning with")
            for line in pipe_in.split("\n"):
                l = min(75, len(line))
                print("    " + line[0:l])
        print("there was an error:")
        print(stderr.decode('utf-8'))
    if isinstance(stdout, bytes):
        return stdout.decode('utf-8')
    else:
        return stdout

if __name__ == "__main__":
    main()
