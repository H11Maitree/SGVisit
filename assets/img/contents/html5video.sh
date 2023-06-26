#!/bin/sh                        

#  Output file for HTML5 video
#  requirements: ffmpeg .6+
#  usage: ./html5video.sh infile.mp4

target_directory='converted'
file=`basename $1`
filename=${file%.*}
filepath=`dirname $1`
destination="$filepath/$target_directory"

if ! test -d "$destination"
then
  mkdir $destination
fi

# get video resolution
resolution=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 $1)

# Ogg/Theora
ffmpeg -i $1 \
  -acodec libvorbis -ac 2 -ab 192k -ar 44100 \
  -b:v 1024k -s $resolution $destination/$filename.ogv
  
# WebM/vp8
ffmpeg -i $1 \
  -acodec libvorbis -ac 2 -ab 192k -ar 44100 \
  -b:v 1024k -s $resolution $destination/$filename.webm

# MP4/h264
ffmpeg -i $1 \
  -acodec aac -ab 192k \
  -vcodec libx264 \
  -level 21 -refs 2 -b:v 1024k -bt 1024k \
  -threads 0 -s $resolution $destination/$filename.mp4
