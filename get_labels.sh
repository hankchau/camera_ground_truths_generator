#!/bin/bash
echo please set appropriate pythonpath
echo PYTHONPATH=/usr/local/bin/python3.7
PYTHONPATH=/usr/local/bin/3.7

echo python3 cam_scrapper.py
echo downloading image data from camera ...
python3 ./cam_scraper.py

echo python3 generate_labels.py
echo generating ground-truths for image data ...
python3 ./generate_labels.py

echo finished generating labels
echo generated folders can be found under '.../darknet/data/'
