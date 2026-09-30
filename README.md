# CSV Reader

A small Streamlit app that lets you upload a CSV file and view its first three rows.

## Run locally

Create and activate a virtual environment, then install the dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Start the app:

```powershell
streamlit run app.py
```

Open the local URL printed by Streamlit and upload a `.csv` file. The first three rows appear in the page and are also printed in the terminal.

## Student details

Copy `.env.example` to `.env` and fill in your name and ID. The `.env` file is ignored by Git so personal details are not pushed to the repository.
