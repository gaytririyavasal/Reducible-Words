
PROJECT DESCRIPTION AND GUIDELINES PROVIDED ON ASSIGNMENT INSTRUCTIONS

What are some of the longest English words that remain valid English words as you remove one letter at a time from those words?

The letters can be removed anywhere from the word one at a time but you may not rearrange the remaining letters to form a valid word. Every time you remove a letter the remaining letters form a valid English word. Eventually, you will end up with a single letter and that single letter must also be a valid English word. A valid English word is one that is found in the Oxford English Dictionary or Webster's Dictionary.

For want of a better term, we will call such words reducible words. Here are two examples of reducible words:

1: sprite. If you remove the r you get spite. Remove the e and you get spit. Remove the s and you get pit. Remove the p and you get it. Remove the t and you get i or I, which is a valid English word.

2: string. Take away the r and you have sting. Take away the t and you have sing. Take away the g and you have sin. Take away the s and you have in. Take away the n and you have i or I, which is a valid English word.

So all reducible words will reduce to one of three letters - a, i, and o. We will not accept any other letter as the final one-letter word.

There is no official word list in an electronic form that we can use. We will use a curated word list file called words.txt. All the words are in lowercase and are two letters or more in length. This word list will do as our input file.

Your output will be the list of the longest words that are reducible. You will print each word in alphabetical order on a line by itself. For example, if the longest reducible words were of length 10, then this would be your output:

carrousels
complected
completing
consigning
insolating
restarting
staunchest
stranglers
twitchiest

To run this program on Mac, do:

python3 Reducible.py < words.txt

To run this program on a Windows machine, do:

python Reducible.py < words.txt