def input_file(file_name):
    file=file_name
    out=[]
    with open(file) as file:
        for line in file:
            if line[-1] == "\n":
                line = line[:-1]
            out.append(line)
        return out

def asm_2_bin(instructions: list[str], console_out=1) -> str:
    """
    переводит из asm в bin возвращает строку
    :param instructions:
    :param console_out - вывод в консоль 0 не выводится 1 выводится:
    :return: 4BF000
    """
    out = ''
    for i in instructions:
        out = out + asm_bin.get(i, "??")
    if console_out == 1:
        print("bin out:",out)
    return out

def bin_2_asm(instructions, console_out=1):
    """
    переводит из bin в asm возвращает строку
    :param instructions:
    :param console_out - вывод в консоль 0 не выводится 1 выводится:
    :return:
    """
    sort = []
    i = 0
    while i < len(instructions[0]):
    # for i in range(0, len(instructions[0]), 2):
        while instructions[0][i] == " " and i < len(instructions[0]):
            i+=1
        sort.append(instructions[0][i:i + 2].upper())
        i+=2

    out = ''
    for i in sort:
        out = out + i + " --> " + get_key(asm_bin,i) + "\n"
    if console_out == 1:
        print(out)
    return out

def get_key(d, value):
    """
    возвращает ключ искомого значения
    :param d - словарь:
    :param value - значение ключ которого ищется:
    :return:
    """
    if value == "??":
        return "Invalid instruction"
    for k, v in d.items():
        if v == value:
            return k

