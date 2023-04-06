
import googletrans

trn = googletrans.Translator()
tr = trn.translate(text="Привет!", dest='english', src='ru')


print(tr.text)
