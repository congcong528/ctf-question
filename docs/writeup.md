# Write-up

Version 1

## Introduction
This writeup describes the methods and solutions to access the flags for each challenge in this CTF. 

Challenges have been split into 3 distinct difficulty levels- Easy, Intermediate and Difficult.
Easy is designed for novices to attempt, and does not expect any technical depth and knowledge of cybersecurity.
Intermediate is designed for those who have a basic understanding of cybersecurity, and requires some understanding of web applications and html.
Difficult requires an in-depth understanding of cybersecurity and participants should need to try creative methods to find the flag.
## Challenges

| Challenge | Difficulty |
| - | -|
| 1 | Easy |
| 2 | Intermediate |
| 3 | Intermediate |
| 4 | Intermediate |
| 5 | Difficult |

### Challenge 1
Difficulty: Easy
Skills required: Basic understanding of browsers and HTML

Challenge 1 is the easiest challenge. The flag is hidden as a comment in the header element of the webpage. 
It can be found by inspecting the source code for the file (use f12 or right-click, inspect on your browser).

### Challenge 2
Difficulty: Intermediate
Skills required: SQL injection
Challenge 2 is a login page, where users need to login to the website without proper credentials. 
Participants are expected to attempt popular illegal access methods such as brute force and SQL injection. In this case, SQL injection is the correct method.
A possible input would be `bob' or 1=1--` in the username field, and any value in the password field.
This would cause the server to interpret the login as valid, and access would be granted. The flag is then provided upon login, and this challenge is solved.

### Challenge 3
Difficulty: Intermediate
Skills required: Cryptography, Scripting
Challenge 3 provides an encoded message `\x06\x11\x0cs\x1b0=,'.*;:` , and participants need to decode the message to find the flag. While this can be a daunting task due to 
the large number of encryption methods, challengers should be able to decrypt the string after trying some of the most common algorithms.
The correct algorithm is single byte xor encryption.
To decrypt the string, participants should write a script to test all possible keys to finally find the hash. The script peseudocode is as such:
> For every integer n from 0 to 255,
> 	for every character c in the string,
>       xor(n, c)
>   print new string
After looking through the printed answers, one of the printed strings will contain the flag.

### Challenge 4
Difficulty: Easy/ Intermediate
Skills required: Broken access control
Challenge 4 requires users to provide a 6 star rating when there is no such available option. Hence participants are expected to think out of the 
box to submit such a feedback rating. The solution lies in the url. Notice that the links to each of the feedback option points to a specific url that 
ends with the selected feedback rating e.g. feedback of 5 start has `/feedback/5`. 
As such, to submit a feedback of 6 stars, the user simply has to edit the url to `/feedback/6`

### Challenge 5
Difficulty: Intermediate
Skills required: Base 64 decryption, cookies
Challenge 5 simply provides an empty screen, with no apparent clue to the location of the flag. It is actually hidden as the value in the cookies section under
the `session` key. However, that is not the end. The string has been hashed to base64. Hence users will have to decrypt the string using base64 to find the 
actual flag. Such a tool can be found online, such as [here](https://www.base64encode.org/)