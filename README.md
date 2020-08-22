# GPXActivityTracker
Extracts activity data and displays summary statistics for locally stored .gpx files.

To run:
```
./Driver.py <Alternate Dir>
```
The program will run in the directory specified by DEFAULT_GPX_DIR on line 8 of `Driver.py`.
If \<Alternate Dir\> is specified the program will run there. 


The current implementation supports Suunto Ambit watch-generated .gpx files, including files converted by the [tools/openambit2gpx.py][1] script from the [Openambit][2] project.

[1]: https://github.com/openambitproject/openambit/blob/master/tools/openambit2gpx.py ".log to .gpx conversion script"
[2]: https://github.com/openambitproject/openambit "Openambit github"
