# opencv-samples

## Setting up for Mac

Assuming the following:

* macOS Sierra
* Using Python 3 (3.6)
* Install Python 3 and OpenCV via Homebrew
    * Homebrew is already installed

### #1 Install Python 3

```console
$ brew install python3
```

### #2 Install OpenCV

```console
$ brew tap homebrew/science
$ brew install opencv3 --with-contrib --with-python3 --without-python
$ cd ~/Library/Python/3.6/lib/python/site-packages
$ ln -s /usr/local/opt/opencv3/lib/python3.6/site-packages/cv2.cpython-36m-darwin.so cv2.so
```
