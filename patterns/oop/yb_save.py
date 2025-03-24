from pytube import YouTube

# Ссылка на видео
video_url = "https://www.youtube.com/watch?v=jJ8WxK5na4s"

# Создание объекта YouTube
yt = YouTube(video_url)

# Получение информации о видео
print("Название:", yt.title)
print("Описание:", yt.description)
print("Длительность:", yt.length, "секунд")
print("Автор:", yt.author)

# Скачивание видео
stream = yt.streams.filter(progressive=True, file_extension="mp4").first()
stream.download(output_path="downloads")
print("Видео скачано!")