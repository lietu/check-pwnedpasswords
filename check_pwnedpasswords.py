from __future__ import unicode_literals, print_function
from argparse import ArgumentParser
import codecs
from collections import namedtuple
import json
import sys
import pwnedpasswords

PasswordEntry = namedtuple("PasswordEntry", ("name", "password",))


class DashlaneJsonReader(object):
    def __init__(self, filename):
        self._filename = filename
        self._index = 0
        self._items = []

    def __enter__(self):
        fp = open(self._filename, "rt")
        data = json.load(fp)
        fp.close()

        try:
            self._items = data["AUTHENTIFIANT"]
        except KeyError:
            raise KeyError("Could not find AUTHENTIFIANT -key in JSON. Is "
                           "this a Dashlane JSON export?")

        return self

    def __exit__(self, *exc_info):
        pass

    def __iter__(self):
        self._index = 0
        return self

    def next(self):
        try:
            item = self._items[self._index]
        except IndexError:
            raise StopIteration()

        self._index += 1

        username = item["email"] if item["login"] == "" else item["login"]
        identifier = "{}: {}".format(item["domain"], username)
        name = "{} ({})".format(item["title"], identifier)

        return PasswordEntry(
            name=name,
            password=item["password"]
        )


def process_entries(reader):
    found = {}
    not_found = []

    print("Processing entries", end="")

    with reader as r:
        for entry in r:
            count = pwnedpasswords.check(entry.password)
            if count > 0:
                found[entry.name] = count
            else:
                not_found.append(entry.name)
            sys.stdout.write(".")
            sys.stdout.flush()

    print(" done!")
    print("")

    return found, sorted(not_found, key=lambda s: s.lower())


if __name__ == "__main__":
    # Who knows what kind of things you have in your usernames and domains
    utf8_writer = codecs.getwriter('UTF-8')
    if sys.version_info.major < 3:
        sys.stdout = utf8_writer(sys.stdout, errors='replace')
    else:
        sys.stdout = utf8_writer(sys.stdout.buffer, errors='replace')

    ap = ArgumentParser()
    ap.add_argument("filename", help="Filename to read data from")
    options = ap.parse_args()

    reader = DashlaneJsonReader(options.filename)
    found, not_found = process_entries(reader)

    if len(not_found) > 0:
        print("The following entries are safe:")
        for name in not_found:
            print(" - {}".format(name))

        print("")

    if len(found) > 0:
        print("The passwords for the following were found in some leaks:")
        for name in found:
            print(" - {} ({} leaks)".format(name, found[name]))
        print("")
    else:
        print("None of your passwords have been leaked. Congratulations!")
        print("")

    processed = len(found) + len(not_found)
    print("")
    print("Processed {} passwords".format(processed))
