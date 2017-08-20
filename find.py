import mmap

def find(file,term):
	f = open(file)
	s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
	if s.find(term) != -1:
		return	True