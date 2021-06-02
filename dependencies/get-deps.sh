#!/bin/bash

#1. Get necessary prerequisites.

sudo apt-get install python3 python3-pip google-chrome-stable
pip3 install selenium

#2. Download and unzip chromedriver. This is needed, so the test scripts will run Google Chrome, and NOT Chromium.
wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip

#3. Move chromedriver to usr/bin/ and allow execution.

sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver

#4. Remove chromedriver_linux64.zip

rm chromedriver_linux64.zip
