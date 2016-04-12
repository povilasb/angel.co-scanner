=====
About
=====

This is angel.co investors scraper.
It gets the investors social links.

Usage
=====

Scrape investors and save output to json formatted file::

    pyenv/bin/scrapy runspider angel_co_scraper/spiders.py -o investors.json

Requirements
============

* python 2.7

Setup
=====

Create python virtual environment::

    $ make pyenv

This command will download and install all project dependencies to `pyenv/`
directory.
