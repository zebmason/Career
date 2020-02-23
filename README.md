# Career

## Introduction

Generate a tailored CV (resume) combinatorially using markdown.
If `N` is the number of keywords then there are potentially `2^N` variants.
e.g. if `N=5` then there are `2^5 = 32` potential variants.

## Getting ready

* Clone this project to a private repository.
* Create a branch in which to add your personal information to the body and template files.
* Set up Python 3.x

```
pip install markdown
```

## Usage

```
python cv.py everything
```

generates a new HTML file containing all the lines in the file body.md.
This is the type of output that I push directly to any jobs boards that I use.

```
python cv.py md python
```

generates a new HTML file containing the lines marked with the md and python keywords
plus the lines that have no braces at the end.

Edit template.html and body.md until the resulting file makes sense to you and your style.

When the tailored CV makes sense for a job application I print the HTML as a PDF file.
So I edit the HTML to remove all the green lines and may add extra HTML to ensure the page breaks look
correct.

```
<br/>
<p>&nbsp;</p>
```
