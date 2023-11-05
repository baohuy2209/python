from Manage_playlist import Manage_playlist

if __name__ == '__main__': 

	mp = Manage_playlist()
	try:
		playlist = read_playlist_from_txt()
		print("Loaded data Successfully !!!")
	except:
		print("Welcome first user !!!")		

	while True:
		print("Main Menu:")
		print("-----------------------------")
		print("| Option 1: Create playlist |")
		print("| Option 2: Show playlist   |")
		print("| Option 3: Play a video    |")
		print("| Option 4: Add a video     |")
		print("| Option 5: Update playlist |")
		print("| Option 6: Remove video    |")
		print("| Option 7: Save and Exit   |")
		print("-----------------------------")
		choice = mp.select_in_range("Select an option (1-7):", 1, 7)
		if choice == 1:
			playlist = mp.read_playlist()	
			input("\nPress Enter to continue.\n")	
		elif choice == 2:
			mp.print_playlist(playlist)
			input("\nPress Enter to continue.\n")	
		elif choice == 3:
			mp.play_video(playlist)	
			input("\nPress Enter to continue.\n")	
		elif choice == 4:
			playlist = mp.add_video(playlist)	
			input("\nPress Enter to continue.\n")
		elif choice == 5:
			playlist = mp.update_playlist(playlist)	
			input("\nPress Enter to continue.\n")
		elif choice == 6:
			playlist = mp.remove_video(playlist)	
			input("\nPress Enter to continue.\n")
		elif choice == 7:
			mp.write_playlist_txt(playlist)
			input("\nPress Enter to continue.\n")	
			break
		else:
			print("Wrong Input, Exist.")
			break