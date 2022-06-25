#!/usr/bin/python3
import argparse, logging, os
import patoolib

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

def create_parser():
    parser = argparse.ArgumentParser(description="extracts rar if torrent is rar")

    parser.add_argument("-p", "--path", required=True)
    parser.add_argument('-o', "--outfile", required=False)

    return parser

def main():
    parser = create_parser()
    try:
        args = parser.parse_args()
    except:
        parser.print_usage()
        return
    # list contents in path, is there a rar file in there?
    torrent_contents = os.listdir(args.path)
    for file_name in torrent_contents:
        if file_name.endswith('.rar'):
            # unrar it
            full_path = os.path.abspath(file_name)
            logging.info("find rar, extracting to same path ...")
            #patoolib.extract_archive(full_path, outdir=args.path)
        else:
            logging.info("no rar file found. going to sleep zzzZZZzz.")
        
if __name__ == "__main__":
    main()
