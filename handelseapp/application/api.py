from flask import Flask, request, render_template
import pandas as pd
import requests
import json
from application import func

app = Flask(__name__)


