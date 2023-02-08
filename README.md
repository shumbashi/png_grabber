# PNG Grabber

PNG Grabber is a sample python project that will grab all PNG images from a website and save them to a directory.

## Installation

Download a packaged binary from the "Release" page or clone this repository and run the file png_grabber directly.

### Binary Package

```
cd ~
wget https://github.com/shumbashi/png_grabber/releases/download/v1.0/png_grabber_linux_amd64 -O png_grabber_v1.0_linux_amd64
sudo mv png_grabber_v1.0_linux_amd64 /usr/local/bin/png_grabber
chmod +x /usr/local/bin/png_grabber
```

### Clone Repository

```
git clone https://github.com/shumbashi/png_grabber.git
cd png_grabber
pip3 install --user -r requirements.txt
```

## Usage

```
Usage: png_grabber [OPTIONS]

  PNG Grabber is a utility program that will grab all PNG images from a
  website and save them to a directory. Developed by: Ahmed Shibani
  (@shumbashi)[https://github.com/shumbashi]

Options:
  -u, --url TEXT            URL to the website you want to grab PNG images
                            from  [required]
  -o, --output TEXT         Output directory to save the images to  [required]
  --username TEXT           Username to authenticate with
  --password TEXT           Password to authenticate with
  --verbose / --no-verbose  Enable verbose output
  --help                    Show this message and exit.
```