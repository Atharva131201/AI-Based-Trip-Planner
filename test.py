from dotenv import load_dotenv
import os
import psycopg2
from transformers import pipeline

# Load environment variables from req.env file
load_dotenv('req.env')

# Access the environment variables
api_token = os.getenv("HUGGINGFACE_API_TOKEN")
db_name = os.getenv("POSTGRES_DB")
db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_host = os.getenv("POSTGRES_HOST")
db_port = os.getenv("POSTGRES_PORT")

# Function to fetch data from PostgreSQL and prepare it for the table-question-answering task
def prepare_table_data(table_name):
    try:
        connection = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]

        table_data = {
            "table": {
                "headers": column_names,
                "data": []
            },
            "query": "What is the average age of people?"
        }

        for row in rows:
            # Ensure each row has the same number of elements as column_names
            if len(row) == len(column_names):
                row_dict = dict(zip(column_names, row))
                table_data["table"]["data"].append(row_dict)
            else:
                print(f"Skipping row {row} due to mismatched length with headers.")

        return table_data
    except Exception as e:
        print(f"Error fetching data from PostgreSQL: {e}")
        return None

# Example usage
if __name__ == "__main__":
    table_name = "person"

    table_data = prepare_table_data(table_name)
    if table_data:
        try:
            # Use a different model for table-question-answering
            model = pipeline("table-question-answering", model="google/tapas-large-finetuned-wtq", use_auth_token=api_token)
            result = model(table=table_data)
            print(result)
        except Exception as e:
            print(f"Error running table-question-answering pipeline: {e}")
