# For sending POST request

from flask import Flask, jsonify, request
import requests
from file_checker import main
from time import sleep

resp = requests.post("http://192.168.122.62:5000/check", files={'file' :open('malwares/Ransomware/Locky.exe', 'rb')})
print(resp, resp.json())
