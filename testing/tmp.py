rcads = """
1 I worry about things Never Sometimes Often Always

2 I feel sad or empty Never Sometimes Often Always

3 When I have a problem, I get a funny feeling in my stomach Never Sometimes Often Always

4 I worry when I think I have done poorly at something Never Sometimes Often Always

5 I would feel afraid of being on my own at home Never Sometimes Often Always

6 Nothing is much fun anymore Never Sometimes Often Always

7 I feel scared when I have to take a test Never Sometimes Often Always

8 I feel worried when I think someone is angry with me Never Sometimes Often Always

9 I worry about being away from my parent Never Sometimes Often Always

10 I am bothered by bad or silly thoughts or pictures in 
my mind

Never Sometimes Often Always

11 I have trouble sleeping Never Sometimes Often Always

12 I worry that I will do badly at my school work Never Sometimes Often Always

13 I worry that something awful will happen to someone 
in my family

Never Sometimes Often Always

14 I suddenly feel as if I can’t breathe when there is no 
reason for this

Never Sometimes Often Always

15 I have problems with my appetite Never Sometimes Often Always

16 I have to keep checking that I have done things right 
(like the switch is off, or the door is locked)

Never Sometimes Often Always

17 I feel scared if I have to sleep on my own Never Sometimes Often Always

18 I have trouble going to school in the mornings 
because I feel nervous or afraid

Never Sometimes Often Always

19 I have no energy for things Never Sometimes Often Always

20 I worry I might look foolish Never Sometimes Often Always

RCADS—C h i l d / Y o u n g  P e r s o n                                                                                                   Questions © 2003 Bruce F. Chorpita, Ph.D  

NHS ID:   

Child/ Young Person’s NAME:   


Date:  / / 20                                                      Time:   h  m

Please put a circle around the word that shows how often each of these things happens to you. 
There are no right or wrong answers.

RCADS



21 I am tired a lot Never Sometimes Often Always

22 I worry that bad things will happen to me Never Sometimes Often Always

23 I can’t seem to get bad or silly thoughts out of my head Never Sometimes Often Always

24 When I have a problem, my heart beats really fast Never Sometimes Often Always

25 I cannot think clearly Never Sometimes Often Always

26 I suddenly start to tremble or shake when there is no 
reason for this

Never Sometimes Often Always

27 I worry that something bad will happen to me Never Sometimes Often Always

28 When I have a problem, I feel shaky Never Sometimes Often Always

29 I feel worthless Never Sometimes Often Always

30 I worry about making mistakes Never Sometimes Often Always

31 I have to think of special thoughts (like numbers or 
words) to stop bad things from happening

Never Sometimes Often Always

32 I worry what other people think of me Never Sometimes Often Always

33 I am afraid of being in crowded places (like shopping 
centers, the movies, buses, busy playgrounds)

Never Sometimes Often Always

34 All of a sudden I feel really scared for no reason at all Never Sometimes Often Always

35 I worry about what is going to happen Never Sometimes Often Always

36 I suddenly become dizzy or faint when there is no 
reason for this

Never Sometimes Often Always

37 I think about death Never Sometimes Often Always

38 I feel afraid if I have to talk in front of my class Never Sometimes Often Always

39 My heart suddenly starts to beat too quickly for no reason Never Sometimes Often Always

40 I feel like I don’t want to move Never Sometimes Often Always

41 I worry that I will suddenly get a scared feeling when 
there is nothing to be afraid of

Never Sometimes Often Always

42 I have to do some things over and over again (like washing 
my hands, cleaning or putting things in a certain order)

Never Sometimes Often Always

43 I feel afraid that I will make a fool of myself in front 
of people

Never Sometimes Often Always

44 I have to do some things in just the right way to stop 
bad things from happening

Never Sometimes Often Always

45 I worry when I go to bed at night Never Sometimes Often Always

46 I would feel scared if I had to stay away from 
home overnight

Never Sometimes Often Always

47 I feel restless Never Sometimes Often Always

RCADS—C h i l d / Y o u n g  P e r s o n                                                                                                   Questions © 2003 Bruce F. Chorpita, Ph.D  

"""

import sys
sys.path.append("../harmony_pypi_package/src/")

import harmony
from harmony.schemas.requests.text import RawFile
f = RawFile(file_name="rcads", file_type="pdf", text_content=rcads, content=rcads, file_id="aaa")

harmony.convert_text_to_instruments(f)