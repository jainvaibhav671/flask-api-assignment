from flask import Blueprint, request
from pandas import DataFrame

from .cache import Cache
from .constants import DEFAULT_CHUNK_SIZE
from .utils import fetch_data_chunk, process_data

# In-memory storage for processed data
cache = Cache()

# Mock function to fetch a specific chunk of data
v1 = Blueprint('v1', __name__)

store = dict()


@v1.get("/")
def index():
    return "<h1>This is version 1 of this api</h1>"


@v1.route("/fetch-data", methods=["GET"])
def fetch_data_endpoint():
    # Get pagination parameters from the request
    page = request.args.get("page", default=1, type=int)
    chunk_size = request.args.get("chunk_size", default=DEFAULT_CHUNK_SIZE, type=int)
    shuffle = request.args.get("shuffle", default="false").lower() == "true"

    cache_key = f"page_{page}_chunk_{chunk_size}"
    cached_data = cache.get(cache_key)
    if cached_data:
        return cached_data

    # Fetch the specific data chunk
    data_chunk = fetch_data_chunk(page, chunk_size, shuffle)

    # If an error occurred, return the error
    if isinstance(data_chunk, dict) and data_chunk.get("error"):
        return data_chunk

    cache.add(cache_key, data_chunk)

    return data_chunk


@v1.route("/get-processed-data", methods=["GET"])
def get_processed_data_endpoint():
    # Get pagination parameters from the request
    page = request.args.get("page", default=1, type=int)
    chunk_size = request.args.get("chunk_size", default=DEFAULT_CHUNK_SIZE, type=int)
    shuffle = request.args.get("shuffle", default=False, type=bool)

    # Check if the processed data is already cached
    cache_key = f"page_{page}_chunk_{chunk_size}"
    cached_data = cache.get(cache_key)
    if cached_data:
        return cached_data

    # Fetch the specific data chunk
    data_chunk = fetch_data_chunk(page, chunk_size, shuffle)

    # If an error occurred, return the error
    if isinstance(data_chunk, dict) and data_chunk.get("error"):
        return data_chunk

    # Convert chunk back to DataFrame for processing
    df = DataFrame(data_chunk)

    # Convert the processed DataFrame back to a list of dictionaries for JSON response
    processed_data_list = process_data(df).to_dict(orient="records")

    # Store the processed data in the in-memory cache
    cache.add(cache_key, processed_data_list)

    return processed_data_list
