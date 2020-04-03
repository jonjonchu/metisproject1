{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# WTWY Street Team Placement\n",
    "This is the first project for the [Metis Data Science Bootcamp](www.thisismetis.com/), where we perform Exploratory Data Analysis (EDA)\ton the [MTA turnstiles data](http://web.mta.info/developers/turnstile.html).\n",
    "\n",
    "\n",
    "## Context\n",
    "WomenTechWomenYes (WTWY) hosts an annual gala during the summer. To drive attendance, their Street team goes to subway stations in NYC to attract people to sign up for the gala.\n",
    "\n",
    "## Goal\n",
    "Provide recommendations on how WTWY csm optimize the placement of their Street teams in NYC subway stations, such that they can gather the most amount of signups.\n",
    "\n",
    "\n",
    "## Methodologies\n",
    "\n",
    "**1. Obtaining data:** We downloaded the [NYC MTA turnstile data](http://web.mta.info/developers/turnstile.html) of June 2019 to obtain the daily entries of people passing through the turnstiles at all stations in NYC. \n",
    "\n",
    "**2. Cleaning data:** \n",
    "  - Fixing errors: We corrected the turnstile entries' values where the entries were logging backwards. \n",
    "  - Removing outliers: We removed entries that are outside of 3 standard deviations. \n",
    "  - Creating the desired data fields: We calculated the entries through each turnstiles by day and by 4-hour interval\n",
    " \n",
    "**3. Exploring data:** We created charts of top stations with the most foot traffic, broken down by day and 4-hour intervals.\n",
    "\n",
    "\n",
    "## Deliverable\n",
    "- [EDA](https://github.com/jonjonchu/metisproject1/blob/master/MTA_explore.ipynb)\n",
    "- [Python module](https://github.com/jonjonchu/metisproject1/blob/master/processTurnstiles.py)\n",
    "- [Presentation Slide](https://docs.google.com/presentation/d/1o4LMUoB8UgBTKi94WQQGkFYQwB9G9XkK5VzDE4sA8vE/edit#slide=id.g82d315d2f9_3_263)\n",
    "\n",
    "\n",
    "## Project Team\n",
    "* [Andy Tan](https://github.com/github/enndy6285)\n",
    "* [Jenny Wang](https://github.com/hellojenny) \n",
    "* [Jon Chu](https://github.com/jonjonchu)\n",
    "\n",
    "\n",
    "## Additional Information\n",
    "### Methods Used\n",
    "* Exploratory Data Analysis\n",
    "* Data Visualization\n",
    "\n",
    "### Technologies Used\n",
    "* Jupyter Notebook\n",
    "* Python\n",
    "* Pandas\n",
    "* Numpy\n",
    "* Matplotlib\n",
    "* seaborn"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
