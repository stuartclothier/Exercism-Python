import re


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
            "em": r"((?<!\*)\*(?!\*)(.*)\*)|_(.*)_" # Possibly add look behind
        }
        
        for el in formats.values():
            if re.search(el, i):
                m1 = re.search(el, i)
                i = m1.string[0:m1.start()]+"<strong>"+m1.group(1)+"</strong>"+m1.string[m1.end():]
        
        i = f"<{element}>{i}</{element}>"
        res += i

    return res

print(parse("__This will be bold__"))

    #     if m:
    #         if not in_list:
    #             in_list = True
    #             is_bold = False
    #             is_italic = False
    #             curr = m.group(1)
    #             m1 = re.match("(.*)__(.*)__(.*)", curr)
    #             if m1:
    #                 curr = (
    #                     m1.group(1)
    #                     + "<strong>"
    #                     + m1.group(2)
    #                     + "</strong>"
    #                     + m1.group(3)
    #                 )
    #                 is_bold = True
    #             m1 = re.match("(.*)_(.*)_(.*)", curr)
    #             if m1:
    #                 curr = (
    #                     m1.group(1)
    #                     + "<em>"
    #                     + m1.group(2)
    #                     + "</em>"
    #                     + m1.group(3)
    #                 )
    #                 is_italic = True
    #             i = "<ul><li>" + curr + "</li>"
    #         else:
    #             is_bold = False
    #             is_italic = False
    #             curr = m.group(1)
    #             m1 = re.match("(.*)__(.*)__(.*)", curr)
    #             if m1:
    #                 is_bold = True
    #             m1 = re.match("(.*)_(.*)_(.*)", curr)
    #             if m1:
    #                 is_italic = True
    #             if is_bold:
    #                 curr = (
    #                     m1.group(1)
    #                     + "<strong>"
    #                     + m1.group(2)
    #                     + "</strong>"
    #                     + m1.group(3)
    #                 )
    #             if is_italic:
    #                 curr = (
    #                     m1.group(1)
    #                     + "<em>"
    #                     + m1.group(2)
    #                     + "</em>"
    #                     + m1.group(3)
    #                 )
    #             i = "<li>" + curr + "</li>"
    #     else:
    #         if in_list:
    #             in_list_append = True
    #             in_list = False

    #     m = re.match("<h|<ul|<p|<li", i)
    #     if not m:
    #         i = "<p>" + i + "</p>"
    #     m = re.match("(.*)__(.*)__(.*)", i)
    #     if m:
    #         i = m.group(1) + "<strong>" + m.group(2) +
    # "</strong>" + m.group(3)
    #     m = re.match("(.*)_(.*)_(.*)", i)
    #     if m:
    #         i = m.group(1) + "<em>" + m.group(2) + "</em>" + m.group(3)
    #     if in_list_append:
    #         i = "</ul>" + i
    #         in_list_append = False
    #     res += i
    # if in_list:
    #     res += "</ul>"
