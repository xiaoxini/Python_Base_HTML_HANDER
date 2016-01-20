# coding=utf-8

if __name__ == '__main__':
    import handers, markup
    import sys
    handler = handers.HTMLRenderer()
    parser = markup.BasicTextParse(handler)
    # f = open('.//HANDER//test01.txt', 'r')
    f = open('test01.txt', 'r')
    oldstdout = sys.stdout          # 重定向stdout
    sys.stdout = open('test02.html', 'w')
    parser.parse(f)
    sys.stdout.close()          # 记得关闭文件
    sys.stdout = oldstdout
    f.close()
