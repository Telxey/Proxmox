#!/bin/bash

PIDFILE="/run/filebrowser.pid"
LOGFILE="/var/log/filebrowser.log"

case "$1" in
    start)
        echo "Starting FileBrowser..."
        if [ -f "$PIDFILE" ]; then
            echo "FileBrowser is already running."
            exit 1
        fi

        # Start the daemon
        /usr/local/bin/filebrowser -r / --port 8080 >> "$LOGFILE" 2>&1 &
        echo $! > "$PIDFILE"
        echo "FileBrowser started with PID $(cat "$PIDFILE")."
        ;;

    stop)
        echo "Stopping FileBrowser..."
        if [ ! -f "$PIDFILE" ]; then
            echo "FileBrowser is not running."
            exit 1
        fi

        # Stop the daemon
        kill "$(cat "$PIDFILE")"
        rm -f "$PIDFILE"
        echo "FileBrowser stopped."
        ;;

    status)
        if [ -f "$PIDFILE" ]; then
            echo "FileBrowser is running with PID $(cat "$PIDFILE")."
        else
            echo "FileBrowser is stopped."
        fi
        ;;

    *)
        echo "Usage: $0 {start|stop|status}"
        exit 1
        ;;
esac
