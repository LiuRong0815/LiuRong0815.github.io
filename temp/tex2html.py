#! /usr/bin/python

# 将 tex 文件转化为 md 文件，批量替换格式

# TODO: 修改 includegraphics
# TODO: 修改 myindex
# TODO: 修改 \qquad ??

# TODO: print('convert tex files to md files.\n')

import os,re

# tex 文件名列表
texFileNames = []

# 当前目录文件列表
fileList = os.listdir()

# 保存 tex 文件名
for files in fileList:
    
    matchFile = re.match( r'(.*)\.(.*)', files)

    # 过滤文件夹或没有后缀的文件
    if(matchFile == None):
        continue
    
    fileName = matchFile.group(1) # 文件名
    fileExt  = matchFile.group(2) # 后缀
    
    if(fileExt == 'tex'):
        texFileNames.append(fileName) # tex 文件名列表

# 若无 tex 文件，则退出
texFileNum = len(texFileNames)
if(texFileNum == 0):
    print("Sorry, no tex files!")
    quit()

#开始转换，并准备必要的数据
for num in range(0,texFileNum):

    fptemp = open(texFileNames[num]+'.temp','w') # 新建 temp
    lines = open(texFileNames[num]+'.tex','r').readlines()  #读入每一行

    # 替换各种环境和文字
    for oneline in lines:
            
        # ~
        oneline = oneline.replace('~', ' ')
        
        # <
        oneline = oneline.replace('<', '< ')
        oneline = oneline.replace('<  ', '< ')

        # ``''
        oneline = oneline.replace(' ``', '“')
        oneline = oneline.replace("'' ", '”')
        oneline = oneline.replace('``', '“')
        oneline = oneline.replace("''", '”')

        # mathbb
        oneline = oneline.replace('mathbb', 'mathbf')

        # example
        oneline = oneline.replace('\\begin{example}\n', \
            '<myexample>\n<p>')
        oneline = oneline.replace('\\end{example}', '</p>\n</myexample>')

        # solution
        oneline = oneline.replace('\\beginsolution', \
            '<mysolution>\n    <p>')
        oneline = oneline.replace('\\endsolution', '</p>\n</mysolution>')
        oneline = oneline.replace('\\begin{solution}\n', \
            '<mysolution>\n    <p>')
        oneline = oneline.replace('\\end{solution}', '</p>\n</mysolution>')
        
        # proof
        oneline = oneline.replace('\\begin{proof}\n', \
            '<myproof>\n    <p>')
        oneline = oneline.replace('\\end{proof}', '</p>\n</myproof>')

        # remark
        oneline = oneline.replace('\\begin{remark}\n',\
            '<myremark>\n    <p>')
        oneline = oneline.replace('\\end{remark}', '</p>\n</myremark>')
        
        # exercise
        oneline = oneline.replace('\\begin{exercise}\n', \
            '<myexercise>\n    <p>')
        oneline = oneline.replace('\\end{exercise}', '</p>\n</myexercise>')

        # align*
        oneline = oneline.replace('\\begin{align*}',\
            '\\[\\begin{aligned}')
        oneline = oneline.replace('\\end{align*}', '\\end{aligned}\]')
        
        # center
        oneline = oneline.replace('\\begin{center}', '<center>')
        oneline = oneline.replace('\\end{center}', '</center>')
        
        # # figs
        # figName = re.search('\\includegraphics.*\{(.*)\}', oneline)
        # if(figName):
        #     oneline = '  <embed src="/figs/' + figName.group(1) + '.svg">\n'
        #     fp.write(oneline)
        #     continue
        
        # # item
        # myItem = re.search( r'\\item', oneline)
        # if(myItem):
        #     # 先替换开头的 \item，再去掉结尾的换行符
        #     oneline = oneline.replace('\\item', '<p>').rstrip()
        #     oneline += '</p>\n'  # 补上换行符
        #     fp.write(oneline)
        #     continue
        
        # myemph
        myemph = re.search( r'(.*)\\myemph\{(.*?)\}(.*)', oneline)
        if(myemph):
            oneline = myemph.group(1) + '<strong>' \
                + myemph.group(2) + '</strong>'+ myemph.group(3)
        
        # 各段加段落标签
        realLine = oneline.strip() # 删掉开头结尾的空字符
        if( 0 == len(realLine) ):
            oneline = '</p>\n<p>'

        # 逐行写入
        fptemp.write(oneline)
    fptemp.close()

    fpmd = open(texFileNames[num]+'.md','w') # 新建 md
    lines = open(texFileNames[num]+'.temp','r').readlines()  #读入每一行

    # 替换各种环境和文字
    for oneline in lines:

        # 删除 <p> 后的空格
        oneline = oneline.replace('<p>    ', '<p>')
        oneline = oneline.replace('<p>   ', '<p>')
        oneline = oneline.replace('<p>  ', '<p>')
        oneline = oneline.replace('<p> ', '<p>')
        oneline = oneline.replace('<p>\n', '<p>')
        # 逐行写入
        fpmd.write(oneline)
    fptemp.close()

for file_name in os.listdir("./"):
    if file_name.endswith('.temp'):
        os.remove("./" + file_name)

print('finished converting ' + str(texFileNum) + ' tex files!')
