#!/bin/bash
# Ship the design language from this home to every project's mirror, then verify the mirrors by SHA-256.
# The home is the only place the language is written; a mirror is a byte-identical copy that the ship overwrites
# (اقرأني.md, "الشحن"). Frozen examples (design-language/examples/) stay home: they are heavy and not read by projects.
#
#   bash tools/ship.sh check    reads only: lists every mirror file that differs from the home or is missing
#   bash tools/ship.sh ship     copies, then runs the check; nothing is ever deleted in a mirror
#
# Run it in Jo's Mac terminal, never while a Claude Code session is working in a mirror's repository; each project then
# commits its mirror in its own round. macOS bash 3.2 and BSD tools; no associative arrays.
set -euo pipefail
HOME_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PROJECTS="$(cd "$HOME_DIR/.." && pwd)"
GUIDE="DESIGN_LANGUAGE_BUILD_GUIDE.md"

# one mirror a line: <folder under Projects>|<what it receives: guide, or guide+assets>
MIRRORS="بوابة نايف القدرات/naif-gate-app/Lessons and Guides|guide+assets
بوابة نايف القدرات/Lessons and Guides|guide
StandardsHub v4/docs/design|guide+assets
CBAHI PHC/_docs/03_build-guides|guide+assets"

asset_files() {
  (cd "$HOME_DIR" && find design-language -type f ! -path 'design-language/examples/*' ! -name .DS_Store | LC_ALL=C sort)
}

check() {
  local bad=0 dir kind dest f
  while IFS='|' read -r dir kind; do
    dest="$PROJECTS/$dir"
    if [ ! -d "$dest" ]; then echo "MISSING FOLDER  $dir"; bad=1; continue; fi
    for f in "$GUIDE" $( [ "$kind" = "guide+assets" ] && asset_files | tr '\n' ' ' ); do
      if [ ! -f "$dest/$f" ]; then echo "missing   $dir/$f"; bad=1
      elif ! cmp -s "$HOME_DIR/$f" "$dest/$f"; then echo "differs   $dir/$f"; bad=1; fi
    done
  done <<< "$MIRRORS"
  if [ "$bad" = 0 ]; then echo "every mirror matches the home ($(asset_files | wc -l | tr -d ' ') asset files + the guide)"; fi
  return $bad
}

ship() {
  local dir kind dest f
  while IFS='|' read -r dir kind; do
    dest="$PROJECTS/$dir"
    [ -d "$dest" ] || { echo "no folder: $dir"; exit 1; }
    cp "$HOME_DIR/$GUIDE" "$dest/$GUIDE"
    if [ "$kind" = "guide+assets" ]; then
      asset_files | while IFS= read -r f; do mkdir -p "$dest/$(dirname "$f")"; cp "$HOME_DIR/$f" "$dest/$f"; done
    fi
    echo "shipped   $dir ($kind)"
  done <<< "$MIRRORS"
  check
}

case "${1:-}" in
  check) check ;;
  ship) ship ;;
  *) echo "usage: bash tools/ship.sh check|ship"; exit 2 ;;
esac
