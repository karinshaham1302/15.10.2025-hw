import pg_script

def main():
    # 1. Recreate the table to ensure the correct structure
    pg_script.recreate_products_table()

    # 2. insert sample rows
    pg_script.insert_sample_products()

    # 3. select & print
    products = pg_script.select_products()

    print("\nAvailable Products:")
    if not products:
        print("(no rows found)")
    else:
        for p in products:
            print(f"id={p['product_id']}, name={p['name']}, price={p['price']}, in_stock={p['in_stock']}")

if __name__ == "__main__":
    main()
