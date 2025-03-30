# **Скачивание видео с Youtube**
**Библиотека** - yt_dlp
**Установка** - pip install yt_dlp

**Запрос ссылки**
```python
link = input("Введите ссылку на видео: ")
```

**Скачивание видео**
```python
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
```
