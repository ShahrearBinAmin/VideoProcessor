from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os

def cut(filename,moving_list,out_directory):

    for idx,start_end in enumerate(moving_list):
        ffmpeg_extract_subclip(filename,start_end[0],start_end[1],targetname=os.path.join(out_directory,str(idx)+".mp4"))


if __name__=='__main__':
    file_name="/home/shanto/Desktop/1.mp4"
    out_dir="/home/shanto/Desktop/out"
    lst=[(1,30),(40,60)]
    cut(file_name,lst,out_dir)