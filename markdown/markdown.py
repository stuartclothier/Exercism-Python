import re


############### ADD SIGNIFICANTLY CLEARER COMMENTS


def parse(markdown):

    # Break lines
    # lines = markdown.split("\n")

    # Not sure
    res = ""
    in_list = False
    # in_list_append = False

    # Parse each line
    for i in markdown.split("\n"):

        # Check for list
        li = re.match(r"\* (.*)", i)
        if li:
            i = i[2:]
            if not in_list:
                i = f"<ul>{i}"
                in_list = True
            element = "li"
        elif not li and in_list:
            in_list = False
            res += "</ul>"

        # Check for heading, NB: although not conventional markdown/html allows
        # for headings in lists hence this is a separate if statement not elif
        # elif statement confirms not in list nor a heading and therefore is paragraph
        headings = re.match("^#*", i)
        if 0 < headings.end() < 7:
            element = f"h{headings.end()}"
            i = i[headings.end() + 1 :]
        elif not in_list:
            element = "p"

        # Format bold and italics
        formats = {
            "strong": r"(\*\*(.*)\*\*)|(__(.*)__)",
            "em": r"((?<!\*)\*(?!\*)(.*)\*)|_(.*)_",  # Possibly add look behind
        }

        for element, reg in formats.items():
            if re.search(reg, i):
                m1 = re.search(reg, i)

                i = f"""{m1.string[0 : m1.start()]}<{element}>{m1.groups()[-1]}</{element}>{m1.string[m1.end() :]}"""

        # Think this adds outer tags, e.g. heading or paragraph
        i = f"<{element}>{i}</{element}>"
        res += i

    return res


print(parse("__How does _This will be bold___"))
