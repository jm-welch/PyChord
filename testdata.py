class Test():
  class WildRover():

    v1 = """
I've [1]been a wild rover for many a [4]year
And I [5]spent all my money on whiskey and [1]beer,
And [1]now I'm returning with gold in great [4]store
And I [5]never will play the wild rover no [1]more."""

    v2 = """
I went in to an ale-house I used to frequent
And I told the landlord that my money was spent.
I asked him for credit, he answered me "Neigh!
Such a custom as yours I could have any day." """

    v3_4 = """
{c:Chorus}

I took from my pocket ten sovereigns bright
And the landlord, his eyes opened wide with delight.
He said "I have whiskey and wines of the best
And the words that I spoke, they were only in jest."

{c:Chorus}

I'll go home to my parents, confess what I've done
And I'll ask them to pardon their prodigal son.
And if they forgive me as ofttimes before
Sure I never will play the wild rover no more.

{c:Chorus x2}"""

    chorus_plain = """
And it's [5]no, nay, never,
[1]No nay never no [4]more,
Will I [1]play the wild [4]rover
No [5]never no [1]more"""

    chorus = """
{c:Chorus}
{soc}
And it's [5]no, nay, never,
[1]No nay never no [4]more,
Will I [1]play the wild [4]rover
No [5]never no [1]more
{eoc}"""

    header = """{title: Wild Rover}
{st: trad.}"""

    footer = """
{key: G}"""

    def __str__(self):
      return '\n'.join([self.header,
                        self.v1,
                        self.chorus,
                        self.v2,
                        self.v3_4,
                        self.footer])


if __name__ == '__main__':
  print(str(Test.WildRover()))