# словарь с инструкциями, пока без использования сложных инструкций
asm_bin = {
'NOP': '00',
'AJMP addr': '01',
'LJMP addr': '02',
'RR A': '03',
'INC A': '04',
'INC data addr': '05',
'INC @R0': '06',
'INC @R1': '07',
'INC R0': '08',
'INC R1': '09',
'INC R2': '0A',
'INC R3': '0B',
'INC R4': '0C',
'INC R5': '0D',
'INC R6': '0E',
'INC R7': '0F',
'JBC bit addr, addr': '10',
'ACALL addr': '11',
'LCALL addr': '12',
'RRC A': '13',
'DEC A': '14',
'DEC data addr': '15',
'DEC @R0': '16',
'DEC @R1': '17',
'DEC R0': '18',
'DEC R1': '19',
'DEC R2': '1A',
'DEC R3': '1B',
'DEC R4': '1C',
'DEC R5': '1D',
'DEC R6': '1E',
'DEC R7': '1F',
'JB bit addr, addr': '20',
'AJMP addr': '21',
'RET': '22',
'RL A': '23',
'ADD A,#data': '24',
'ADD A,data addr': '25',
'ADD A,@R0': '26',
'ADD A,@R1': '27',
'ADD A,R0': '28',
'ADD A,R1': '29',
'ADD A,R2': '2A',
'ADD A,R3': '2B',
'ADD A,R4': '2C',
'ADD A,R5': '2D',
'ADD A,R6': '2E',
'ADD A,R7': '2F',
'JNB bit addr, addr': '30',
'ACALL addr': '31',
'RETI': '32',
'RLC A': '33',
'ADDC A,#data': '34',
'ADDC A,data addr': '35',
'ADDC A,@R0': '36',
'ADDC A,@R1': '37',
'ADDC A,R0': '38',
'ADDC A,R1': '39',
'ADDC A,R2': '3A',
'ADDC A,R3': '3B',
'ADDC A,R4': '3C',
'ADDC A,R5': '3D',
'ADDC A,R6': '3E',
'ADDC A,R7': '3F',
'JC addr': '40',
'AJMP addr': '41',
'ORL data addr,A': '42',
'ORL data addr,#data': '43',
'ORL A,#data': '44',
'ORL A,data addr': '45',
'ORL A,@R0': '46',
'ORL A,@R1': '47',
'ORL A,R0': '48',
'ORL A,R1': '49',
'ORL A,R2': '4A',
'ORL A,R3': '4B',
'ORL A,R4': '4C',
'ORL A,R5': '4D',
'ORL A,R6': '4E',
'ORL A,R7': '4F',
'JNC addr': '50',
'ACALL addr': '51',
'ANL data addr,A': '52',
'ANL data addr,#data': '53',
'ANL A,#data': '54',
'ANL A,data addr': '55',
'ANL A,@R0': '56',
'ANL A,@R1': '57',
'ANL A,R0': '58',
'ANL A,R1': '59',
'ANL A,R2': '5A',
'ANL A,R3': '5B',
'ANL A,R4': '5C',
'ANL A,R5': '5D',
'ANL A,R6': '5E',
'ANL A,R7': '5F',
'JZ addr': '60',
'AJMP addr': '61',
'XRL data addr,A': '62',
'XRL data addr,#data': '63',
'XRL A,#data': '64',
'XRL A,data addr': '65',
'XRL A,@R0': '66',
'XRL A,@R1': '67',
'XRL A,R0': '68',
'XRL A,R1': '69',
'XRL A,R2': '6A',
'XRL A,R3': '6B',
'XRL A,R4': '6C',
'XRL A,R5': '6D',
'XRL A,R6': '6E',
'XRL A,R7': '6F',
'JNZ addr': '70',
'ACALL addr': '71',
'ORL C,bit addr': '72',
'JMP @A+DPTR': '73',
'MOV A,#data': '74',
'MOV data addr,#data': '75',
'MOV @R0,#data': '76',
'MOV @R1,#data': '77',
'MOV R0,#data': '78',
'MOV R1,#data': '79',
'MOV R2,#data': '7A',
'MOV R3,#data': '7B',
'MOV R4,#data': '7C',
'MOV R5,#data': '7D',
'MOV R6,#data': '7E',
'MOV R7,#data': '7F',
'SJMP addr': '80',
'AJMP addr': '81',
'ANL C,bit addr': '82',
'MOVC A,@A+PC': '83',
'DIV AB': '84',
'MOV data addr,data addr': '85',
'MOV data addr,@R0': '86',
'MOV data addr,@R1': '87',
'MOV data addr,R0': '88',
'MOV data addr,R1': '89',
'MOV data addr,R2': '8A',
'MOV data addr,R3': '8B',
'MOV data addr,R4': '8C',
'MOV data addr,R5': '8D',
'MOV data addr,R6': '8E',
'MOV data addr,R7': '8F',
'MOV DPTR,#data': '90',
'ACALL addr': '91',
'MOV bit addr,C': '92',
'MOVC A,@A+DPTR': '93',
'SUBB A,#data': '94',
'SUBB A,data addr': '95',
'SUBB A,@R0': '96',
'SUBB A,@R1': '97',
'SUBB A,R0': '98',
'SUBB A,R1': '99',
'SUBB A,R2': '9A',
'SUBB A,R3': '9B',
'SUBB A,R4': '9C',
'SUBB A,R5': '9D',
'SUBB A,R6': '9E',
'SUBB A,R7': '9F',
'ORL C,/bit addr': 'A0',
'AJMP addr': 'A1',
'MOV C,bit addr': 'A2',
'INC DPTR': 'A3',
'MUL AB': 'A4',
'reserved': 'A5',
'MOV @R0,data addr': 'A6',
'MOV @R1,data addr': 'A7',
'MOV R0,data addr': 'A8',
'MOV R1,data addr': 'A9',
'MOV R2,data addr': 'AA',
'MOV R3,data addr': 'AB',
'MOV R4,data addr': 'AC',
'MOV R5,data addr': 'AD',
'MOV R6,data addr': 'AE',
'MOV R7,data addr': 'AF',
'ANL C,/bit addr': 'B0',
'ACALL addr': 'B1',
'CPL bit addr': 'B2',
'CPL C': 'B3',
'CJNE A,#data, addr': 'B4',
'CJNE A,data addr, addr': 'B5',
'CJNE @R0,#data, addr': 'B6',
'CJNE @R1,#data, addr': 'B7',
'CJNE R0,#data, addr': 'B8',
'CJNE R1,#data, addr': 'B9',
'CJNE R2,#data, addr': 'BA',
'CJNE R3,#data, addr': 'BB',
'CJNE R4,#data, addr': 'BC',
'CJNE R5,#data, addr': 'BD',
'CJNE R6,#data, addr': 'BE',
'CJNE R7,#data, addr': 'BF',
'PUSH data addr': 'C0',
'AJMP addr': 'C1',
'CLR bit addr': 'C2',
'CLR C': 'C3',
'SWAP A': 'C4',
'XCH A,data addr': 'C5',
'XCH A,@R0': 'C6',
'XCH A,@R1': 'C7',
'XCH A,R0': 'C8',
'XCH A,R1': 'C9',
'XCH A,R2': 'CA',
'XCH A,R3': 'CB',
'XCH A,R4': 'CC',
'XCH A,R5': 'CD',
'XCH A,R6': 'CE',
'XCH A,R7': 'CF',
'POP data addr': 'D0',
'ACALL addr': 'D1',
'SETB bit addr': 'D2',
'SETB C': 'D3',
'DA A': 'D4',
'DJNZ data addr, addr': 'D5',
'XCHD A,@R0': 'D6',
'XCHD A,@R1': 'D7',
'DJNZ R0, addr': 'D8',
'DJNZ R1, addr': 'D9',
'DJNZ R2, addr': 'DA',
'DJNZ R3, addr': 'DB',
'DJNZ R4, addr': 'DC',
'DJNZ R5, addr': 'DD',
'DJNZ R6, addr': 'DE',
'DJNZ R7, addr': 'DF',
'MOVX A,@DPTR': 'E0',
'AJMP addr': 'E1',
'MOVX A,@R0': 'E2',
'MOVX A,@R1': 'E3',
'CLR A': 'E4',
'MOV A,data addr': 'E5',
'MOV A,@R0': 'E6',
'MOV A,@R1': 'E7',
'MOV A,R0': 'E8',
'MOV A,R1': 'E9',
'MOV A,R2': 'EA',
'MOV A,R3': 'EB',
'MOV A,R4': 'EC',
'MOV A,R5': 'ED',
'MOV A,R6': 'EE',
'MOV A,R7': 'EF',
'MOVX @DPTR,A': 'F0',
'ACALL addr': 'F1',
'MOVX @R0,A': 'F2',
'MOVX @R1,A': 'F3',
'CPL A': 'F4',
'MOV data addr,A': 'F5',
'MOV @R0,A': 'F6',
'MOV @R1,A': 'F7',
'MOV R0,A': 'F8',
'MOV R1,A': 'F9',
'MOV R2,A': 'FA',
'MOV R3,A': 'FB',
'MOV R4,A': 'FC',
'MOV R5,A': 'FD',
'MOV R6,A': 'FE',
'MOV R7,A': 'FF',
}

bin_out = asm_2_bin(input_file("asm_input"))

asm_out=bin_2_asm(input_file("bin_input"))
