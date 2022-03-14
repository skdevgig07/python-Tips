CHUNK_SIZE = 430

f = open(image_file, 'rb')
chunk = f.read(CHUNK_SIZE)
while chunk: #loop until the chunk is empty (the file is exhausted)
	send_chunk_to_space(chunk)
	chunk = f.read(CHUNK_SIZE) #read the next chunk
f.close()
