##import string
##
##s = []
##for char in string.ascii_lowercase:
##    s.append(char)
##    
##for char in string.ascii_uppercase:
##    s.append(char)
##
##for i in range(1, 10):
##    s.append(str(i))
##s.append('0')
##s.append(' ')
##s.append('.')
##
##ss = []
####ss.append('CGA')
####ss.append('CCA')
####ss.append('GTT')
####ss.append('TTG')
####ss.append('GGC')
####ss.append('GGT')
####ss.append('TTT')
####ss.append('CGC')
####ss.append('ATG')
####ss.append('AGT')
####ss.append('AAG')
####ss.append('TGC')
####ss.append('TCC')
####ss.append('TCT')
####ss.append('GGA')
####ss.append('GTG')
####ss.append('AAC')
####ss.append('TCA')
####ss.append('ACG')
####ss.append('TTC')
####ss.append('CTG')
####ss.append('CCT')
####ss.append('CCG')
####ss.append('CTA')
####ss.append('AAA')
####ss.append('CTT')
####ss.append('ATA')
####ss.append('TCG')
####ss.append('GAT')
####ss.append('GCT')
####ss.append('ACT')
####ss.append('ACC')
####ss.append('TAG')
####ss.append('GCA')
####ss.append('GAG')
####ss.append('AGA')
####ss.append('TTA')
####ss.append('ACA')
####ss.append('AGG')
####ss.append('GCG')
##
##ss.append('AAA')
##ss.append('AAC')
##ss.append('AAG')
##ss.append('AAT')
##ss.append('ACA')
##ss.append('ACC')
##ss.append('ACG')
##ss.append('ACT')
##ss.append('AGA')
##ss.append('AGC')
##ss.append('AGG')
##ss.append('AGT')
##ss.append('ATA')
##ss.append('ATC')
##ss.append('ATG')
##ss.append('ATT')
##
##ss.append('CAA')
##ss.append('CAC')
##ss.append('CAG')
##ss.append('CAT')
##ss.append('CCA')
##ss.append('CCC')
##ss.append('CCG')
##ss.append('CCT')
##ss.append('CGA')
##ss.append('CGC')
##ss.append('CGG')
##ss.append('CGT')
##ss.append('CTA')
##ss.append('CTC')
##ss.append('CTG')
##ss.append('CTT')
##
##ss.append('GAA')
##ss.append('GAC')
##ss.append('GAG')
##ss.append('GAT')
##ss.append('GCA')
##ss.append('GCC')
##ss.append('GCG')
##ss.append('GCT')
##ss.append('GGA')
##ss.append('GGC')
##ss.append('GGG')
##ss.append('GGT')
##ss.append('GTA')
##ss.append('GTC')
##ss.append('GTG')
##ss.append('GTT')
##
##ss.append('TAA')
##ss.append('TAC')
##ss.append('TAG')
##ss.append('TAT')
##ss.append('TCA')
##ss.append('TCC')
##ss.append('TCG')
##ss.append('TCT')
##ss.append('TGA')
##ss.append('TGC')
##ss.append('TGG')
##ss.append('TGT')
##ss.append('TTA')
##ss.append('TTC')
##ss.append('TTG')
##ss.append('TTT')
##
##print(s)
##print(ss)
##
##encoded = 'GATCCGGCGCGCACTCTAACACCCGCACTGTCTACCTCTAACTACGTCTTCCTATCCAGCGCGCCCGCTTCCGCGCGATCAATACTGCTTCCTAACAATAGATCTTGCGTACACTACTTC'
##
##count = 0
##sss = ''
##final = ''
##for char in encoded:
##    count += 1
##    sss += char
##    if count == 3:
##        count = 0
##        for i in range(0,len(ss)):
##            if ss[i] == sss:
##                final += s[i]
##        sss = ''
##
##print(final)


#!/usr/bin/env python

mapping = {

  'AAA': 'a',
  'AAC': 'b',
  'AAG': 'c',
  'AAT': 'd',
  'ACA': 'e',
  'ACC': 'f',
  'ACG': 'g',
  'ACT': 'h',
  'AGA': 'i',
  'AGC': 'j',
  'AGG': 'k',
  'AGT': 'l',
  'ATA': 'm',
  'ATC': 'n',
  'ATG': 'o',
  'ATT': 'p',
  'CAA': 'q',
  'CAC': 'r',
  'CAG': 's',
  'CAT': 't',
  'CCA': 'u',
  'CCC': 'v',
  'CCG': 'w',
  'CCT': 'x',
  'CGA': 'y',
  'CGC': 'z',
  'CGG': 'A',
  'CGT': 'B',
  'CTA': 'C',
  'CTC': 'D',
  'CTG': 'E',
  'CTT': 'F',
  'GAA': 'G',
  'GAC': 'H',
  'GAG': 'I',
  'GAT': 'J',
  'GCA': 'K',
  'GCC': 'L',
  'GCG': 'M',
  'GCT': 'N',
  'GGA': 'O',
  'GGC': 'P',
  'GGG': 'Q',
  'GGT': 'R',
  'GTA': 'S',
  'GTC': 'T',
  'GTG': 'U',
  'GTT': 'V',
  'TAA': 'W',
  'TAC': 'X',
  'TAG': 'Y',
  'TAT': 'Z',
  'TTG': ' ',
  'TTC': '0',
  'TCA': '1',
  'TCC': '2',
  'TCG': '3',
  'TCT': '4',
  'TGA': '5',
  'TGC': '6',
  'TGG': '7',
  'TGT': '8',
  'TTA': '9'
}


c = 'GATCCGGCGCGCACTCTAACACCCGCACTGTCTACCTCTAACTACGTCTTCCTATCCAGCGCGCCCGCTTCCGCGCGATCAATACTGCTTCCTAACAATAGATCTTGCGTACACTACTTC'

flag = []
for x in range(0, len(c), 3):
    piece = c[x:x+3]
    print(piece + ' = ' + mapping[piece])
    flag.append(mapping[piece])

print(''.join(flag))
