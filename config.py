import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "20097130"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1cec77ed8878559fcc6c65d3fe1545e7")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://arupsaha9475:y3hUXbtH8CC9AntX@cluster0.k8nx1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
