import os
import re
import sys


ComposerList = list[str]
WorksByPeriodDict = dict[str, list[str]]
MusicalWorksData = tuple[ComposerList, WorksByPeriodDict]


def parse_musical_works_csv(filename: str) -> MusicalWorksData:
    """
    Reads a CSV file of musical works and returns an alphabetically ordered list of composers,
    along with a dictionary of musical work names, alphabetically ordered, categorized by period.
    """
    composers = set()
    works_by_period: WorksByPeriodDict = {}

    for csv_row in get_musical_works_without_desc(filename):
        fields = csv_row.split(";")

        # Composers:
        composer_field = fields[3]
        for composer in re.split(r", ?", composer_field):
            composers.add(composer)

        # Musical works by period:
        work_name = fields[0]
        period = fields[2]

        if period in works_by_period:
            works_by_period[period].append(work_name)
        else:
            works_by_period[period] = [work_name]

    sorted_works_by_period = {
        period: sorted(works) for period, works in works_by_period.items()
    }

    composer_list = list(composers)
    composer_list.sort()

    return composer_list, sorted_works_by_period


def get_musical_works_without_desc(filename: str) -> list[str]:
    """
    Musical works CSV header: name;description;creationYear;period;composer;duration;id.
    Returns the rows of a musical works CSV file, excluding the description field.
    """
    lines = []
    with open(filename, "r") as file:
        # Remove multiline descriptions:
        content = re.sub(r';"(?s:.*?)";', ";", file.read())

        for line in content.splitlines()[1:]:
            fields = line.split(";")

            if len(fields) == 6:
                lines.append(line)

            # Single line description:
            elif len(fields) == 7:
                fields.pop(1)
                lines.append(";".join(fields))

    return lines


def main() -> None:
    if len(sys.argv) not in [2, 3]:
        sys.exit("invalid number of arguments")

    output_dir = "output"
    musical_works_csv = sys.argv[1]

    if len(sys.argv) == 3:
        output_dir = sys.argv[2]

    if not os.path.exists(musical_works_csv):
        sys.exit("csv file does not exist")

    composers, works_by_period = parse_musical_works_csv(musical_works_csv)

    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(output_dir, "composers.txt"), "w") as file:
        file.write("\n".join(composers))

    with open(os.path.join(output_dir, "works-by-period.txt"), "w") as file:
        for period, works in works_by_period.items():
            file.write(f"{period}: {", ".join(works)}\n")

    with open(os.path.join(output_dir, "number-of-works-by-period.txt"), "w") as file:
        for period, works in works_by_period.items():
            file.write(f"{period}: {len(works)}\n")


if __name__ == "__main__":
    main()
