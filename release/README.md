# Watermarking using LSB


## Demo

![Watermarked](https://i.imgur.com/TK6uXjX.png)


# How to use
Watermark image:<br/>
```python main.py -w image.jpg watermark.jpg```<br/>
Extract watermark:<br/>
```python main.py -e watermarkedimage.png```

### Note

Since LSB is very fragile any compression like jpg etc. will most likely break the watermark.

