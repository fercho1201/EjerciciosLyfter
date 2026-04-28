def alphabetically_sort_files(input_path, output_path):
	with open(input_path) as file:
		songs = [line.strip() for line in file if line.strip()]
		
		sorted_songs = sorted(songs, key=str.lower)

		with open(output_path, 'w') as new_file:
				new_file.write('\n'.join(sorted_songs))


	print(f'your file has been sorted, and save to: {output_path}')



input_path = r'C:\\Users\\ferch\\Documents\\Academy_Python\\file_management_exercise\\Songs.txt'
output_path = r'C:\\Users\\ferch\\Documents\\Academy_Python\\file_management_exercise\\Sorted_songs.txt'

alphabetically_sort_files(input_path,output_path)