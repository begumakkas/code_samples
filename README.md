# Code Samples

Two Python samples representing different parts of my recent work: backend/authentication logic and data linking/analysis.

## 1. `views.py` — InsightOut (Django backend)
Authentication logic I wrote for InsightOut, a tool that helps nonprofit staff 
identify beneficiary populations by geography using DHS survey data. I built 
the auth backend and most of the frontend for this production application.

Live site: https://insightout.civic.garden/

## 2. `index.py` — Green Space Accessibility in Chicago
A geospatial data-linking and scoring pipeline I built with three team members, to measure green space 
access for ~500 affordable housing units in Chicago. Combines spatial buffering 
and fuzzy name matching (Jaro-Winkler) to link park polygons to Yelp/Google 
review data, then computes a composite accessibility score weighted by park 
size and review quality.

Full project + repo: https://github.com/begumakkas/Green-Space-Access
