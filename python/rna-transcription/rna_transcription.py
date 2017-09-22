def to_rna(dna):
    transcription = { 'G' : 'C', 'C' : 'G', 'T' : 'A', 'A' : 'U'}
    rna = ''
    for n in dna:
    	try:
    		rna += transcription[n]
    	except:
    		return ''
    return rna