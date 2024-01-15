
import streamlit as st
import pandas as pd
import plotly.express as px

# 1.0 Title and Introduction
st.title("test dashboard")
a = "housut"
st.write(f"hello {a}")

st.write("""
this is test dashboard for functional testing
""")

# frontend
st.header("upload datas")
uploaded_file = st.file_uploader("choose file",
                                 type = "csv",
                                 accept_multiple_files = False)
#backend
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("preview data")
    st.write(data.head())

    # total sales
    st.header("sales insights")
    if "sales_date" and "sales_amount" in data.columns:
        st.write("sales over time")
        fig = px.line(data, x = "sales_date", y = "sales_amount",
                    title="sales over time")
        st.plotly_chart(fig)
    else:
        st.warning("no sales data found")

    # regional sales
    st.header("regional sales")
    if "region" and "sales_amount" in data.columns:
        st.write("sales per region")
        fig = px.bar(data, x = "region", y = "sales_amount",
                    title="sales per region",
                    color="region")
        st.plotly_chart(fig)
    else:
        st.warning("no region data found!")

    # product sales
        st.header("product sales")
    if "product" and "sales_amount" in data.columns:
        st.write("products by sales")
        # summarise by product sum sales amount
        group = data.groupby("product").agg({"sales_amount":"sum"}).reset_index()
    # order the figure by sales amount
        fig = px.bar(group.sort_values("sales_amount", ascending=False),
                    x = "product", y = "sales_amount",
                    title="products by sales",
                    color="product")
        st.plotly_chart(fig)

    # feedback
    st.header("feedback")
    feedback = st.text_area("please leave feedback here")

    if st.button("submit"):
        st.success("feedback submitted")

# footer
st.write("---")
st.write("made with streamlit, easy to use app frameworks for data science!")

if __name__ == "__main__":
    pass