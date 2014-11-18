SoBrB
===
SoBrb (Sonos Be Rigth Back) is a simple python project that, in conjonction with a scheduler (e.g. CRON), lowers `Sonos speakers`_ volume at a specific time and then puts it back to the level it used to be. Useful for skipping radio ads!

Why?
—
I’m a big fan of `ICI Musique`_ (The French-language music radio service of Canada's national public broadcaster) and since October 2013 they started to introduce ads. I find most of those ads to be of bad taste and are a big mood-breaker to say the least.

At some point I realized that most of the time ads were run at a specific time (i.e. at the 28th minute of each hours, for 2 minutes). I therefore decided to write a script that would automatically lower down the volume at that time.

Installation
—
SoBrb depends on `SoCo library`_.

Use pip:

``pip install soco``

Config
—
Edit ``uri_signature = ""`` in **sonos_be_right_back.py** with the uri (or a part of it that would be unique) that correspond to the uri of the radio station.

To help you figure out what’s the uri you can run  **whats_playing.py** (in utils/).

Here’s an example:
.. code:: python

    >>> python utils/whats_playing.py
		>>> Currently playing in Salon: x-sonos-http:_t%3a%3a49405423%3a%3aa%3a%3a4539012.mp3?sid=11&flags=32
Currently playing in Cuisine: x-rincon-mp3radio://7QMTL0.akacast.akamaistream.net/7/445/177407/v1/rc.akacast.akamaistream.net/7QMTL0

Copy over the complete url or a part of it that would constitute a unique signature (i.e. in this case ’7QMTL0.akacast.akamaistream.net’) in uri_signature.

``uri_signature = [7QMTL0.akacast.akamaistream.net]``

Schedule
—
I use cron to schedule when to lower the volume and when to put it back on.

Here’s an example:
````
At the 28th minute of each hours between 8am and 5pm, weekdays:

28 08-17 * * 1-5 python ~/Documents/scripts/SoBrb/
sonos_be_right_back.py

Two minutes later…
30 08-17 * * 1-5 python ~/Documents/scripts/SoBrb/sonos_were_back.py


Author
—
`Jean-François Comeau`_, UI/UX designer

Licence
—
SoBrb is released under the `MIT license`_.

.. _Sonos speakers: http://www.sonos.com/system/
.. _SoCo library: https://github.com/SoCo/SoCo/
.. _ICI Musique: http://icimusique.ca
.. _MIT license: http://www.opensource.org/licenses/mit-license.php
.. _Jean-François Comeau: http://twitter.com/jfcomeau
