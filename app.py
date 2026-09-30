"""A small Streamlit app for previewing the first three rows of a CSV file."""

import pandas as pd
import streamlit as st


st.set_page_config(page_title="CSV Reader", page_icon="📄")
st.title("CSV Reader")
st.write("Upload a CSV file to preview its first three rows.")

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        dataframe = pd.read_csv(uploaded_file)
    except (
        pd.errors.EmptyDataError,
        pd.errors.ParserError,
        UnicodeDecodeError,
        ValueError,
    ) as error:
        st.error(f"Could not read this CSV file: {error}")
    else:
        first_three_rows = dataframe.head(3)
        st.subheader("First three rows")
        st.dataframe(first_three_rows, use_container_width=True)
        print(first_three_rows.to_string(index=False))
