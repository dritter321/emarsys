import sqlite3

# Load SQL query from the file
def load_query_from_file(file_path):
    with open(file_path, 'r') as file:
        query = file.read()
    return query

def main():
    # SQLite database file
    database_file = "marketing_data.db"

    # SQL query file
    query_file = "./queries/task_01.sql"

    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(database_file)
        cursor = connection.cursor()
        print(f"Connected to database: {database_file}")

        # Load SQL query from the file
        query = load_query_from_file(query_file)
        print(f"Loaded query from file: {query_file}")

        # Execute the loaded query
        cursor.execute(query)

        # Fetch results (if the query returns data)
        results = cursor.fetchall()
        print("Query executed successfully. Results:")

        # Display results
        for row in results:
            print(row)

        # Close the cursor and connection
        cursor.close()
        connection.close()
        print("Connection closed.")

    except FileNotFoundError:
        print(f"Error: Query file '{query_file}' not found.")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()