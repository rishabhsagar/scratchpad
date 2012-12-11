for logline in data:
	if "SFIL" in logline and "MSST=Copy step successful." in logline:
		x = re.search(r"STAR=([^|]*).*PNAM=([^|]*).*PNUM=([^|]*).*SFIL=([^|]*).*DFIL=([^|]*).*", logline)
		print x.group(1) + ", " + x.group(2) + ", " + x.group(3) + ", " + x.group(4) + ", " + x.group(5)