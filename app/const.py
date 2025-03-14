import dotenv

CONFIG = dotenv.dotenv_values("test.env")
POST_SIZE_BYTES = CONFIG['POST_SIZE_BYTES']



# defaults
if POST_SIZE_BYTES:
    POST_SIZE_BYTES = int(POST_SIZE_BYTES)
else:
    POST_SIZE_BYTES = 1048576 #1 MB

if not CONFIG['engine_string']:
    CONFIG['engine_string'] = "sqlite:///db.sqlite"
    