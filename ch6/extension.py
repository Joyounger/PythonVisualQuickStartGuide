
def get_ext(fname):
	""" Return the extension of file name
	"""
	dot = fname.rfind('.')
	if dot == -1:  # fname中没有
	  return ''
	else:
      return fname[dot + 1 :]