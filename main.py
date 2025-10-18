import app_products-part1

def main():
    """
    Run all three steps from the PostgreSQL + Python exercise
    """
    # Step 1: Create table
    app_products.create_products_table()

    # Step 2: Insert data
    app_products.insert_sample_products()

    # Step 3: Select and print results
    products = app_products.select_products()

    print("\nProducts currently in stock:")
    if not products:
        print("(no rows found)")
    else:
        for p in products:
            print(f"id={p['product_id']}, name={p['name']}, price={p['price']}, in_stock={p['in_stock']}")

if __name__ == "__main__":
    main()

