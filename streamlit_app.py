import os
import sys

# Ensure repository root and App directory are available in Python sys.path
root_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.join(root_dir, 'App')

if root_dir not in sys.path:
    sys.path.insert(0, root_dir)
if app_dir not in sys.path:
    sys.path.insert(0, app_dir)

import nltk

# Ensure all essential NLTK resources are downloaded before running App
for res in ['stopwords', 'punkt', 'punkt_tab', 'averaged_perceptron_tagger', 'averaged_perceptron_tagger_eng', 'wordnet', 'omw-1.4']:
    try:
        nltk.download(res, quiet=True)
    except Exception:
        pass

app_file = os.path.join(app_dir, 'App.py')
os.chdir(app_dir)

# Execute App.py within the active Streamlit script context on every run
with open(app_file, 'r', encoding='utf-8') as f:
    code = compile(f.read(), app_file, 'exec')
    exec(code, globals())
