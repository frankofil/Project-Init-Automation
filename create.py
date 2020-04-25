import sys


def main():
    public = False
    projectName = sys.argv[1]
    if len(sys.argv) > 2 and sys.argv[2] == "-public":
        public = True

    print(projectName)
    print(public)


if __name__ == '__main__':
    main()
