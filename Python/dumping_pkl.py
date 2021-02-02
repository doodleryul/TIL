
def dumping_pkl(filePath, outFilename, files):
    import os, pickle
    dumpingPath = os.path.join(filePath, outFilename)
    print("Dumping at..", dumpingPath)
    with open(dumpingPath, 'wb') as outp:
        pickle.dump(files, outp, -1)
