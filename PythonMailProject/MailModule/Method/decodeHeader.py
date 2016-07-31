from email import header

class DecodeHeaderClass:
    # EML 파일을 decoding 하는 Methdo
    def decodeHeader(headerMsg):
        L = header.decode_header(headerMsg)  # 파일을 변환하는 과정
        return L[0][0]  # return 값을 해당하는 subject 문자열만 반환
