#!/usr/bin/python3
def count_movie_genre(input_file):
	genre_count={}
	with open(input_file, 'r') as f:
		for line in f:
			fields=line.split('::')
			genres=fields[2].split('|')
			for genre in genres:
				genre=genre.strip()
				if genre in genre_count:
					genre_count[genre] += 1
				else:
					genre_count[genre] = 1
	return genre_count

def write_genre(output_file, genre_count):
	with open(output_file, 'w') as f:
		for genre, count in genre_count.items():
			f.write(f"{genre} {count}\n")

if __name__ == '__main__':
	import sys
	input_file=sys.argv[1]
	output_file=sys.argv[2]

	genre_count = count_movie_genre(input_file)
	write_genre(output_file, genre_count)
