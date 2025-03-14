import dotenv
# dotenv.load_dotenv('.env')

CONFIG = dotenv.dotenv_values()
POST_SIZE_BYTES = int(CONFIG["POST_SIZE_BYTES"]) # type: ignore