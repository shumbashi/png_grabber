#!/usr/bin/python3

import os
import click
import requests
from bs4 import BeautifulSoup

def verbose_print(message):
    if VERBOSE:
      click.secho(message, fg='yellow')
    return

@click.command()
@click.option('-u', '--url', required=True, help='URL to the website you want to grab PNG images from')
@click.option('-o', '--output', required=True, help='Output directory to save the images to')
@click.option('--username', required=False, help='Username to authenticate with')
@click.option('--password', required=False, help='Password to authenticate with')
@click.option('--verbose/--no-verbose', default=False, help="Enable verbose output")

def main(url,output,username,password,verbose):
    """
    PNG Grabber is a utility program that will grab all PNG images from a website and save them to a directory.
    Developed by: Ahmed Shibani (@shumbashi)[https://github.com/shumbashi]
    """
    global VERBOSE
    VERBOSE = verbose
    if verbose:
        click.secho('[!] Verbose mode is on', fg='yellow')

    # Check if the output directory exists, if not, create it
    verbose_print('[!] Checking if output directory exists')
    if not os.path.exists(output):
        verbose_print('[!] Output directory does not exist, creating it')
        os.makedirs(output)

    # Grab the HTML from the URL, if username and Ppassword are provided, we'll use them to authenticate
    click.secho('[+] Fetching HTML from URL: %s' % url, fg='green')
    if username and password:
        # Use Basic Authentication
        verbose_print('[!] Using username and password for Basic Authentication')
        # 'python requests' supports following redirects by default, no changes are required
        r = requests.get(url, auth=(username, password))
    else:
        r = requests.get(url)

    if r.status_code == 200:
      verbose_print('[!] Successfully fetched HTML from URL: %s' % url)
    else:
      click.secho('[!] Failed to fetch HTML from URL: %s %s' % (r.status_code, r.reason), fg='red')
      return
    
    # Parse the HTML using BeautifulSoup
    verbose_print('[!] Parsing HTML')
    soup = BeautifulSoup(r.text, 'html.parser')

    # Grab all the images from the HTML
    verbose_print('[!] Grabbing all images from HTML')
    images = soup.find_all('img')
    verbose_print('[!] Found %s images' % len(images))

    # Counter for the number of PNG images we find
    count = 0
    if len(images) > 0:
      # Loop through the images and save them to the output directory if they are PNGs
      verbose_print('[!] Checking images for PNGs')
      for image in images:
          try:
            # Grab the image URL
            image_url = image['src']
            # Grab the image extension
            image_extension = image_url.split('.')[-1]
            # Check if the image is a PNG, convert to lowercase
            if image_extension.lower() == 'png':
              verbose_print('[!] Found PNG image: %s' % image_url)
              # Increment the counter
              count += 1
              # Check if the image URL is relative
              if not image_url.startswith('http'):
                verbose_print('[!] Found relative image URL: %s' % image_url)
                # Make the image URL absolute
                image_url = url + image_url
                verbose_print('[!] Made image URL absolute: %s' % image_url)

              # Grab the image name
              image_name = image_url.split('/')[-1]
              # Grab the image data
              verbose_print('[!] Grabbing image data')
              image_data = requests.get(image_url).content
              # Save the image to the output directory
              verbose_print('[!] Saving image to directory "%s"' % output)
              with open(output + '/' + image_name, 'wb') as handler:
                  handler.write(image_data)
          except Exception as e:
            verbose_print('[!] Failed to grab image: %s' % e)
      if count == 0:
          click.secho('[!] No PNG images found', fg='red')
      else:
          click.secho('[!] Grabbed %s PNG images' % count, fg='green')
    else:
      click.secho('[!] No images found', fg='red')

if __name__ == '__main__':
    main()