import os

def search_files():
    directory = "C:/Users/данча/Downloads"
    files = []
    ras = []
    files += os.listdir(directory)
    for file in files:
        ras += os.path.splitext(file)

    return ras
def main():
    list = find
    print(search_files())




if __name__ == '__main__':
    main()