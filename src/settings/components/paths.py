import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# GDAL_LIBRARY_PATH = 'venv/Lib/site-packages/osgeo/gdal304.dll'

# Static files (CSS, JavaScript, images)
STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "hud" / "components",
]

# STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
CKEDITOR_UPLOAD_PATH = "uploads/"
PROTECTED_MEDIA_ROOT = os.path.join(BASE_DIR, 'protected')
