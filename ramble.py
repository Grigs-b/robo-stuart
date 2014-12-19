__author__ = 'Ryan Grigsby'
import pyttsx, random, time, wikipedia

# in seconds
RAMBLE_FREQUENCY_MIN = 30
RAMBLE_FREQUENCY_MAX = 60


def boot_stuart():
    engine = pyttsx.init()
    # create a reasonable facsimile for Stuart, if one exists
    for voice in engine.getProperty('voices'):
        if 'Mike' in voice.name:
            print("*clears throat*")
            #engine.setProperty('voice', voice.id)
    # sloooww down
    engine.setProperty('rate', engine.getProperty('rate')-60)
    return engine

def get_starting_point(length):
    return random.randint(1, length-1) if length > 1 else 0

def get_rant(summary):
    '''
    To ramble in true Stuart fashion, we have to try and eliminate as much context as possible. Get a random wiki
    summary, and we'll break it up by sentences and start somewhere in the middle.
    :return: a Stuart-esque rambling
    '''
    summary = summary.encode('ascii', 'replace')    # we don't care about unicode
    summary.replace('\n', '')     #remove newlines so we dont speak them
    sentences = summary.split('.')

    # we've got to eliminate some context, so get a starting point
    start = get_starting_point(len(sentences))
    return '. '.join(sentences[start:])


engine = boot_stuart()
# TODO : Only ramble during work hours.
while True:
    try:
        topic = wikipedia.random()
        print("I'm reading about {}".format(topic))
        rant = get_rant(wikipedia.summary(wikipedia.random()))
        engine.say(rant)
        engine.runAndWait()
        if not engine.isBusy():
            print("Time to browse some TalkBass")
            time.sleep(random.randint(RAMBLE_FREQUENCY_MIN, RAMBLE_FREQUENCY_MAX))
    except Exception as err:
        print("This computer is...messing up.")
        print(str(err))
        engine.stop()
        engine = boot_stuart()