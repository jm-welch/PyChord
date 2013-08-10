class Test():
  class DBF():
    tags = """
{title: Drink Between Friends}
{subtitle: The Highwaymen}
{key: Dmix}
"""
    tags_short = """
{t: Drink Between Friends}
{st: The Highwaymen}
{k: Dmix}
"""

    v1 = """
Come and [D]join me, my friends, take a [C]seat by the [D]fire
Fill your [D]glasses with whiskey, and [C]stay for a [G]while
And if [D]you're of a humor to [C]be enter[D]tained
Well, we'll [D]sing you a song, if you'll [C]join the re[G]frain
"""

    cho = """
Here's a [D]health to his-to-ry and one to mem-o-ry,
And [C]here's to the [D]point where all [G]memory [A]ends
[D]On the last cup, raise your glass, drink it up,
For there's [C]nothing so [D]fine as a [G]drink between [D]friends
"""

    cho_tagged = '\n'.join(('{c: Chorus}','{soc}',cho,'{eoc}'))

    v2 = """
Here's a health to the lusts and the loves of young life
We'll drink once to McGregor, and twice to his wife
Here's a health to the pleasures and pains of the year
If you drink one to sorrow, drink two to good cheer
"""

    all = '\n'.join((v1,cho,v2))
    all_tagged = '\n'.join((v1,cho_tagged,v2))
    all_with_headers = '\n'.join((tags,v1,cho_tagged,v2))
    all_with_short_headers = '\n'.join((tags_short,v1,cho_tagged,v2))

  class HS():
    v1 = """
[1]Somebody's knockin' at the garden gate
Hello, somebody, hello
It's [4]Bully John and his dirty mate
[1]Hello, [5]somebody, [1]hello
"""
