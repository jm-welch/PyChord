''' Python Chord Sheet parser

Author : Jeremy Welch
Link   : https://github.com/jm-welch/PyChord

Notes:
My goal is to make something roughly-equivalent to Chordii in Python.

Chordii docs:
  http://www.vromans.org/johan/projects/Chordii/documentation/chordii-4.2-user_guide.pdf
'''


import testdata

def main():
  song = Test.WildRover()
  print('\n'.join(parse_chords(song.v1)))

def parse_chords(text):
  def split_line(line):
    ch_line, ly_line = '', ''

    while '[' in line:
      x = line.find('[')
      y = line.find(']')
      ch_line += '{0: >{1}}'.format(line[x+1:y],x+1 if ch_line=='' else x)
      ly_line += line[0:x]
      line = line[y+1:]

    ly_line += line
    return [ch_line, ly_line]

  result = []

  for l in text.splitlines():
    if l == '':
      result.append(l)
    else:
     result.extend(split_line(l))

  return result

if __name__ == '__main__':
  main()
