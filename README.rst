Frequently Used Tools (FUTS)
--------
A bunch of stuff that if find useful and have developed over the years.

To use (with caution), simply do:

```
import futs

print futs.joke()
```

To run the unit tests i've written:

```
python setup.py test
```

Python functions:
--------
- check_for_sensible_lat_long:
- time_above_the_horizon:
- when_is_sunrise_and_sunset:
- which_time_zone:
- local_to_utc:
- extract_daylight_passes:
- datestring_to_YYYY_DOY:
- round_down_to_nearest:
- round_up_to_nearest:
- round_to_nearest:
- closest_five_min_granule_time:

Other tools:
--------
There's a bunch of scripts in the bin/ dir that are added to your path when you install this package.
- unpack: Extract common file formats, dependencies: unrar, unzip, p7zip

Installation.
--------
Now we can install the package locally (for use on our system), with:

```python setup.py install ```

We can also install the package with a symlink, so that changes to the source files will be immediately available to other users of the package on our system:

```python setup.py develop ```


This package was put together using these instructions
--------
I found a webpage here: http://python-packaging.readthedocs.io/en/latest/minimal.html


The bin dir has command line tools and stuff like that. - make sure to add them to the setup.py when you make new ones.
The robs_tool_belt dir has the python functions - make sure to add the to the __init__.py when you make new ones.


Acknowledgement:
--------
The name futs - Frequently Used Tools - came from the brainstorming of my brilliant wife, Meg.
