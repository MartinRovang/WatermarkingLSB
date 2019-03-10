# Watermarking using LSB


## Demo
<<<<<<< HEAD:README.md
    WATERMARKED IMAGE                                   EXTRACTED IMAGE
=======

    WATERMARKED IMAGE                                      EXTRACTED IMAGE
>>>>>>> 00d81af0534ff8da9eeb1d43151bd5cc8e3bc358:release/README.md
![Watermarked](https://i.imgur.com/TK6uXjX.png)


# How to use
Watermark image:<br/>
```python main.py -w image.jpg watermark.jpg```<br/>
Extract watermark:<br/>
```python main.py -e watermarkedimage.png```


# Dependencies
* Numpy<br/>
* Matplotlib<br/>
* PIL

### Note

Since LSB is very fragile any compression like jpg etc. will most likely break the watermark.

