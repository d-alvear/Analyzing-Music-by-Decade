import json
import requests
import time


to_get = {'36cUttPdHVwUERcPdJDQhG': 'https://itunes.apple.com/search?term=the+rolling+stones+miss+you&limit=1',
        '4ztwMHfPZhPoruZdBbgriM': 'https://itunes.apple.com/search?term=commodores+three+times+a+lady&limit=1',
        '0y0QpmcF1G3F79rjk3fjUx': 'https://itunes.apple.com/search?term=a+taste+of+honey+boogie+oogie+oogie&limit=1',
        '5d4E1hgkLyb7sXr5J3InnM': 'https://itunes.apple.com/search?term=anne+murray+you+needed+me&limit=1',
        '6UXXeFqMBGiqjkzQzkMT3E': 'https://itunes.apple.com/search?term=bee+gees+tragedy&limit=1',
        '1ETz9baOMbvyodg9XwIps1': 'https://itunes.apple.com/search?term=blondie+heart+of+glass&limit=1',
        '7wbPfd2mXbStoZZSnHNd2V': 'https://itunes.apple.com/search?term=peaches+&+herb+reunited&limit=1',
        '73V1mhbDb7K0lqlHB82iN5': 'https://itunes.apple.com/search?term=bee+gees+love+you+inside+out&limit=1',
        '4f6dsGpNHRXepY9CgjQkxL': 'https://itunes.apple.com/search?term=donna+summer+bad+girls&limit=1',
        '1HOMkjp0nHMaTnfAkslCQj': 'https://itunes.apple.com/search?term=the+knack+my+sharona&limit=1',
        '3w3rLh6wmne91BS2rwgcog': 'https://itunes.apple.com/search?term=robert+john+sad+eyes&limit=1',
        '1Cesm6CDuP2UhLyq2fZV8k': 'https://itunes.apple.com/search?term=commodores+still&limit=1',
        '6PoXYcSlpCB4gJSmcYRY6X': 'https://itunes.apple.com/search?term=styx+babe&limit=1',
        '5IMtdHjJ1OtkxbGe4zfUxQ': 'https://itunes.apple.com/search?term=rupert+holmes+escape+(the+piña+colada+song)&limit=1',
        '0m4jVVZrsv0bLkAr1uM6UG': 'https://itunes.apple.com/search?term=captain+&+tennille+do+that+to+me+one+more+time&limit=1',
        '35ItUJlMtjOQW3SSiTCrrw': 'https://itunes.apple.com/search?term=queen+crazy+little+thing+called+love&limit=1',
        '6UGCCEogkX5fWorXeB1yiy': 'https://itunes.apple.com/search?term=blondie+call+me&limit=1',
        '0KQh7AuuZvpTKWhcJa8Pbr': 'https://itunes.apple.com/search?term=lipps+inc.+funkytown&limit=1',
        '0Ix1999mTT1A3TF6Bywgv5': 'https://itunes.apple.com/search?term=paul+mccartney+coming+up+(live+at+glasgow)&limit=1',
        '4OOelW7GAFlzPbcVcnwEIo': 'https://itunes.apple.com/search?term=diana+ross+upside+down&limit=1',
        '57JVGBtBLCfHw2muk5416J': 'https://itunes.apple.com/search?term=queen+another+one+bites+the+dust&limit=1',
        '149NXloAVhLWi9fI9Pmf5g': 'https://itunes.apple.com/search?term=kenny+rogers+lady&limit=1',
        '5y0YreEOnQiKFAnCrcFIXz': 'https://itunes.apple.com/search?term=john+lennon+(just+like)+starting+over&limit=1',
        '3K7Q9PHUWPTaknlbFPThn2': 'https://itunes.apple.com/search?term=kool+&+the+gang+celebration&limit=1',
        '131Svaar2WXaVMg4IByw9V': 'https://itunes.apple.com/search?term=blondie+rapture&limit=1',
        '0odIT9B9BvOCnXfS0e4lB5': 'https://itunes.apple.com/search?term=kim+carnes+bette+davis+eyes&limit=1',
        '0FGxAEMIE5GhyFqFMHRWaO': 'https://itunes.apple.com/search?term=diana+ross+endless+love&limit=1',
        '2yT82AafNlbpU7EAZkMQbw': 'https://itunes.apple.com/search?term=olivia+newton-john+physical&limit=1',
        '1ynmMEK1fkyiZ6Z6F3ThEt': 'https://itunes.apple.com/search?term=the+j.+geils+band+centerfold&limit=1',
        '3zmXCcrMKpGho2sTRZG1Ux': 'https://itunes.apple.com/search?term=vangelis+chariots+of+fire&limit=1',
        '3fVSMbeq8tY3G85yxcJwRU': 'https://itunes.apple.com/search?term=paul+mccartney+ebony+and+ivory&limit=1',
        '3L7RtEcu1Hw3OXrpnthngx': 'https://itunes.apple.com/search?term=the+human+league+dont+you+want+me&limit=1',
        '2E2ZVy2fxslpAUgbb4zu84': 'https://itunes.apple.com/search?term=steve+miller+band+abracadabra&limit=1',
        '4U6mBgGP8FXN6UH4T3AJhu': 'https://itunes.apple.com/search?term=joe+cocker+up+where+we+belong&limit=1',
        '53aSijEqI0rQCuK7qbtG7k': 'https://itunes.apple.com/search?term=lionel+richie+truly&limit=1',
        '3MrWxJaD2AT0W9DjWF64Vm': 'https://itunes.apple.com/search?term=dexys+midnight+runners+come+on+eileen&limit=1',
        '5nUpmh8WSlQooSmNEUWDJo': 'https://itunes.apple.com/search?term=irene+cara+flashdance...+what+a+feeling&limit=1',
        '1JSTJqkT5qHq8MDJnJbRE1': 'https://itunes.apple.com/search?term=the+police+every+breath+you+take&limit=1',
        '0QKfiqpEU4h9ycPSzIFwYe': 'https://itunes.apple.com/search?term=michael+sembello+maniac&limit=1',
        '2Wb9ejnmy27DUTUe9YF5Ew': 'https://itunes.apple.com/search?term=lionel+richie+all+night+long+(all+night)&limit=1',
        '4InXjGfCi4hJVWlqPuY6Im': 'https://itunes.apple.com/search?term=paul+mccartney+say+say+say&limit=1',
        '2wSAWEYUHkt92X4SBAPqZE': 'https://itunes.apple.com/search?term=culture+club+karma+chameleon&limit=1',
        '79byi182K1IfzjaUHeijWa': 'https://itunes.apple.com/search?term=lionel+richie+hello&limit=1',
        '1Qrdlkgg9I4J7r3P4kZNwr': 'https://itunes.apple.com/search?term=john+waite+missing+you&limit=1',
        '3fH4KjXFYMmljxrcGrbPj9': 'https://itunes.apple.com/search?term=simple+minds+dont+you+(forget+about+me)&limit=1',
        '4RvWPyQ5RL0ao9LPZeSouE': 'https://itunes.apple.com/search?term=tears+for+fears+everybody+wants+to+rule+the+world&limit=1',
        '43bLVIfp1CPtLgik5mXGv7': 'https://itunes.apple.com/search?term=bryan+adams+heaven&limit=1',
        '2gQaQUhDCNGfBVXTvxAmXQ': 'https://itunes.apple.com/search?term=tears+for+fears+shout&limit=1',
        '2olVm1lHicpveMAo4AUDRB': 'https://itunes.apple.com/search?term=huey+lewis+&+the+news+the+power+of+love&limit=1',
        '5PM96PMKMfD1lLX2lryUsG': 'https://itunes.apple.com/search?term=ready+for+the+world+oh+sheila&limit=1',
        '1mhEfzV4pz6R0ArW0CWOFp': 'https://itunes.apple.com/search?term=stevie+wonder+part&limit=1',
        '2UoF4VlADu3IkPCR6LGkpS': 'https://itunes.apple.com/search?term=jan+hammer+miami+vice+theme&limit=1',
        '1gN4wxYZXt7WBM2LAlS8MH': 'https://itunes.apple.com/search?term=heart+these+dreams&limit=1',
        '5izGeTxueiFX1UPFGohY9w': 'https://itunes.apple.com/search?term=robert+palmer+addicted+to+love&limit=1',
        '29UXndgjLVTUZ8b1Mhz9CR': 'https://itunes.apple.com/search?term=patti+labelle+on+my+own&limit=1',
        '3tarj4VIvuIa9Es0YkqUW7': 'https://itunes.apple.com/search?term=steve+winwood+higher+love&limit=1',
        '50jEs9EZZgXJ1oDZVAv7Wp': 'https://itunes.apple.com/search?term=berlin+take+my+breath+away&limit=1',
        '2cFl7utlqyZjCXN1G5nRvA': 'https://itunes.apple.com/search?term=huey+lewis+&+the+news+stuck+with+you&limit=1',
        '3mJ6pNcFM2CkykCYSREdKT': 'https://itunes.apple.com/search?term=janet+jackson+when+i+think+of+you&limit=1',
        '4gpext9x0CbdD9NWaa4nDj': 'https://itunes.apple.com/search?term=boston+amanda&limit=1',
        '537yo062QIz16oQOgxmul3': 'https://itunes.apple.com/search?term=the+human+league+human&limit=1',
        '0rmGAIH9LNJewFw7nKzZnc': 'https://itunes.apple.com/search?term=bon+jovi+you+give+love+a+bad+name&limit=1',
        '3R4gG3tZqKeXBgy1sXpaa4': 'https://itunes.apple.com/search?term=madonna+open+your+heart&limit=1',
        '37ZJ0p5Jm13JPevGcx4SkF': 'https://itunes.apple.com/search?term=bon+jovi+livin+on+a+prayer&limit=1',
        '0huRoriGPIi0vSHFV2f3C9': 'https://itunes.apple.com/search?term=huey+lewis+&+the+news+jacobs+ladder&limit=1',
        '4ByEFOBuLXpCqvO1kw8Wdm': 'https://itunes.apple.com/search?term=cutting+crew+(i+just)+died+in+your+arms&limit=1',
        '6ADSaE87h8Y3lccZlBJdXH': 'https://itunes.apple.com/search?term=u2+with+or+without+you&limit=1',
        '14izs7HtUGrTK8o7K2uqqc': 'https://itunes.apple.com/search?term=heart+alone&limit=1',
        '58vu117LAwbmxYAXqgMQ1S': 'https://itunes.apple.com/search?term=bob+seger+shakedown&limit=1',
        '6wpGqhRvJGNNXwWlPmkMyO': 'https://itunes.apple.com/search?term=u2+i+still+havent+found+what+im+looking+for&limit=1',
        '4uvjOKsp7mSjrDhWdkLPBY': 'https://itunes.apple.com/search?term=tiffany+i+think+were+alone+now&limit=1',
        '3GfGTJ2xzC0rqKgdjNJLOC': 'https://itunes.apple.com/search?term=billy+idol+mony+mony&limit=1',
        '58mFu3oIpBa0HLNeJIxsw3': 'https://itunes.apple.com/search?term=belinda+carlisle+heaven+is+a+place+on+earth&limit=1',
        '3OeUlriM0EZHdWleJtjoVr': 'https://itunes.apple.com/search?term=george+harrison+got+my+mind+set+on+you&limit=1',
        '3F2YXxSOC9dPmxXdrh6mYl': 'https://itunes.apple.com/search?term=richard+marx+hold+on+to+the+nights&limit=1',
        '7snQQk1zcKl8gZ92AnueZW': 'https://itunes.apple.com/search?term=guns+n+roses+sweet+child+o+mine&limit=1',
        '4hObp5bmIJ3PP3cKA9K9GY': 'https://itunes.apple.com/search?term=bobby+mcferrin+dont+worry+be+happy&limit=1',
        '3Dfy8YIxq89i84t108TvMi': 'https://itunes.apple.com/search?term=def+leppard+love+bites&limit=1',
        '4uOKFydzAejjSFqYbv1XPt': 'https://itunes.apple.com/search?term=ub40+red+red+wine&limit=1',
        '1CnMKxIztQzO9DM9qADbP8': 'https://itunes.apple.com/search?term=the+beach+boys+kokomo&limit=1',
        '72hcFp4tYkd3dbNA9dZ3Pv': 'https://itunes.apple.com/search?term=bon+jovi+bad+medicine&limit=1',
        '43GS3mtezoIFiuIZCLLiDY': 'https://itunes.apple.com/search?term=poison+every+rose+has+its+thorn&limit=1',
        '0v9kGNjkKdQUdDoBIuiph4': 'https://itunes.apple.com/search?term=bobby+brown+my+prerogative&limit=1',
        '3RJof5CojqlbgZ5adHw50O': 'https://itunes.apple.com/search?term=sheriff+when+im+with+you&limit=1',
        '5xl5582IihbEZAnfj0xyso': 'https://itunes.apple.com/search?term=paula+abdul+straight+up&limit=1',
        '07HqIg8BnB1lJElnw2ZiSR': 'https://itunes.apple.com/search?term=bon+jovi+ill+be+there+for+you&limit=1',
        '0lmS0Wofcv7B7uFYssSKta': 'https://itunes.apple.com/search?term=paula+abdul+forever+your+girl&limit=1',
        '47dEbqgg8E8D4lJBsB8KLp': 'https://itunes.apple.com/search?term=richard+marx+satisfied&limit=1',
        '6jrp8qBMJO6vhAeYVAsdk9': 'https://itunes.apple.com/search?term=paula+abdul+cold+hearted&limit=1',
        '4r5VaK6H1bq0cTGPMTN97Z': 'https://itunes.apple.com/search?term=janet+jackson+miss+you+much&limit=1',
        '7z38bideBRvGAgjXe2SECm': 'https://itunes.apple.com/search?term=paula+abdul+opposites+attract&limit=1',
        '5HAv1Ckfe50DUjv8ghwTrz': 'https://itunes.apple.com/search?term=janet+jackson+escapade&limit=1',
        '2fzHtlT0Ytt0Lxed76Ccm5': 'https://itunes.apple.com/search?term=madonna+vogue&limit=1',
        '6jRTkMfF0pCfT5m80CycvQ': 'https://itunes.apple.com/search?term=wilson+phillips+hold+on&limit=1',
        '1sUTfgduT0WIQO8kXKXxLC': 'https://itunes.apple.com/search?term=jon+bon+jovi+blaze+of+glory&limit=1',
        '1rIy3lkFJnMsTLZpxFmYU8': 'https://itunes.apple.com/search?term=wilson+phillips+release+me&limit=1',
        '3JjY2L2bqql54j1SjnjQ23': 'https://itunes.apple.com/search?term=nelson+(cant+live+without+your)+love+and+affection&limit=1',
        '6YtlpP5cMvGJbMkBWE3IfD': 'https://itunes.apple.com/search?term=janet+jackson+black+cat&limit=1',
        '4bBv0T7T4JVFRufmcXyY0X': 'https://itunes.apple.com/search?term=madonna+justify+my+love&limit=1',
        '1SkJ8HjZUZRPYT3R2rh5sA': 'https://itunes.apple.com/search?term=janet+jackson+love+will+never+do+(without+you)&limit=1',
        '02KLiEs31kxh1krQJezlTL': 'https://itunes.apple.com/search?term=londonbeat+ive+been+thinking+about+you&limit=1',
        '1nE0SDjEZxWrz2YXVK1Lm6': 'https://itunes.apple.com/search?term=wilson+phillips+youre+in+love&limit=1',
        '3IDsegNBHC4pjGCOMTQYlU': 'https://itunes.apple.com/search?term=amy+grant+baby+baby&limit=1',
        '1gVgkQFOKa8Wc1HYsJtPdH': 'https://itunes.apple.com/search?term=extreme+more+than+words&limit=1',
        '1GkRtFi1i90d3QngEVQTDY': 'https://itunes.apple.com/search?term=emf+unbelievable&limit=1',
        '6eBK3edMW7bEzecF1eCezc': 'https://itunes.apple.com/search?term=bryan+adams+(everything+i+do)+i+do+it+for+you&limit=1',
        '5m8xVZhlM7E2mL9uuxZpF6': 'https://itunes.apple.com/search?term=paula+abdul+the+promise+of+a+new+day&limit=1',
        '5hWdgGVcfTeLPAiHM6EZG9': 'https://itunes.apple.com/search?term=marky+mark+and+the+funky+bunch+good+vibrations&limit=1',
        '11FcfHd3SOmmrWJPGe7Y30': 'https://itunes.apple.com/search?term=george+michael+dont+let+the+sun+go+down+on+me&limit=1',
        '7okbmgA8lRBGl5limZ7LFM': 'https://itunes.apple.com/search?term=vanessa+williams+save+the+best+for+last&limit=1',
        '1SAkL1mYNJlaqnBQxVZrRl': 'https://itunes.apple.com/search?term=sir+mix-a-lot+baby+got+back&limit=1',
        '4L2EjXAj56FbYYb26YfcUL': 'https://itunes.apple.com/search?term=boyz+ii+men+end+of+the+road&limit=1',
        '2QVHmiFTjFsHyxONRdbkcq': 'https://itunes.apple.com/search?term=the+heights+how+do+you+talk+to+an+angel&limit=1',
        '4CUg7RRNVa2GLpwhodh4pC': 'https://itunes.apple.com/search?term=peabo+bryson+a+whole+new+world&limit=1',
        '29rQJydAlO0uMyWvRIZxQg': 'https://itunes.apple.com/search?term=janet+jackson+thats+the+way+love+goes&limit=1',
        '7ojJ4XvqBhBcteM0zjMebT': 'https://itunes.apple.com/search?term=ub40+(i+cant+help)+falling+in+love+with+you&limit=1',
        '391CwgcBxvUHmEKda2b5In': 'https://itunes.apple.com/search?term=meat+loaf+id+do+anything+for+love+(but+i+wont+do+that)&limit=1',
        '7GYnMWYheGL8l9g7XS7xOG': 'https://itunes.apple.com/search?term=janet+jackson+again&limit=1',
        '61sQYdFNS6sEBYCyr1q5gn': 'https://itunes.apple.com/search?term=boyz+ii+men+ill+make+love+to+you&limit=1',
        '6uQKuonTU8VKBz5SHZuQXD': 'https://itunes.apple.com/search?term=montell+jordan+this+is+how+we+do+it&limit=1',
        '32Gf5A7Hr8RdgggXG0Fdks': 'https://itunes.apple.com/search?term=bryan+adams+have+you+ever+really+loved+a+woman&limit=1',
        '1ZB2zIoc8AjSuyqKRcJgbO': 'https://itunes.apple.com/search?term=2pac+how+do+u+want+it&limit=1',
        '6MdqqkQ8sSC0WB4i8PyRuQ': 'https://itunes.apple.com/search?term=blackstreet+no+diggity&limit=1',
        '1Je1IMUlBXcx1Fz0WE7oPT': 'https://itunes.apple.com/search?term=spice+girls+wannabe&limit=1',
        '0lnxrQAd9ZxbhBBe7d8FO8': 'https://itunes.apple.com/search?term=hanson+mmmbop&limit=1',
        '027tq4cWr0kRxLTfdxvM1L': 'https://itunes.apple.com/search?term=boyz+ii+men+4+seasons+of+loneliness&limit=1',
        '1GrikfH0jDejDvrxo84n4P': 'https://itunes.apple.com/search?term=janet+jackson+together+again&limit=1',
        '5GorFaKkP2mLREQvhSblIg': 'https://itunes.apple.com/search?term=k-ci+&+jojo+all+my+life&limit=1',
        '4tyCIuHCxoeKK4XZ5jLnhD': 'https://itunes.apple.com/search?term=cher+believe&limit=1',
        '2bbeNsFmjZqdoDhjLsKNWe': 'https://itunes.apple.com/search?term=enrique+iglesias+bailamos&limit=1',
        '0M3TOK3E6W8RJkc2xKU2Cm': 'https://itunes.apple.com/search?term=sisqó+incomplete&limit=1',
        '0calZiHD3eVfJrHDCwzjW6': 'https://itunes.apple.com/search?term=janet+jackson+doesnt+really+matter&limit=1',
        '0eKyHwckh9vQb8ncZ2DXCs': 'https://itunes.apple.com/search?term=creed+with+arms+wide+open&limit=1',
        '3WkibOpDF7cQ5xntM1epyf': 'https://itunes.apple.com/search?term=shaggy+it+wasnt+me&limit=1',
        '3NuXDTbsYgjAgyALkdOJ0j': 'https://itunes.apple.com/search?term=janet+jackson+all+for+you&limit=1',
        '7GQqj9jRtDkMp8zByehXQI': 'https://itunes.apple.com/search?term=christina+aguilera+lady+marmalade&limit=1',
        '1P5vjPu3EPoPwDSikHOiiq': 'https://itunes.apple.com/search?term=ja+rule+im+real&limit=1',
        '3aw9iWUQ3VrPQltgwvN9Xu': 'https://itunes.apple.com/search?term=mary+j.+blige+family+affair&limit=1',
        '4hrae8atte6cRlSC9a7VCO': 'https://itunes.apple.com/search?term=ja+rule+always+on+time&limit=1',
        '6zMUIb4uce1CzpbjR3vMdN': 'https://itunes.apple.com/search?term=ashanti+foolish&limit=1',
        '04KTF78FFg8sOHC1BADqbY': 'https://itunes.apple.com/search?term=nelly+hot+in+herre&limit=1',
        '0ARK753YaiJbpLUk7z5yIM': 'https://itunes.apple.com/search?term=nelly+dilemma&limit=1',
        '5Z01UMMf7V1o0MzF86s6WJ': 'https://itunes.apple.com/search?term=eminem+lose+yourself&limit=1',
        '4RY96Asd9IefaL3X4LOLZ8': 'https://itunes.apple.com/search?term=50+cent+in+da+club&limit=1',
        '41bIQPBE1lFN0mmw6Lmssz': 'https://itunes.apple.com/search?term=50+cent+21+questions&limit=1',
        '4TJduXYW1Pg96EDNnfiwxJ': 'https://itunes.apple.com/search?term=murphy+lee+shake+ya+tailfeather&limit=1',
        '2CtCwQhY0ZLvr8L2l8Bo6e': 'https://itunes.apple.com/search?term=ludacris+stand+up&limit=1',
        '3A4cpTBPaIQdtPFb5JxtaX': 'https://itunes.apple.com/search?term=twista+slow+jamz&limit=1',
        '6ihObRBTB8xdSH2mlERtOX': 'https://itunes.apple.com/search?term=juvenile+slow+motion&limit=1',
        '2Ozc0me9PV5vlt8cokwdvI': 'https://itunes.apple.com/search?term=terror+squad+lean+back&limit=1',
        '2NBQmPrOEEjA8VbeWOQGxO': 'https://itunes.apple.com/search?term=snoop+dogg+drop+it+like+its+hot&limit=1',
        '5D2mYZuzcgjpchVY1pmTPh': 'https://itunes.apple.com/search?term=50+cent+candy+shop&limit=1',
        '0LzrhCZFXW94Y8nwtTuRlw': 'https://itunes.apple.com/search?term=gwen+stefani+hollaback+girl&limit=1',
        '3LmvfNUQtglbTrydsdIqFU': 'https://itunes.apple.com/search?term=mariah+carey+we+belong+together&limit=1',
        '1PS1QMdUqOal0ai3Gt7sDQ': 'https://itunes.apple.com/search?term=kanye+west+gold+digger&limit=1',
        '2hQU8LNZFUcXLUwqeABX3K': 'https://itunes.apple.com/search?term=mariah+carey+dont+forget+about+us&limit=1',
        '6zS6zUoWh8QluIZ2lv9tWb': 'https://itunes.apple.com/search?term=nelly+grillz&limit=1',
        '6brl7bwOHmGFkNw3MBqssT': 'https://itunes.apple.com/search?term=ne-yo+so+sick&limit=1',
        '30cSNer6TV8x2utjULVeQ5': 'https://itunes.apple.com/search?term=rihanna+sos&limit=1',
        '3kZoay4ANo86ehb6s4RwS9': 'https://itunes.apple.com/search?term=chamillionaire+ridin&limit=1',
        '47aQT2aV12TyilaoYi1NiD': 'https://itunes.apple.com/search?term=nelly+furtado+promiscuous&limit=1',
        '7jRoWfRlLnGYEIEn4t4kbq': 'https://itunes.apple.com/search?term=fergie+london+bridge&limit=1',
        '2JpUkUR0OsOlUUfm6iS8ic': 'https://itunes.apple.com/search?term=ludacris+money+maker&limit=1',
        '4xAk8Lw82G3YoVSOdVAsBx': 'https://itunes.apple.com/search?term=akon+i+wanna+love+you&limit=1',
        '0AA6zq5ArZ1sSH7VIMi4NK': 'https://itunes.apple.com/search?term=mims+this+is+why+im+hot&limit=1',
        '4KTtYhxFtFL7mBwnjkKfLm': 'https://itunes.apple.com/search?term=fergie+glamorous&limit=1',
        '7I6DceMT3utDOHjcYCbrr4': 'https://itunes.apple.com/search?term=akon+dont+matter&limit=1',
        '0wbDgMuAoy7O7pL3a69uZx': 'https://itunes.apple.com/search?term=timbaland+give+it+to+me&limit=1',
        '1lHXlGlve5Zx8tXLhyjDwM': 'https://itunes.apple.com/search?term=maroon+5+makes+me+wonder&limit=1',
        '49FYlytm3dAAraYgpoJZux': 'https://itunes.apple.com/search?term=rihanna+umbrella&limit=1',
        '4RCWB3V8V0dignt99LZ8vH': 'https://itunes.apple.com/search?term=plain+white+ts+hey+there+delilah&limit=1',
        '3Q4WeJmzxuDpzMu9QjQqbM': 'https://itunes.apple.com/search?term=fergie+big+girls+dont+cry&limit=1',
        '66TRwr5uJwPt15mfFkzhbi': 'https://itunes.apple.com/search?term=soulja+boy+crank+that+(soulja+boy)&limit=1',
        '4fzsfWzRhPawzqhX8Qt9F3': 'https://itunes.apple.com/search?term=kanye+west+stronger&limit=1',
        '4VcumP0Gs84VTIxSHGyvnu': 'https://itunes.apple.com/search?term=mariah+carey+touch+my+body&limit=1',
        '4P7VFiaZb3xrXoqGwZXC3J': 'https://itunes.apple.com/search?term=lil+wayne+lollipop&limit=1',
        '3goSVuTt3fDYDP6kRnFwuL': 'https://itunes.apple.com/search?term=rihanna+take+a+bow&limit=1',
        '005lwxGU1tms6HGELIcUv9': 'https://itunes.apple.com/search?term=katy+perry+i+kissed+a+girl&limit=1',
        '2VOomzT6VavJOGBeySqaMc': 'https://itunes.apple.com/search?term=rihanna+disturbia&limit=1',
        '1fJ2hkhhyxVnpKOwzLRNyE': 'https://itunes.apple.com/search?term=lady+gaga+just+dance&limit=1',
        '4dK00wCxlqWEeN8BoM1BHT': 'https://itunes.apple.com/search?term=eminem+crack+a+bottle&limit=1',
        '0EqCQ0kGCNNQRYWhfjTh5X': 'https://itunes.apple.com/search?term=lady+gaga+poker+face&limit=1',
        '7xRNsqOQOgWbHV1nbXnfXN': 'https://itunes.apple.com/search?term=black+eyed+peas+boom+boom+pow&limit=1',
        '4vp2J1l5RD4gMZwGFLfRAu': 'https://itunes.apple.com/search?term=black+eyed+peas+i+gotta+feeling&limit=1',
        '7LP4Es66zdY7CyjepqmvAg': 'https://itunes.apple.com/search?term=jay+sean+down&limit=1',
        '3DamFFqW32WihKkTVlwTYQ': 'https://itunes.apple.com/search?term=owl+city+fireflies&limit=1',
        '2igwFfvr1OAGX9SKDCPBwO': 'https://itunes.apple.com/search?term=jay-z+empire+state+of+mind&limit=1',
        '5OiLJ8tjUPFiPX2gVM8fxJ': 'https://itunes.apple.com/search?term=black+eyed+peas+imma+be&limit=1',
        '1CdqVF1ywD0ZO1zXtB9yWa': 'https://itunes.apple.com/search?term=taio+cruz+break+your+heart&limit=1',
        '60jzFy6Nn4M0iD1d94oteF': 'https://itunes.apple.com/search?term=rihanna+rude+boy&limit=1',
        '7Ie9W94M7OjPoZVV216Xus': 'https://itunes.apple.com/search?term=eminem+not+afraid&limit=1',
        '6tS3XVuOyu10897O3ae7bi': 'https://itunes.apple.com/search?term=katy+perry+california+gurls&limit=1',
        '15JINEqzVMv3SvJTAXAKED': 'https://itunes.apple.com/search?term=eminem+love+the+way+you+lie&limit=1',
        '5jzKL4BDMClWqRguW5qZvh': 'https://itunes.apple.com/search?term=katy+perry+teenage+dream&limit=1',
        '4DvhkX2ic4zWkQeWMwQ2qf': 'https://itunes.apple.com/search?term=far+east+movement+like+a+g6&limit=1',
        '6DkXLzBQT7cwXmTyzAB1DJ': 'https://itunes.apple.com/search?term=rihanna+whats+my+name?&limit=1',
        '2ENexcMEMsYk0rVJigVD3i': 'https://itunes.apple.com/search?term=rihanna+only+girl+(in+the+world)&limit=1',
        '4lCv7b86sLynZbXhfScfm2': 'https://itunes.apple.com/search?term=katy+perry+firework&limit=1',
        '6r2BECwMgEoRb5yLfp0Hca': 'https://itunes.apple.com/search?term=lady+gaga+born+this+way&limit=1',
        '40UMPtDbxDJQ0huWj2lzmb': 'https://itunes.apple.com/search?term=katy+perry+e.t.&limit=1',
        '7ySUcLPVX7KudhnmNcgY2D': 'https://itunes.apple.com/search?term=rihanna+s&m&limit=1',
        '0IkKz2J93C94Ei4BvDop7P': 'https://itunes.apple.com/search?term=lmfao+party+rock+anthem&limit=1',
        '3avYqdwHKEq8beXbeWCKqJ': 'https://itunes.apple.com/search?term=katy+perry+last+friday+night+(t.g.i.f.)&limit=1',
        '1Bmg1Mq9jFzIt6H17BYXUW': 'https://itunes.apple.com/search?term=maroon+5+moves+like+jagger&limit=1',
        '6qn9YLKt13AGvpq9jfO8py': 'https://itunes.apple.com/search?term=rihanna+we+found+love&limit=1',
        '0obBFrPYkSoBJbvHfUIhkv': 'https://itunes.apple.com/search?term=lmfao+sexy+and+i+know+it&limit=1',
        '1nZzRJbFvCEct3uzu04ZoL': 'https://itunes.apple.com/search?term=katy+perry+part+of+me&limit=1',
        '4wCmqSrbyCgxEXROQE6vtV': 'https://itunes.apple.com/search?term=gotye+somebody+that+i+used+to+know&limit=1',
        '3TGRqZ0a2l1LRblBkJoaDx': 'https://itunes.apple.com/search?term=carly+rae+jepsen+call+me+maybe&limit=1',
        '7AEAGTc8cReDqcbPoY9gwo': 'https://itunes.apple.com/search?term=taylor+swift+we+are+never+ever+getting+back+together&limit=1',
        '4XNrMwGx1SqP01sqkGTDmo': 'https://itunes.apple.com/search?term=maroon+5+one+more+night&limit=1',
        '5VlyxtjCKSk2ETp1D3W0GX': 'https://itunes.apple.com/search?term=rihanna+diamonds&limit=1',
        '0n4bITAu0Y0nigrz3MFJMb': 'https://itunes.apple.com/search?term=robin+thicke+blurred+lines&limit=1',
        '6F5c58TMEs1byxUstkzVeM': 'https://itunes.apple.com/search?term=katy+perry+roar&limit=1',
        '2dLLR6qlu5UJ5gk0dKz0h3': 'https://itunes.apple.com/search?term=lorde+royals&limit=1',
        '48RrDBpOSSl1aLVCalGl5C': 'https://itunes.apple.com/search?term=eminem+the+monster&limit=1',
        '5jrdCoLpJSvHHorevXBATy': 'https://itunes.apple.com/search?term=katy+perry+dark+horse&limit=1',
        '3oiMJQAWVaxSubJ7b2VUtX': 'https://itunes.apple.com/search?term=iggy+azalea+fancy&limit=1',
        '5xTtaWoae3wi06K5WfVUUH': 'https://itunes.apple.com/search?term=taylor+swift+shake+it+off&limit=1',
        '1p80LdxRV74UKvL8gnD7ky': 'https://itunes.apple.com/search?term=taylor+swift+blank+space&limit=1',
        '273dCMFseLcVsoSWx59IoE': 'https://itunes.apple.com/search?term=taylor+swift+bad+blood&limit=1',
        '22VdIZQfgXJea34mQxlt81': 'https://itunes.apple.com/search?term=the+weeknd+cant+feel+my+face&limit=1',
        '4B0JvthVoAAuygILe3n4Bs': 'https://itunes.apple.com/search?term=justin+bieber+what+do+you+mean?&limit=1',
        '7fBv7CLKzipRk6EC6TWHOB': 'https://itunes.apple.com/search?term=the+weeknd+the+hills&limit=1',
        '22miRgpJCBD0WRka7G53s0': 'https://itunes.apple.com/search?term=justin+bieber+love+yourself&limit=1',
        '72TFWvU3wUYdUuxejTTIzt': 'https://itunes.apple.com/search?term=rihanna+work&limit=1',
        '275a9yzwGB6ncAW4SxY7q3': 'https://itunes.apple.com/search?term=desiigner+panda&limit=1',
        '1zi7xx7UVEFkmKfv06H8x0': 'https://itunes.apple.com/search?term=drake+one+dance&limit=1',
        '6fujklziTHa8uoM5OQSfIo': 'https://itunes.apple.com/search?term=rae+sremmurd+black+beatles&limit=1',
        '7MXVkk9YMctZqd1Srtv4MB': 'https://itunes.apple.com/search?term=the+weeknd+starboy&limit=1',
        '7KXjTSCq5nL1LoYtL7XAwS': 'https://itunes.apple.com/search?term=kendrick+lamar+humble&limit=1',
        '6habFhsOp2NvshLv26DqMb': 'https://itunes.apple.com/search?term=luis+fonsi+despacito&limit=1',
        '1P17dC1amhFzptugyAO7Il': 'https://itunes.apple.com/search?term=taylor+swift+look+what+you+made+me+do&limit=1',
        '0e7ipj03S05BNilyu5bRzt': 'https://itunes.apple.com/search?term=post+malone+rockstar+(feat.+21+savage)&limit=1',
        '6DCZcSspjsKoFjzjrWoCdn': 'https://itunes.apple.com/search?term=drake+gods+plan&limit=1',
        '3CA9pLiwRIGtUBiMjbZmRw': 'https://itunes.apple.com/search?term=drake+nice+for+what&limit=1',
        '3swc6WTsr7rl9DqQKQA55C': 'https://itunes.apple.com/search?term=post+malone+psycho&limit=1',
        '3ee8Jmje8o58CHK66QrVC2': 'https://itunes.apple.com/search?term=xxxtentacion+sad!&limit=1',
        '2G7V7zsVDxg1yRsu7Ew9RJ': 'https://itunes.apple.com/search?term=drake+in+my+feelings&limit=1',
        '2rb9aqRTP8wBQgmyx1rH1I': 'https://itunes.apple.com/search?term=maroon+5+girls+like+you&limit=1',
        '3e9HZxeyfWwjeyPAMmWSSQ': 'https://itunes.apple.com/search?term=ariana+grande+thank+u+next&limit=1',
        '5p7ujcrUXASCNwRaWNHR1C': 'https://itunes.apple.com/search?term=halsey+without+me&limit=1',
        '3KkXRkHbMCARz0aVfEt68P': 'https://itunes.apple.com/search?term=post+malone+sunflower&limit=1',
        '6ocbgoVGwYJhOv1GgI9NsF': 'https://itunes.apple.com/search?term=ariana+grande+7+rings&limit=1',
        '2VxeLyX666F8uXCJ0dZF8B': 'https://itunes.apple.com/search?term=lady+gaga+shallow&limit=1',
        '22vgEDb5hykfaTwLuskFGD': 'https://itunes.apple.com/search?term=jonas+brothers+sucker&limit=1',
        '2Fxmhks0bxGSBdJ92vM42m': 'https://itunes.apple.com/search?term=billie+eilish+bad+guy&limit=1',
        '0TK2YIli7K1leLovkQiNik': 'https://itunes.apple.com/search?term=shawn+mendes+señorita&limit=1',
        '7qEHsqek33rTcFNT9PFqLf': 'https://itunes.apple.com/search?term=lewis+capaldi+someone+you+loved&limit=1',
        '4l0Mvzj72xxOpRrp6h8nHi': 'https://itunes.apple.com/search?term=selena+gomez+lose+you+to+love+me&limit=1',
        '7aH5zH4TxVotW0meTNqEJj': 'https://itunes.apple.com/search?term=the+weeknd+heartless&limit=1',
        '443uAjFs4FWHjI98GrpYgz': 'https://itunes.apple.com/search?term=mariah+carey+all+i+want+for+christmas+is+you&limit=1'}

responses = {}
error = {}

for track_id, url in to_get.items():
    try:
        r = requests.get(url)
        content = r.json()
        preview = content['results'][0]["previewUrl"]
        genre = content['results'][0]["primaryGenreName"]
        
    except JSONDecodeError:
        time.sleep(3)
        
        r = requests.get(url)
        content = r.json()
        preview = content['results'][0]["previewUrl"]
        genre = content['results'][0]["primaryGenreName"]

    else:
        error[track_id] = url

    responses[track_id] = [preview, genre]
    

print(len(responses.keys()))