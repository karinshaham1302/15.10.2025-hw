import json
import psycopg2
from psycopg2.extras import RealDictCursor
import streamlit as st

def get_db_config():
    """
    Read database connection details from db_config.json file.
    """
    with open('db_config.json') as f:
        return json.load(f)

def get_connection():
    """
    Establish a connection to the PostgreSQL database using config file.
    """
    config = get_db_config()
    return psycopg2.connect(**config)


# Part A: Calculator
# 1. Display your name at the top
st.title("Karin Shaham")

# 2. Create two numeric input fields
st.subheader("Calculator")
n1 = st.text_input("Number 1")
n2 = st.text_input("Number 2")

# 3. Add a button labeled "Add"
if st.button("Add"):
    try:
        # Convert input to float and add them
        a = float(n1)
        b = float(n2)
        total = a + b
        # show the result using st.success()
        st.success(f"Sum: {total}")
    except ValueError:
        # extra safety
        st.warning("Please enter valid numeric values in both fields.")


# Part B: Display Available Products
# 1. Add a subheader
st.subheader("Available Products")

# 2. Create a function to show products
def available_products():
    """
    Fetch all available products (in stock) from the PostgreSQL database.
    """
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM products WHERE in_stock = TRUE;")
        return cur.fetchall()
    except Exception as e:
        st.error(f"Failed to fetch products: {e}")
        return []
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


if st.button("Show Products"):
    rows = available_products()
    if not rows:
        st.info("No products found.")
    else:
        st.write("Available Products:")
        for r in rows:
            st.write(dict(r))
