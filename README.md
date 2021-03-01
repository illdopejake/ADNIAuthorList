# ADNIAuthorList

Far too many times now, I have reached the post-acceptance stage of manuscript publication, only to be told that I have to somehow calibrate the ADNI author list to fit the journal's expectations. Yes, ADNI makes you put a link directing to it's author list on your cover page. But even still, many journals (including all the Nature journals) also want you to provide a full list of all the authors and affiliations in ADNI at the end of your manuscript. Also, they want you to start counting your affiliations *after* the end of the affiliations list on your cover page. Who on earth has time for this garbage?!?!

So I made a very simple and kinda janky script to prep the ADNI author list for journals, so no poor soul has to go through the unenviable task of repeatedly changing the affiliation number of every one of the (hundreds of?) ADNI authors.

# Requirements:
Python 3+

# Usage
* First, clone or download this repo.
* Navigate to the repo on your local computer (`cd /location/of/ADNIAuthorList/`)
* Then, in your terminal or command prompt or whatever, type: `python ADNIAuthorList.py`
* When prompted, tell the program where you want to start numbering the ADNI affiliations (e.g. if your main text author page lists 8 affiliations, you would start here at 9).
* The script will output the author list, with affiliations! Paste it into your paper and your done!

# Issues?
Raise an issue.

