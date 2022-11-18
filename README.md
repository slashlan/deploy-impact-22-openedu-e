# deploy-impact-22-openedu-e
Repository for Team openedu-e for deploy(impact) 2022


You are currently on the Free plan
You have used 1,225 of 1,000 successful credits this month on the Free plan
Renews on Fri, December 2, 2022.

Doc: 
https://www.scraperapi.com/

https://www.scraperapi.com/documentation/python/ 

Refine web search with advanced operators:
https://support.google.com/websearch/answer/2466433?visit_id=638043801751520505-2327133070&p=adv_operators&hl=en&rd=1


Scrapy Executor
This actor allows you to run web spiders written in Python and the Scrapy framework on the Apify platform. Executing a spider is as simple as copy-pasting your Scrapy code into the actor's input. For multi-file Scrapy spiders, see the bottom of this readme.
Please note that the actor is experimental and it might change in the future.


Input configuration
The actor has the following input options:

Scrapy code - Paste your Python source code with Scrapy into this field.
Proxy - Optionally, select a proxy to be used by the actor, in order to avoid IP address-based blocking by the target website. The actor automatically executes all the Scrapy's HTTP(S) requests through the proxy.
Storing data on Apify cloud
To store your Scrapy items in Apify's Dataset or Key-value store cloud storages, you can use the apify Python package. All the methods are available for actors running both locally as well as on the Apify platform.

First, import the package by adding the following command to the top of your source file:

##Usage
After installing scrapy (see the Dependencies section), simply run:

scrapy crawl vnexpress -o data/path-to-output.json 
to crawl the web pages.

The extracted data will be stored in the specified file path in a json format.


##Extracted Data
You can see the data scraped in data/vnexpress.json. This is the result of running with the default setting and the categories specified in crawler/vnexpress.py.

For each article, four fields were extracted:

category: the url which contains the category of the article, e.g. "https://vnexpress.net/y-kien/doi-song-p10". You should ignore the page number (p10) because as explaind below, the URL is not permanent and its content will change as vnexpress add more articles.
url: the url to the full article, you can visit this url to read or crawl the full content
title: the title of the article.
text: a short exceprt of the article.
Note that some of the fields may be empty.


Multi-file Scrapy spiders
If your Scrapy spider contains multiple source code or configuration files, or you want to configure Scrapy settings, pipelines or middlewares, you can download the source code of this actor, import your files into it and push it to the Apify cloud for execution.

Before you start, make sure you have Python development environment set up, and NPM and Apify CLI installed on your computer.

Here are instructions:

Clone the GitHub repository with the source code of this actor:
git clone https://github.com/apifytech/actor-scrapy-executor
Go to the repository directory and install NPM packages:
cd actor-scrapy-executor
npm install
Copy your spider(s) into the actor/spiders/ directory.
Make any necessary changes to files in the the actor/ directory, including items.py, middlewares.py, pipelines.py or settings.py.
Run the actor locally on your computer and test that it works:
apify run
If everything works fine, upload the actor to the Apify platform, so that you can run it in the cloud:
apify push
And that's it!

If you have any problem or anything does not work, please file an issue on GitHub.



Statistics
17 categories
18,452 articles
611,733 tokens (single words)



Customizations
Vnexpress organizes its contents into categories. Each category may have thousands of articles, organised into numbered pages. For example, for one of the travel categories, the first page is "https://vnexpress.net/du-lich/diem-den". Subsequent pages can be formed by adding a suffix of 'p' with the page number, such as "https://vnexpress.net/du-lich/diem-den-p100". Since the articles within a page are generated dynamically, you will likely get a different result when crawling the same page url (after certain period of time depending on the frequency of the update, which seems daily at least).

Categories
The categories can be customized by editting the crawler/vnexpress.py file. The categories that are currently there are for my personal purposes, you can replace with your own categories by visiting vnexpress.net.

Pages to crawl for each category
You can choose how many pages to crawl for each category by changing the pages parameter in the get_urls() method in the same file. The default is 30 pages. Each page contains 30 articles.



Dependencies
scrapy is the only dependency in this project. The official documentation page recommends installing the package using conda or miniconda.

Scrapy settings
The settings in spiders/settings.py works well for me, partly because vnexpress.net did not seem to be very strict against crawling. If they have more restrictions in the future, you may need to use proxies to avoid getting blocked.
