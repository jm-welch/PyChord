''' Python Chord Sheet parser

My goal is to make something roughly-equivalent to Chordii in Python.

Chordii docs:
  http://www.vromans.org/johan/projects/Chordii/documentation/chordii-4.2-user_guide.pdf

Milestone 0: Test data                 - COMPLETE
  - Test data as importable module
  - Verses with/without chords
  - Chorus with/without tags
  - Document tags from Milestone 2

Milestone 1: Initial functionality     - COMPLETE
  - Filter out inline chords from lyrics and print on their own line
  - Chords designated by []

Milestone 2: Document tag recognition  - IN PROGRESS
  - Recognize the following tags for documents:
    {title:This Is a Title}        - short: t
    {subtitle: This is a Subtitle} - short: st
    {key: G}                       - short: k
    {comment: This is a comment}   - short: c

Milestone 3: Paragraph recognition
  - Only double-space paragraphs that contain chords
  - Recognize {start_of_chorus} and {end_of_chorus} tags ({soc}/{eoc})
  - Recognize even when mixed verbosity ({start_of_chorus}{eoc})
  - Indent chorus blocks

Milestone 4: Refactoring
  - Song class
  - Cleanup code
  - Flesh out comments
  -

Future:
  - Full compatibility with the Chordii specification
  - Configuration file to specify settings
  - Output to EPS w/ conversion to PDF
  - Support for persistent 'library' of songs
  - Ability to import/export libraries
  - Library management via a GUI
  - Allow non-indented chorus "header" via '{soc: Header}'
'''

from testdata import Test

def main():
  print('\n'.join(parse_chords(Test.DBF.all)))

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
