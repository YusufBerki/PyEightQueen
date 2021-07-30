import os

DATA_DIR = 'data'
RESULTS_DIR = 'results'
IMG_DIR = os.path.join(DATA_DIR, 'img')
PIECES_DIR = os.path.join(IMG_DIR, 'pieces')

COLOR_SCHEME = {
    0: {
        1: (0, 0, 0),
        0: (255, 255, 255),
    },
    1: {
        0: (181, 217, 240),
        1: (99, 136, 181)

    }
}

PIECES = {
    "queen": {"path": os.path.join(PIECES_DIR, 'queen.png')}
}


def make_dirs(path):
    os.makedirs(path, exist_ok=True)
    return path
