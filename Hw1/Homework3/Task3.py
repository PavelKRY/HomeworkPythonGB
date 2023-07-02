import string

text = "termio (7)           - System V terminal driver interface " \
       "Test::Lintian (3)    - - Check Lintian files for issues" \
       "xqxdecode (1)        - Decode a XQX stream into human readable form." \
       "xrandr (1)           - primitive command line interface to RandR extension" \
       "xreader-previewer (1) - show print preview for a document" \
       "xsetpointer (1)      - set an X Input device as the main pointer" \
       "xsubpp (1)           - compiler to convert Perl XS code into C code " \
       "xvinfo (1)           - Print out X-Video extension adaptor information"
text = text.translate(str.maketrans('', '', string.punctuation)).lower().split()

res = {}
for letter in text:
    res[letter] = res.get(letter, 0) + 1

srt = [i for i, j in sorted(res.items(), key=lambda item: item[1], reverse=True)[:10]]
print(srt)