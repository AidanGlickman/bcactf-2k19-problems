# Just You Wait Writeup

## Necessary Tools
* This one's not too bad. Every tool you need can be found on our old friend [dcode.fr](https://dcode.fr)

## Procedure
1. Ok, so it looks like we have 6 different pieces of data, each with their own encoding schemes. First up is `MzIgLSAgfDMgVGltZXMgQSBDaGFybXwgLSAzMg==`, Which is simply encoded with [base64](https://en.wikipedia.org/wiki/Base64). Decoding it gives us the message `32 -  |3 Times A Charm| - 32`.
2. The next block of text also looks a bit weird, but with our clue from the last bit we can get an idea. The number 32 appears at the beginning and end, and the middle says '3 Times a Charm'. Maybe it is [base32](https://en.wikipedia.org/wiki/Base32) encoded 3 times? Yup! Decoding it 3 times gives us our next message.

```
Why english so ard to tok. 
No speak more English. 
Ail gi you tu hints to read my encrypted languich. 

1. SALT iz key to gret food!
2. Le francais crypte le meilleur
```

3. Ok, this block is the clue to the last part, which looks like it is using some sort of substitution cipher. If we look at the clue, we can see 'SALT iz key' and 'Le francais crypte le meilleur.' The second part is talking about French ciphers, and the most well known French substitution cipher is the [Vigenere cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher), which takes a key, in this case it is probably 'SALT.'

```
That was simple enough. So I heard you came for a flag? Since you have made it this far, I’ll go easy on you and hand it over. 
bcactf{Ju57_y0u_W4i7_ZnJhbmNhaXM} But, be warned, next time it won’t be so simple… 
```


## Flag
`bcactf{Ju57_y0u_W4i7_ZnJhbmNhaXM}`

> write-up by: [**@aidanglickman**](https://aidanglickman.com)
