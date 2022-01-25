"""Function to return football table from a list of results"""
import pandas as pd
import numpy as np

cols = ["Team", "MP", "W", "D", "L", "P"]


def tally(rows: list[str]) -> list[str]:
    """Tabulates football results

    :param rows: list[str] - list of strings with results from football matches.
    :return: list[str] - Football table from given matches.
    """

    table = pd.DataFrame([], columns=cols)

    # Split list into individual matches.
    for each in rows:
        part = each.split(";")

        # Check if team is in table and add if necessary.
        for i in range(0, 2):
            if part[i] not in set(table["Team"]):
                table = table.append(
                    pd.DataFrame(
                        [[part[i]] + list(np.zeros(5, dtype=int))],
                        columns=cols,
                    )
                )

        # Check results and add to relevant column.
        if part[-1] == "win":
            table.loc[table.Team == part[0], "W"] += 1
            table.loc[table.Team == part[1], "L"] += 1
        elif part[-1] == "loss":
            table.loc[table.Team == part[1], "W"] += 1
            table.loc[table.Team == part[0], "L"] += 1
        else:
            table.loc[table.Team == part[1], "D"] += 1
            table.loc[table.Team == part[0], "D"] += 1

    # Update matches played and points.
    for each in table.iterrows():
        each[1][1] = sum(each[1][1:])
        each[1][-1] = 3 * each[1][2] + each[1][3]

    table.sort_values(by=["P", "Team"], ascending=[False, True], inplace=True)

    table_list = [cols] + table.to_numpy().tolist()

    return [
        "{0: <31}|{1: >3} |{2: >3} |{3: >3} |{4: >3} |{5: >3}".format(*line)
        for line in table_list
    ]
