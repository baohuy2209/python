from Video import Video 
from Playlist import Playlist 
class Manage_playlist:
	"""docstring for ClassName"""

	def read_video(self):
		title = input("Enter title: ") + "\n"
		link = input("Enter link: ") + "\n"
		video = Video(title, link)
		return video

	def print_video(self,video):
		print("Video title: ", video.title, end="")
		print("Video link: ", video.link, end="")

	def read_videos(self):
		videos = []
		total_video = int(input("Enter how many videos: "))
		for i in range(total_video):
			print("Enter video ", i+1)
			vid = read_video()
			videos.append(vid)
		return videos

	def print_videos(self,videos):
		for i in range(len(videos)):
			print("Video " + str(i+1) + ":")
			self.print_video(videos[i])

	def write_video_txt(self,video, file):
		file.write(video.title)
		file.write(video.link)

	def write_videos_txt(self,videos, file):
		total = len(videos)
		file.write(str(total) + "\n")
		for i in range(total):
			self.write_video_txt(videos[i], file)

	def read_video_from_txt(self,file):
		title = file.readline()
		link = file.readline()
		video = Video(title, link)
		return video

	def read_videos_from_txt(self,file):
		videos = []
		total = file.readline()		
		for i in range(int(total)):
			video = self.read_video_from_txt(file)
			videos.append(video)
		return videos

	def read_playlist(self):
		playlist_name = input("Enter playlist name: ") + "\n"
		playlist_description = input("Enter playlist description: ") + "\n"
		playlist_rating = input("Enter rating (1-5): ") + "\n"
		playlist_videos = self.read_videos()
		playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
		return playlist

	def write_playlist_txt(self,playlist):
		with open("data.txt", "w") as file:
			file.write(playlist.name)
			file.write(playlist.description)
			file.write(playlist.rating)
			self.write_videos_txt(playlist.videos, file)
		print("Successfully write playlist to txt")

	def read_playlist_from_txt(self):
		with open("data.txt", "r") as file:
			playlist_name = file.readline()
			playlist_description = file.readline()
			playlist_rating = file.readline()
			playlist_videos = self.read_videos_from_txt(file)
		playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
		return playlist

	def print_playlist(self,playlist):
		print("-------")
		print("Playlist name: " +  playlist.name, end="")
		print("Playlist description: " +  playlist.description, end="")
		print("Playlist rating: " +  playlist.rating, end="")
		print_videos(playlist.videos)
	def select_in_range(self,prompt, min, max):
		choice = input(prompt)
		while not choice.isdigit() or int(choice) < min or int(choice) > max:
			choice = input(prompt)

		choice = int(choice)
		return choice

	def play_video(self,playlist):
		print_videos(playlist.videos)
		total = len(playlist.videos)

		choice = self.select_in_range("Select a video (1," + str(total) + "): " , 1,total)
		print("Open video: " + playlist.videos[choice-1].title + " - " + playlist.videos[choice-1].link, end ="")
		playlist.videos[choice-1].open()

	def add_video(self,playlist):
		print("Enter new video information:")
		new_video_title = input("Enter new video title: ") + "\n"
		new_video_link =  input("Enter new video link: ") + "\n"
		new_video = Video(new_video_title, new_video_link)
		playlist.videos.append(new_video)
		return playlist

	def update_playlist(self,playlist):
		# Update name / description / rating
		print("Update playlist?")
		print("1. Name")	
		print("2. Description")	
		print("3. Rating")	

		choice = select_in_range("Enter what you want to update (1-3):", 1,3)
		if choice == 1:
			new_playlist_name = input("Enter new name for playlist: ") + "\n"
			playlist.name = new_playlist_name
			print("Updated Successfully !")
			return playlist
		if choice == 2:
			new_playlist_description = input("Enter new description for playlist: ") + "\n"
			playlist.description = new_playlist_description
			print("Updated Successfully !")
			return playlist
		if choice == 3:
			new_playlist_rating = str(self.select_in_range("Enter new rating (1-5): ",1,5)) + "\n"
			playlist.rating = new_playlist_rating
			print("Updated Successfully !")
			return playlist

	def remove_video(self,playlist):
		self.print_videos(playlist.videos)
		choice = self.select_in_range("Enter video you want to delete: ",1,len(playlist.videos))
		new_video_list = []
		# del playlist.videos[choice-1]
		for i in range(len(playlist.videos)):
			if i == choice-1:
				continue
			new_video_list.append(playlist.videos[i])

		playlist.videos = new_video_list

		print("Delete Successfully !!!")
		return playlist		