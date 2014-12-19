__author__ = 'Ryan Grigsby'
import pyttsx, random, time, wikipedia

# in seconds
RAMBLE_FREQUENCY_MIN = 30*60
RAMBLE_FREQUENCY_MAX = 60*60
engine = pyttsx.init()

# create a reasonable facsimile for Stuart, if one exists
for voice in engine.getProperty('voices'):
    if 'Mike' in voice.name:
        engine.setProperty('voice', voice.id)

def get_starting_point(length):
    return random.randint(1, length-1) if length > 1 else 0

def get_rant(summary):
    '''
    To ramble in true Stuart fashion, we have to try and eliminate as much context as possible. Get a random wiki
    summary, and we'll break it up by sentences and start somewhere in the middle.
    :return: a Stuart-esque rambling
    '''
    summary = summary.encode('ascii', 'replace')    # we don't care about unicode
    summary.replace_all('\n', '')     #remove newlines so we dont speak them
    sentences = summary.split('.')

    # we've got to eliminate some context, so get a starting point
    start = get_starting_point(len(sentences))
    return '. '.join(sentences[start:])


# TODO : Only ramble during work hours.
while True:
    rant = get_rant(wikipedia.summary(wikipedia.random()))
    engine.say(rant)
    engine.runAndWait()
    time.sleep(random.randint(RAMBLE_FREQUENCY_MIN, RAMBLE_FREQUENCY_MAX))