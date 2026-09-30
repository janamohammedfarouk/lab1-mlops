# CSV Reader

A small desktop app that lets you choose a CSV file, displays its first three data rows, and prints them in the terminal.

The app uses Python's standard library, so it does not need third-party packages.

## Run on Windows

If you do not already have a virtual environment, create one:

```powershell
py -m venv .venv
```

Start the app directly from the environment. Activation is not required:

```powershell
.\.venv\Scripts\python.exe app.py
```

Click **Choose CSV file** and select a `.csv` file. The first three data rows appear in the app and are also printed in the terminal.

## Student details

Copy `.env.example` to `.env` and fill in your name and ID. The `.env` file is ignored by Git so personal details are not pushed to the repository.
