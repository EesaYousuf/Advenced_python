# pip install geocoder folium tk
import tkinter as tk
import geocoder
import folium
import webbrowser
import os
import threading
import time
class LocationTracker:
    def __init__(self, update_interval=10):
        self.update_interval = update_interval
        self.running = False
        self.map_file = "live_location.html"
    def get_location(self):
        g = geocoder.ip('me')
        return g.latlng   

