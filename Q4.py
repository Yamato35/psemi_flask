with open('/Users/condor0305/Desktop/名称未設定フォルダ/研究室/Python/課題/data.txt', 'r') as f:
    content = f.read().split()
    content.sort()

with open('/Users/condor0305/Desktop/名称未設定フォルダ/研究室/Python/課題/data2.txt', 'w') as fp:
    print(content,file = fp)