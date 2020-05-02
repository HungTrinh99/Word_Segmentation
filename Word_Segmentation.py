import re

def Word_Segmentation(inputString):
    #parameter tokens: Mảng lưu trữ chuỗi đầu vào sau khi Split
    tokens=inputString.split(" ")

    #parameter dictionary: Lưu trư data xong khi chuẩn hóa dưới dạng chuối
    corpus=""

    #Mảng result lưu kết quả cuối cùng chuỗi đã được xử lý
    result=[]

    with open("./VDic_uni.txt",encoding="utf8") as f_in:
        data=f_in.readlines()
    for line in data:
        #line là mảng sau khi cắt từ mỗi dòng của data
        # Vì data VDic_uni.txt mỗi line 2 từ cách nhau 2 tabs
        line=line.split("		")
        corpus += r"#{}#".format(line[0])
    maxWord=[]
    trueWord=[]
    index=0
    DELIMETER_SIGN=[',','.',':',':','?','!']

    while index<len(tokens):
        if(tokens[index][-1] in DELIMETER_SIGN):
            maxWord.append(tokens[index][:-1])
        else:
            maxWord.append(tokens[index])
        pattern="#{}#".format((" ".join(maxWord)).lower())
        checkExistInCorpus=re.findall(pattern,corpus)

        if checkExistInCorpus:
            trueWord.append(tokens[index])
            index+=1
            if index>=len(tokens):
                result.append("_".join(trueWord))
            continue
        else:
            if len(maxWord)==1:
                result.append("".join(maxWord))
                index+=1
            else:
                result.append("_".join(trueWord))
            maxWord=[]
            trueWord=[]
    return " ".join(result)

def main():
    print("Enter the sentence:")
    stringInput=input()
    result=Word_Segmentation(stringInput)
    print("Result: ",result)

if __name__=="__main__":
    main()






