#!/usr/bin/python3
""" Module __init__
    This module creates a unique FileStorage instance
    for our application
"""
from engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
