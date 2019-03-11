#!/usr/bin/env python3

import pathlib
import shlex
import subprocess
import sys

import logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger()

def shlex_quote_always(str_):
    _str = shlex.quote(str_)
    if not _str.startswith("'"):
        return "'%s'" % _str
    else:
        return _str

def concat_videos(files, output_filename=None, output_dest=None):
    if output_dest is None:
        output_dest = '.'
    if output_filename is None:
        filenames = [str(pathlib.Path(p).name) for p in files]
        output_filename = str(
            pathlib.Path(output_dest) / ("%s.mp4" % "__".join(filenames)))
    filelist_txt = '_filelist.txt'
    with open(filelist_txt, 'w') as _file:
        for filename in files:
            line = "file %s" % shlex_quote_always(filename)
            log.info(line)
            _file.write(line)
            _file.write("\n")
    #command="ffmpeg -f concat -i mylist.txt -c copy output.mp4"
    command = [
        "ffmpeg",
        "-f", "concat",
        "-safe", "0",
        "-i", filelist_txt,
        "-c", "copy",
        output_filename]
    log.info(command)
    subprocess.call(command)
    return output_filename

def main(argv=None):
    argv = argv if argv is not None else []
    files = argv
    if not files:
        raise Exception("You must pass files as args")
    output_filename = concat_videos(files)
    print(f"output_filename: {repr(output_filename)}")
    return 0


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
