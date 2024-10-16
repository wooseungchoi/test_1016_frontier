import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('movies_2024.csv')

# Streamlit app
def main():
    st.title("Movies Data Visualization")
    st.write("This app provides visualization for the movies dataset.")

    # Display the dataset
    if st.checkbox("Show Raw Data"):
        st.write(data)

    # Dropdown to select column for analysis
    column = st.selectbox("Select Column to Visualize", ["popularity", "budget", "revenue", "runtime", "vote_average", "vote_count"])

    # Plotting histogram for the selected column
    if column:
        st.write(f"Histogram of {column}")
        fig, ax = plt.subplots()
        ax.hist(data[column].dropna(), bins=20, color='skyblue', edgecolor='black')
        ax.set_xlabel(column)
        ax.set_ylabel("Frequency")
        st.pyplot(fig)

    # Bar chart to show movie count by language
    st.write("Movie Count by Language")
    language_count = data['original_language'].value_counts()
    fig, ax = plt.subplots()
    ax.bar(language_count.index, language_count.values, color='lightgreen')
    ax.set_xlabel("Language")
    ax.set_ylabel("Number of Movies")
    ax.set_title("Number of Movies by Language")
    st.pyplot(fig)

    # Scatter plot of budget vs. revenue
    st.write("Budget vs. Revenue")
    fig, ax = plt.subplots()
    ax.scatter(data['budget'], data['revenue'], alpha=0.5, color='coral')
    ax.set_xlabel("Budget")
    ax.set_ylabel("Revenue")
    ax.set_title("Budget vs. Revenue")
    st.pyplot(fig)

if __name__ == "__main__":
    main()