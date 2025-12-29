#!/usr/bin/env python3
"""
Development server with live reload.
Watches for changes and rebuilds the site automatically.
"""

import http.server
import socketserver
import threading
import time
import sys
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from build import SiteBuilder


class RebuildHandler(FileSystemEventHandler):
    """Handler that rebuilds the site when files change."""

    def __init__(self, builder: SiteBuilder):
        self.builder = builder
        self.last_build = 0
        self.debounce = 1  # seconds

    def on_any_event(self, event):
        # Ignore changes to output directory
        if 'output' in event.src_path:
            return

        # Debounce rapid changes
        now = time.time()
        if now - self.last_build < self.debounce:
            return

        print(f"\n🔄 Change detected: {event.src_path}")
        try:
            self.builder.build()
            self.last_build = now
            print("✅ Rebuild complete!")
        except Exception as e:
            print(f"❌ Build error: {e}")


def serve(port: int = 8000):
    """Serve the output directory."""
    output_dir = Path("output")

    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(output_dir), **kwargs)

        def log_message(self, format, *args):
            # Suppress log messages
            pass

    try:
        with socketserver.TCPServer(("", port), Handler) as httpd:
            print(f"📡 Server running at http://localhost:{port}/")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 Shutting down server...")
        sys.exit(0)


def watch_and_serve(port: int = 8000):
    """Build the site, watch for changes, and serve."""
    # Initial build
    builder = SiteBuilder()
    builder.build()

    # Start file watcher
    event_handler = RebuildHandler(builder)
    observer = Observer()

    # Watch content, templates, and static directories
    for directory in ['content', 'templates', 'static']:
        if Path(directory).exists():
            observer.schedule(event_handler, directory, recursive=True)
            print(f"👀 Watching {directory}/ for changes...")

    observer.start()

    # Start server in main thread
    try:
        serve(port)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Development server with live reload")
    parser.add_argument("--port", type=int, default=8000, help="Port to serve on (default: 8000)")
    args = parser.parse_args()

    watch_and_serve(args.port)
