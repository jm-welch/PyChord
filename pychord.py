''' Python Chord Sheet parser

Author : Jeremy Welch
Link   : https://github.com/jm-welch/PyChord

Notes:
My goal is to make something roughly-equivalent to Chordii in Python.

Chordii docs:
  http://www.vromans.org/johan/projects/Chordii/documentation/chordii-4.2-user_guide.pdf
'''

from sys import argv
import os
import json
import logging

#TODO: argparse?
class Tags:
  """ Define document-level tags in short and long form
  """
  soc = ['start_of_chorus','soc']
  eoc = ['end_of_chorus','eoc']
  title = ['title', 't']
  subtitle = ['subtitle', 'st']
  comment = ['comment', 'c']
  key = ['key', 'k']

def main():
  """ Main program logic goes here
  """

  # Assume that the first arg is the input file.
  if len(argv) > 1:
    infile = os.path.abspath(argv[1])
    logging.debug('Input file: {}'.format(infile))

  # Check for file existence before reading
  if not os.path.exists(infile):
    logger.error('Unable to locate "{}". Script will terminate.'.format(infile))
    return

  # Read data in
  with open(infile,'r') as f:
    raw_song = f.readlines()

  # Initialize vars
  # TODO: Song will eventually be its own class, hence some of the values in the dict.
  global song     # Temporary
  song = {'body_lines': [], 'chorus':False, 'split':False}
  indent = '     '
  paragraph = []

  # Parse lines
  for i in range(len(raw_song)):
    line = raw_song[i].strip('\n')

    # At the end of a paragraph, handle paragraph lines (if any) and reset split and paragraph
    if line == '':
      logger.debug('Blank line encountered on line {}. Paragraph:\n  {}\n'.format(i, '\n  '.join(paragraph)))
      if paragraph:
        if '[' in '\n'.join(paragraph):
          ln = [x for x in chord_parse(paragraph)]
          logger.debug('Chord tags found in paragraph. Parsed output:\n  {}\n'.format('\n  '.join(ln)))
          song['body_lines'].extend(ln)
        else:
          logger.debug('No chords found in paragraph. Appending to song body.')
          #paragraph.append(line)
          song['body_lines'].extend(paragraph)
        paragraph = []
      song['body_lines'].append(line)
    else:
      if '{' in line:
      # Document tag found in line
        if line[-1:] != '}':
        # Tag unclosed - print an error
          logger.warn('Unclosed tag on line {}. Line will be discarded. Line:\n  {}\n'.format(i, line))
        else:
        # Tag closed - continue processing
          song = tag_parse(song, line, i)
      else:
      # No document tag, process as text
        paragraph.append('{}{}'.format(indent*song['chorus'], line))
        logger.debug('No document tag found. Adding line to paragraph. Paragraph lines: {}'.format(len(paragraph)))

  with open('output.chart', 'w') as f:
    f.write(song['title'] + '\n')
    f.write(song['subtitle'] + '\n')
    f.write('\n'.join(song['body_lines']))


def tag_parse(song, line, index):
  line_split = line.strip('{}').split(':',1)
  tag = line_split[0].lower()

  val = line_split[1].lstrip() if len(line_split) > 1 else None

  #TODO: Normalize debug log output.
  if tag in Tags.soc:           # Found Start of Chorus tag
    song['chorus'] = True
    logger.debug('Line: {} - {} tag found. START_OF_CHORUS.'.format(index, tag))
  elif tag in Tags.eoc:         # Found End of Chorus tag
    song['chorus'] = False
    logger.debug('Line: {} - {} tag found. Ending indentation'.format(index, tag))
  elif tag in Tags.title:       # Found Title tag
    song['title'] = val
    logger.debug('{} tag "{}" found on line {}.'.format(tag, val, index))
  elif tag in Tags.subtitle:    # Found Subtitle tag
    song['subtitle'] = val
    logger.debug('{} tag "{}" found on line {}.'.format(tag, val, index))
  elif tag in Tags.comment:     # Found Comment tag
    song['body_lines'].append(val)
    logger.debug('{} tag "{}" found on line {}.'.format(tag, val, index))
  elif tag in Tags.key:         # Found Key tag
    song['key'] = val
    logger.debug('{} tag "{}" found on line {}.'.format(tag, val, index))
  else:
    logger.warn('Unrecognized tag "{}" on line {}. Ignoring line. Line:\n  {}\n'.format(tag, index, line))

  return song

def chord_parse(paragraph):
  """ Parse chords from a paragraph of text
  lines - paragraph, as a list of lines
  """

  for line in paragraph:
    ch_line, ly_line = '', ''
    while '[' in line:
      x = line.find('[')
      y = line.find(']')
      ch_line += '{0: >{1}}'.format(line[x+1:y], x if ch_line else x+1)
      ly_line += line[0:x]
      line = line[y+1:]

    ly_line += line
    yield ch_line
    yield ly_line


def gtfo():
  exit()

def setup_logging(toconsole=True, tofile=False, level=logging.INFO, flevel=False):
  global logger
  logger = logging.getLogger()
  logger.setLevel(level)

  formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

  # File handler
  if tofile:
    fh = logging.FileHandler('pychord.log')
    fh.setLevel(flevel if flevel else level)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

  #Stream Handler (console)
  if toconsole:
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

  logger.info('Log initialized')

if __name__ == '__main__':
  setup_logging(level=logging.DEBUG)
  main()

