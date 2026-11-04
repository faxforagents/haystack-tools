"""Disable telemetry and keep configuration writes inside the checkout."""

import os
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
os.environ["HAYSTACK_TELEMETRY_ENABLED"] = "false"
os.environ["HAYSTACK_AUTO_TRACE_ENABLED"] = "false"
os.environ["XDG_CONFIG_HOME"] = str(_ROOT / ".coding-agent/tmp/config")
os.environ["XDG_CACHE_HOME"] = str(_ROOT / ".coding-agent/tmp/cache")
