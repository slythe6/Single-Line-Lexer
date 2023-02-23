import re

def singleLineLexer(input):
    output = []
    tokenList = {r'\b(if|else|int|float)(?=\s|\t)': 'key',
                 r'[A-Za-z]+\d+|[A-Za-z]+': 'id',
                 r'[=+>*]': 'op',
                 r'^\d+(?![\d+\.])': 'lit', #int literal
                 r'\d+\.\d+': 'lit', #float literal
                 r'[():\";]': 'sep',
                 r'[\t]+|[ ]+': 'space'}

    temp = input

    while len(temp) != 0:
        for x in tokenList:
            token = re.match(x, temp)
            if token:
                if tokenList[x] == 'space':
                    pos = token.end()
                    temp = temp[pos:]
                elif tokenList[x] == 'sep' and temp[0] == '\"':
                    output.append('<' + tokenList[x] + ',' + token.group() + '>')
                    pos = token.end()
                    temp = temp[pos:]
                    regExStr = re.match(r'^(.)+?(?=\")', temp)
                    if regExStr:
                        output.append('<' + 'lit' + ',' + regExStr.group() + '>')
                        pos = regExStr.end()
                    output.append('<' + tokenList[x] + ',' + token.group() + '>')
                    pos += 1
                    temp = temp[pos:]
                else:
                    output.append('<' + tokenList[x] + ',' + token.group() + '>')
                    pos = token.end()
                    temp = temp[pos:]

    return 'Output <type,token> list: ', output


if __name__ == '__main__':
    print(singleLineLexer("int	A1=5"))
    print(singleLineLexer("float BBB2	=1034.2"))
    print(singleLineLexer("float	cresult	=	A1	+BBB2	*	BBB2"))
    print(singleLineLexer("if	(cresult	>10):"))
    

