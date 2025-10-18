import json
import psycopg2
from psycopg2.extras import RealDictCursor

# Database Setup

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


# 1. Recreate Table

def recreate_products_table():
    """
    Drop the table if exists, then create with the correct schema.
    """
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS products;")
        cur.execute("""
            CREATE TABLE products (
                product_id SERIAL PRIMARY KEY,
                name       TEXT NOT NULL,
                price      NUMERIC(6, 2) NOT NULL,
                in_stock   BOOLEAN DEFAULT TRUE
            );
        """)
        conn.commit()
        print("Step 1: products table recreated successfully")
    except Exception as e:
        print(f"Step 1 failed: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

# 2. Insert Data

def insert_sample_products():
    """
    Insert sample products into the table
    """
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO products (name, price, in_stock) VALUES
            ('Laptop', 3200.50, TRUE),
            ('Mouse', 99.99, TRUE),
            ('Keyboard', 250.00, FALSE),
            ('Monitor', 1190.95, TRUE);
        """)
        conn.commit()
        print("Step 2: Data inserted successfully")
    except Exception as e:
        print(f"Step 2 failed: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

# 3. Select Data

def select_products():
    """
    Select all products that are in stock using RealDictCursor
    """
    conn = None
    cur = None
    rows = []
    try:
        conn = get_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM products WHERE in_stock = TRUE;")
        rows = cur.fetchall()
        print("Step 3: Products selected successfully")
    except Exception as e:
        print(f"Step 3 failed: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
    return rows
