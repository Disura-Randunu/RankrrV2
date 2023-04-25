import os

baseDir = os.path.abspath(os.path.dirname(__file__))

def get_root_dir():
    return os.path.join(baseDir, '..')

def get_demo_data_file_path():
    return os.path.join(baseDir, '..', 'demo_data.csv')

def get_upoad_path():
    return os.path.join(baseDir, '..', 'uploads')

def get_emph_text_model_path():
    return os.path.join(baseDir, '..', 'model_v9.pkl')