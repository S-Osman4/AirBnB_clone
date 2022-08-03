#!/bin/usr/env python3
"""Module for FileStorage (Create a unique instance for my application)."""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
