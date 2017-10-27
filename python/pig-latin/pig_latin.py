def translate(text):
    def translate_word(word):
        vowels = 'euioa'
        if (word[0] in vowels) or (word[:2] in ['yt','xr']):
            return word + 'ay'
        elif word[:3] in ['squ','thr','sch']:
            return word[3:] + word[:3] + 'ay'
        elif word[:2] in ['qu','th','ch']:
            return word[2:] + word[:2] + 'ay'
        else:
            return word[1:] + word[0] + 'ay'
    return " ".join(list(map(translate_word,text.split())))
