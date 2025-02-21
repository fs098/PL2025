# TP2 - Analysis of a musical works dataset

## Author: Filipe Santos, A100607

This Python script reads a CSV file containing information about musical works and generates three output files with organized and analyzed data. The output consists of:

1. An alphabetically ordered list of composers.

2. A file showing the number of musical works per period.

3. An alphabetically ordered list of musical work names per period.

## Usage

The script can be run using the following command:

```sh
python main.py csv-file-name [output-folder-name]
```

- **csv-file-name**: The path to the CSV file containing the musical works data. The CSV file must have the following header format:

    ```
    name;description;creationYear;period;composer;duration;id
    ```

- **output-folder-name (optional)**: The name of the folder where the output files will be saved. If not provided, the default folder name is **"output"**.

## Output Files

Once the script finishes running, it will generate the following files in the specified output folder:

1. **composers.txt**: An alphabetically ordered list of composers.

    Example content:
    ```
    Alessandro Stradella
    Antonio
    Antonio Maria Abbatini
    Bach
    ...
    ```

2. **works-by-period.txt**: A list of musical works ordered by period, with works listed alphabetically within each period.

    Example content:
    ```
    Barroco: Ab Irato, Die Ideale, S.106, ...
    Medieval: Adagio in B minor, Ballade No.1, ...
    ```

3. **number-of-works-by-period.txt**: A count of how many works exist in each musical period.

    Example content:
    ```
    Barroco: 26
    Clássico: 15
    Medieval: 48
    Renascimento: 41
    ...
    ```