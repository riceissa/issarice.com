#!/usr/bin/python3

import os
import sys
import subprocess
import shlex

def main():
    url = input("Enter URL for article: ").strip()
    open_editor = True
    if url.endswith(" -"):
        open_editor = False
    log_if_v("Downloading page ...")
    page = run_command("wget -qO- {}".format(url))
    title = run_command("""gawk -v IGNORECASE=1 -v RS='</title' 'RT{gsub(/.*<title[^>]*>/,"");print;exit}'""", pipe_in=page).strip()
    log_if_v("Page downloaded and title parsed as {}".format(title))
    datetime = run_command("date +'%Y-%m-%d at %I:%M %p'").strip()
    with open("wiki/articles-read.md", "r") as r:
        original = [line for line in r]
    log_if_v("Contents of wiki/articles-read.md read.")
    if open_editor:
        with open("wiki/articles-read.md", "w") as w:
            for line in original[:37]:
                w.write(line)
            w.write(make_entry(datetime, url, title, ""))
            for line in original[37:]:
                w.write(line)
        subprocess.call(["vim", "+42", "wiki/articles-read.md"])
    else:
        print("Enter body text:")
        body = sys.stdin.read().strip() + "\n"
        with open("wiki/articles-read.md", "w") as w:
            for line in original[:37]:
                w.write(line)
            w.write(make_entry(datetime, url, title, body))
            for line in original[37:]:
                w.write(line)
        log_if_v("File written.")

def make_entry(datetime, url, title, body):
    template = '''
*{datetime}*

[{title}]({url})

{body}

---

'''
    return (template.format(datetime=datetime, title=title, url=url,
        body=body))

def log_if_v(text, log=True):
    if log:
        print(text)

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
