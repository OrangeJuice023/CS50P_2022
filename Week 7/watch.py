import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # parses links such as <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
    # <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0"
    # allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

    # intitate main data first
    url_frame = re.search(r"<iframe(.)*><\/iframe>", s)
    format_yt = re.search(r"(http(s)?:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-z_0-9]+)", s)

    if url_frame:
        if format_yt:
            splitter_frmt = format_yt.groups()
            return "https://youtu.be/" + splitter_frmt[3]

if __name__ == "__main__":
    main()
