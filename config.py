# Copyright (c) 2023 EDM115
import os


class Config:
    APP_ID = int(os.environ.get("24490919"))
    API_HASH = os.environ.get("d1b3b15126c47dd4cb491553ee1db910")
    BOT_TOKEN = os.environ.get("6455342244:AAGVBztqflke4VMxs_2fVc14wFunR43Dllw")
    LOGS_CHANNEL = int(os.environ.get("-1002092398392"))
    MONGODB_URL = os.environ.get("mongodb+srv://spymusicbot:spymusicbot@cluster0.l4pi5sr.mongodb.net/?retryWrites=true&w=majority")
    BOT_OWNER = int(os.environ.get("5621114370"))
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/Downloaded"
    THUMB_LOCATION = f"{os.path.dirname(__file__)}/Thumbnails"
    TG_MAX_SIZE = 2097152000
    # Default chunk size (0.005 MB → 1024*6) Increase if you need faster downloads
    CHUNK_SIZE = 1024 * 1024 * 10  # 10 MB
    BOT_THUMB = f"{os.path.dirname(__file__)}/bot_thumb.jpg"
    MAX_CONCURRENT_TASKS = 50
    MAX_TASK_DURATION_EXTRACT = 45 * 60  # 45 minutes (in seconds)
    MAX_TASK_DURATION_MERGE = 90 * 60  # 1 hour 30 minutes (in seconds)
