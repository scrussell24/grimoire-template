# Grimoire Template

This repo is intended to be used as a template to create a [Grimoire](https://github.com/scrussell24/grimoire) project.


## Getting started

Start by using Github's "Use this template feature" to create your own repo from this one. Next,
clone your new repo and cd into the top-level directory.

### Install dependencies

Install the dependencies which is just the grimoire library. You likely want to create a Python
virtual environment before installing.

```
pip install -r requirements.txt
```

### Build you project

Build the default story.

```
python main.py
```

There you go. Your story has been build and the files should have been created in the
site/ directory. Load the index.html file in your browser.

### Make it your own

This template has three starting files that you can start editing to create your
own style.

#### app.py

The app.py file is where Grimoire's page functions are defined.

#### state.py

The state.py file is where your State model is defined.

#### template.py

The template.py file is where html temaplates are defined.

## Next Steps

To learn more about creating Grimoire stories check the [tutorial](https://scrussell24.github.io/grimoire/).
