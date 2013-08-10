PyChord
=======
Chord sheet parser, written in Python 3.x

**Current Version:** 0.0a

Description
-----------

This is designed to - eventually - replicate the Chordii parsing language, using Python as the backend.

I'm doing this as a way to learn more about Python outside of work, so some things may not wind up being possible, but I have high hopes.

Milestone 0: Test data                 - COMPLETE
  - Test data as importable module
  - Verses with/without chords
  - Chorus with/without tags
  - Document tags from Milestone 2

Milestone 1: Initial functionality     - COMPLETE
  - Filter out inline chords from lyrics and print on their own line
  - Chords designated by `[]`

Milestone 2: Document tag recognition  - IN PROGRESS
  - Recognize the following tags for documents:
    ```
	{title:This Is a Title}        - short: t
    {subtitle: This is a Subtitle} - short: st
    {key: G}                       - short: k
    {comment: This is a comment}   - short: c
	```

Milestone 3: Paragraph recognition
  - Only double-space paragraphs that contain chords
  - Recognize `{start_of_chorus}` and `{end_of_chorus}` tags (`{soc}`/`{eoc}`)
  - Recognize even when mixed verbosity (`{start_of_chorus}...{eoc}`)
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
  - Allow non-indented chorus "header" via `{soc: Header}`