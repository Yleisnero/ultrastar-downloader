from pytube import YouTube 
import os 
  
# # url input from user 
# yt = YouTube( 
#     str(input("Enter the URL of the video you want to download: \n>> "))) 

yt = YouTube('https://www.youtube.com/watch?v=eVTXPUF4Oz4')

print(yt.thumbnail_url)

stream = yt.streams.get_by_itag(22)
stream.download()

# video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

# # Save the video to a file
# save_path = os.path.join(os.getcwd(), yt.title + ".mp4")
# os.rename(video, save_path)
  
# # result of success 
# print(yt.title + " has been successfully downloaded.")