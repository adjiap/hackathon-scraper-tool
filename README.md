# hacktahon-scraper-tool

 This tool is originally developed to crawl the www.hackathon.com website, specifically for scraping
 pages for the country, Germany.
 
 The information gathered will be processed to a CSV file which can then be used for trend searching
 for direction of new technologies.
 
 Prerequisite:
 * Python 3.7 or newer
 * Chrome version 79.0.3945.117 
 
 How to use: 
 1. Download from External repository to local folder
 2. Open the command line (e.g. Microsoft PowerShell) and go to tool folder.
 3. Run the following commands.
    ````
    pip setup.py install           # Installs dependencies in the site-packages
    python setup.py build_sphinx   # Creates HTML documentation in .\build
    ````
 4. Finally, in the same folder, enter the following to run the script.
    ````
    python crawl_url.py     # enter -h as options to see available crawl method
    # Example:
    # python crawl_url.py -y 2016 -c "united-kingdom"
    # # This crawls the hackathon website exclusively for the year 2016, and for the
    # # UK.
    ````