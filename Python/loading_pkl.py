def loading_pkl(filePath, filename):
    import os, pickle
    loadingPath = os.path.join(filePath, filename)
    print("Loading at..", loadingPath)
    with open(loadingPath, 'rb') as f:
        p = pickle.load(f)
    return p
