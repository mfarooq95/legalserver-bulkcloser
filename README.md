# 📁 LegalServer Bulk Case Closer
Close cases in bulk on your LegalServer site via the LegalServer API. You can review your API history in the Admin panel under *API Logs* and see the requests made in detail.

If your site uses an integration that relies on API calls as well, be aware of the rate limits LegalServer has of the standard 200 calls per minute. A high amont of calls to the API for a high volume of cases you'd like to close or update via PATCH or PUT reuqests can eat up the same call rates as your integration. ```time.sleep``` can help to alleviate this, but for best mesaures, run the code when office hours are closed, when the integration and your LegalServer site aren't making API calls with your source data for the import.

You can also repurpose the code to do more than close the case. Just rewrite the requests, the cases you're pulling from the report (and update the report to get the cases you'd like to work on), and hit it agian.

Refer to the LegalServer API docs for more information: https://www.apidocs.legalserver.org/.


## Requirements
### 📦 Libraries
1. ```requests```
2. ```time```

### 🌐 LegalServer
1. API v2 Access
2. API user with GET and PATCH permissions
3. Report returning cases you'd like to close en mass with the data field Globally Unique ID/UUID

   ❗️ This is known in LegalServer's reports as ```unique_id ["matter_5"."unique_id"``` and can be added to your report through: *Advanced Add Columns* -> *Case Data* -> *Fields* -> **Globally Unique ID**

## Setup
1. After downloading the code, add and import your API user's username and password into a ```.env``` file for security and import the ```username``` and ```password```

   ❗️ You can suplement Basic Auth with a Bearer Token setup if you perfer
2. Copy your report's url and API code from the report's page and use it for the ```url``` variable to get the cases you'd like to close via the report
   
   ❗️ Be sure to have *Use column headers as keys* enabeled in the XML/API settings on the report page to target the case's UUID via the label *Globally Unique ID*

   ❗️ Remember to set the Reports API return/response type to JSON instead of XML on the report page
   
3. Run code as is to close cases in mass

## Closing Thoughts
An actual logger like ```logging``` could be used to better log and track errors, issues, successes and information for the API calls as the code runs through the cases in the reports and closes each case

Using ```requests.Session()``` instead of ```requests.patch()``` can help to grealty speed up the calls to the LegalServer API, especially when working with a large amount of cases as auth can be the largest overhead when it comes to speedy setups
