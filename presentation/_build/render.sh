#!/usr/bin/env bash
# render.sh <html-basename-without-ext> <width> <height>
# Renders presentation/_build/<name>.html -> presentation/images/<name>.png at 2x scale.
set -e
CHROME="/c/Program Files/Google/Chrome/Application/chrome.exe"
BUILD_WIN='C:\Users\vmank\Documents\Code\GBClients\LimbicArc-assessment\limbic-arc-assessment\presentation\_build'
OUT_WIN='C:\Users\vmank\Documents\Code\GBClients\LimbicArc-assessment\limbic-arc-assessment\presentation\images'
name="$1"; w="${2:-1280}"; h="${3:-720}"
"$CHROME" --headless=new --disable-gpu --no-sandbox --hide-scrollbars \
  --force-device-scale-factor=2 \
  --screenshot="$OUT_WIN\\$name.png" --window-size="$w,$h" \
  "$BUILD_WIN\\$name.html" 2>&1 | tail -1
