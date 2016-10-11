# SoBrB

SoBrb (Sonos Be Rigth Back) is a simple python project that, in conjonction with a scheduler (e.g. CRON), lowers [Sonos speakers](http://www.sonos.com/system/) volume at a specific time and then puts it back to the level it used to be. Useful to automatically lower down the volume when radio ads are playing!

## Why?

I’m a big fan of [ICI Musique](http://icimusique.ca) (a public radio mostly playing music) and since October 2013 they started to introduce ads, a first since 1974! I find most of those ads to be of bad taste and are a big mood-breaker to say the least.

At some point I realized that most of the time ads were run at a specific time (i.e. at the 28th minute of each hours, for 2 minutes). I therefore decided to write a script that would automatically lower down the volume at that time.

## Install

SoBrb depends on the great [SoCo library](https://github.com/SoCo/SoCo/). You can install it by using pip:

``pip install soco``

## How it Works?

The idea here is to look if a particular stream is currently playing and if so execute the script, thus lower the volume for a given period of time.

To find out if the stream we want to mute is playing the script compares what's playing with a stream "signature". A stream signature is a URI (or a part of it that would be unique) that correspond to the URI of the radio station.

To help you figure out what’s the URI of the stream currently playing on your system you can run  **whats_playing.py** (in utils/).

Here’s an example:
```python
>>> python utils/whats_playing.py
Currently playing in Salon: x-sonos-http:_t%3a%3a49405423%3a%3aa%3a%3a4539012.mp3?sid=11&flags=32
Currently playing in Cuisine: x-rincon-mp3radio://7QMTL0.akacast.akamaistream.net/7/445/177407/v1/rc.akacast.akamaistream.net/7QMTL0
```

In my case that would be:

``uri_signature = "7QMTL0.akacast.akamaistream.net"``

Edit ``uri_signature = ""`` in **sonos_be_right_back.py** with your URI

## Schedule

I use a crontab job to lower the volume and to put it back on according to a schedule.

Here’s an example:
````
At the 28th minute of each hours between 8am and 5pm, weekdays:
28 08-17 * * 1-5 python ~/Documents/scripts/SoBrb/
sonos_be_right_back.py

Two minutes later…
30 08-17 * * 1-5 python ~/Documents/scripts/SoBrb/sonos_were_back.py
````

#### Author

[Jean-François Comeau](http://twitter.com/jfcomeau), UX/UI designer
[Website](http://jfcomeau.design)

#### Licence

SoBrb is released under the [MIT license](http://www.opensource.org/licenses/mit-license.php).
