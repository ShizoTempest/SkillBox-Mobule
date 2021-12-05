def encrypt(line, key):
    answer = ''
    for i in line:
        if i in word:
            num = word.find(i)
            answer = answer + word[num - key]
        else:
            answer = answer + i
    return answer

text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jn' \
       'qm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbuf' \
       'e/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/e' \
       'f uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up ' \
       'csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tip' \
       'vme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui' \
       ' dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip' \
       ' fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmui' \
       'pvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud ' \
       'xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu' \
       '++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec ' \
       '/jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe' \
       ' jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp t' \
       'f"uip'
word = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
print("i - ", 1, " -------", encrypt(text, 1))


# TODO Доделай
