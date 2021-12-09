# gcode_stats_scraper

Scrapes estimated weight and print time from a folder of .gcode files and creates a CSV with the PR number and date.

PR number comes from the file name and can be ignored if wrong.

The date comes from the date the file was last modified, so can be innacurate if changes have been made. It works for my use case, however.

To use: Place in a folder containing the .gcode files to be scraped and run. Use the generated CSV as needed.
