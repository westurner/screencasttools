#!/bin/bash -x

infile="${HOME}/example.mp4"
outfile="${infile}.trimmed.mp4"

ffmpeg -i "${infile}" -vcodec copy -ss 00:00:00.000 -t 00:01:00.000 "${outfile}"
