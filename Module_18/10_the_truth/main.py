def revert_text(line, key):
    step_1 = ''
    step_2 = ''
    for F_word in line:
        if F_word in word:
            num = word.find(F_word)
            step_1 += word[num - key]
        else:
            step_1 += F_word

    place_index = 3

    for words in step_1.split(' '):
        new_word = ''
        for index in range(len(words)):
            new_word += (words[index - place_index % len(words)])
        if new_word.endswith('/'):
            place_index += 1
        step_2 += new_word + ' '
    answer_text = step_2.replace('/', '\n')

    return answer_text

text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cf' \
       'uufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf d' \
       'btft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt f' \
       'oumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip f' \
       'c pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf ' \
       'sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqm' \
       'f tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftq' \
       'bdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'

word = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = "',-*!"

answer_text = revert_text(text, 1)
answer_text = answer_text.replace('(', "'").replace('+', '*').replace('-', ',').replace('..', '--').replace('"', '!')
print(answer_text)
