from pandas import DataFrame, read_csv
from pandas.errors import EmptyDataError

from .constants import DATA_PATH, DEFAULT_CHUNK_SIZE

# Mock function to fetch data with a delay
def fetch_data_chunk(page=1, chunk_size=DEFAULT_CHUNK_SIZE, shuffle=False):
    try:
        # Calculate the start and end rows for the chunk
        start_row = (page - 1) * chunk_size

        # Read the specific rows from the CSV file
        chunk = read_csv(
            DATA_PATH, skiprows=list(range(1, start_row + 1)), nrows=chunk_size
        )

        # Optionally shuffle the data to introduce randomness
        if shuffle:
            chunk = chunk.sample(frac=1).reset_index(drop=True)

        # Convert the DataFrame chunk to a list of dictionaries for JSON serialization
        chunk_list = chunk.to_dict(orient="records")
    except FileNotFoundError:
        return {
            "error": "File not found. Please check the file path.",
            "status_code": 404,
        }
    except EmptyDataError:
        return {"error": "No more data available.", "status_code": 404}
    except Exception as e:
        return {"error": str(e), "status_code": 500}

    return chunk_list


def process_data(data: DataFrame) -> DataFrame:
    """
    Example process_data function that processes the input data.
    Replace this with your actual data processing logic.
    """

    # For demonstration, let's convert all numeric columns to their squares
    processed_data = data.copy()
    for col in processed_data.select_dtypes(include="number").columns:
        processed_data[col] = processed_data[col] ** 2
    return processed_data
