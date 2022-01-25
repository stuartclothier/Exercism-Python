def tally(rows: list[str]) -> list[str]:
    """Tabulates football results

    :param rows: list[str] - list of strings with results from football
    matches.
    :return: list[str] - Football table from given matches.
    """

    # Initiate dictionary for table and sorter list
    table = {}
    sorter = []

    res = {"win": 0, "loss": 1}

    for each in rows:
        part = each.split(";")

        # add team(s) in not in table
        for i in range(0, 2):
            if part[i] not in table:
                table[part[i]] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}

        # To populate table, the result given in last part of each line is used
        # to index the line for the winner or loser (or drawn) via the res dict.
        # i.e. If the result is win the team in part[0] is the winner and if
        # result is loss the team in part[1] is the winner.
        if part[-1] in res:
            table[part[res[part[-1]]]]["W"] += 1
            table[part[1 - res[part[-1]]]]["L"] += 1
        else:
            table[part[0]]["D"] += 1
            table[part[1]]["D"] += 1

    for each in table:
        table[each]["MP"] = sum(table[each].values())
        table[each]["P"] = table[each]["W"] * 3 + table[each]["D"]
        sorter.append(
            [table[each]["P"], each]
        )  # Two columns relevant for sorting

    # Sort this list, first by second element (Name) in Alphabetical order then by points desceding
    order = sorted(
        sorted(sorter, key=lambda x: x[1]), key=lambda x: x[0], reverse=True
    )

    table_text = [["Team", "MP", "W", "D", "L", "P"]]
    for team in order:
        table_text.append([team[1]] + list(table[team[1]].values()))

    return [
        "{0: <31}|{1: >3} |{2: >3} |{3: >3} |{4: >3} |{5: >3}".format(*line)
        for line in table_text
    ]
