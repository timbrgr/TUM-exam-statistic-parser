import os


def parse_tum():
    pass


if __name__ == "__main__":
    import csv
    import json

    methods = {
        parse_tum
    }

    if not os.path.isdir("/data"):
        raise ValueError("No /data/ folder exists. Please create /data/ folder and put your course statistics there.")

    if not os.path.isdir("results"):
        os.mkdir("results")

    for method in methods:
        name = method.__name__.split("_")[1]
        print("Starting [{0}]...".format(name))
        print()
        result = method()
        outfile = open("./results/{0}.csv".format(name), "w+")
        writer = csv.writer(outfile)
        for row in json.loads(result.read()):
            writer.writerow()
        print()
        print("Finished [{0}]".format(name))
        print()
