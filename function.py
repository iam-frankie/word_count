from django.shortcuts import render


def home(request):
    return render(request, 'home.html')  # 获得请求，返回home.html，在setting中已经设置好templatest的位置


def count(request):
    strings = request.GET['text']
    length = len(strings)  # GET-从前端网页获取“text”中的文字，注意要将名字的对应

    word_dict = {}

    for word in strings:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    sortedict = sorted(word_dict.items(), key=lambda w: w[1], reverse=True)

    return render(request, 'count.html',
                  {'length': length, 'strings': strings, 'word': word_dict, "sortedict" : sortedict})
    # 获得统计指令，返回count.html, 显示计算结果
    # render还能向网页中传递一些信息,此处‘length’字符串中传递已经计算出来的length长度
    # {'length': length}通过字典的方式传递
