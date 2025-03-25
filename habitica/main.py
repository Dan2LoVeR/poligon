import os
import requests
from dotenv import load_dotenv

load_dotenv()

USER_ID = os.getenv('HABITICA_USER_ID')
API_TOKEN = os.getenv('HABITICA_ID_TOKEN')

API_URL = 'https://habitica.com/api/v3'

def get_user_data():
    headers = {
        "x-client": f"{USER_ID}-MyHabiticaScript",
        "x-api-user": USER_ID,
        "x-api-key": API_TOKEN,
    }
    response = requests.get(f"{API_URL}/user", headers=headers)
    if response.status_code == 200:
        return response.json()["data"]
    else:
        raise Exception(f"Ошибка при запросе: {response.status_code} - {response.text}")

def generate_html(user_data):
    avatar_url = f"https://habitica.com/export/avatar-{USER_ID}.png"
    level = user_data.get("stats", {}).get("lvl", "N/A")
    health = user_data.get("stats", {}).get("hp", "N/A")
    max_health = user_data.get("stats", {}).get("maxHealth", "N/A")

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Habitica Stats</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
                line-height: 1.6;
            }}
            .avatar {{
                width: 140px;
                height: 147px;
                border: 1px solid #ddd;
                margin-bottom: 10px;
            }}
            .stats {{
                margin-top: 10px;
            }}
        </style>
    </head>
    <body>
        <h1>Habitica Stats</h1>
        <div class="avatar-container">
            <img src="{avatar_url}" alt="Habitica Avatar" class="avatar">
        </div>
        <div class="stats">
            <p><strong>Level:</strong> {level}</p>
            <p><strong>Health:</strong> {health:.1f} / {max_health:.1f}</p>
        </div>
    </body>
    </html>
    """
    return html

def save_html(html_content, filename="habitica_stats.html"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(html_content)
    print(f"HTML файл сохранен как {filename}")

if __name__ == "__main__":
    try:
        user_data = get_user_data()
        html_content = generate_html(user_data)
        save_html(html_content)
    except Exception as e:
        print(f"Произошла ошибка: {e}")