import comment_extract as CE
import sentimentYouTube as SYT

def main():
	# EXAMPLE VideoId = 'tCXGJQYZ9JA'
	videoId = input("Enter VideoId : ")
	# Fetch the number of comments
	# if count = -1, fetch all comments
	count = int(input("Enter no. of comments to extract : "))
	comments = CE.commentExtract(videoId, count)
	
	# Save comments to a file
	with open("comments.txt", "w", encoding = 'utf-8') as file:
		for comment in comments:
			file.write(comment + "\n---\n")
	
	SYT.sentiment(comments)


if __name__ == '__main__':
	main()
