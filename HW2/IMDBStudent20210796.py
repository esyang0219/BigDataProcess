#!/usr/bin/python3
import sys
def count_genre(input_file):
	movie_count={}
	with open(input_file, 'r') as f:
		for line in f:
			fields=line.split('::')
			genres=fields[2].split('|')
			for genre in genres:
				genre=genre.strip()
				if genre in movie_count:
					movie_count[genre] += 1
				else:
					movie_count[genre] = 1
	return movie_count

def write_genre(output_file, movie_count):
	with open(output_file, 'w') as f:
		for genre, count in movie_count.items():
			f.write(f"{genre} {count}\n")

if __name__ == '__main__':
	input_file=sys.argv[1]
	output_file=sys.argv[2]

	movie_count = count_genre(input_file)
	write_genre(output_file, movie_count)
