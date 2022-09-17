[![Python application test with Github Actions](https://github.com/nogibjj/abzdel_project1/actions/workflows/pylint.yml/badge.svg)](https://github.com/nogibjj/abzdel_project1/actions/workflows/pylint.yml)

## Architectural Diagram
![ids706_project1 drawio](https://user-images.githubusercontent.com/55398496/190877160-cef690da-7588-4fea-9f46-5582ff5ab9a8.png)

## Key Objectives of this Project

- The main goal is to **build a Python microservice that connects directly to Azure Databricks** through an API.
- I have built a tool that uses the [Fortune 1000 dataset from Kaggle](https://www.kaggle.com/datasets/surajjha101/fortune-top-1000-companies-by-revenue-2022).
  - To run this project yourself, you simply need to download this data and put it into Databricks (naming the table fortune_1000, and ensuring correct data types)
- The user of the tool enters a **rank between 1-1000**, and the program returns the **company associated with that rank**.
- This is quite a simple tool that returns a simple payload. However, this demonstrates my ability to speak directly to Azure Databricks, perform a query **customized by the user in the command line**, and return an associated output.

## Setup Authentication

- [Place in Codespace Secrets](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/python-api#unixlinuxandmacos)

~~~
DATABRICKS_HOST
DATABRICKS_HTTP_PATH
DATABRICKS_SERVER_HOSTNAME
DATABRICKS_TOKEN
~~~

## Test out the CLI

~~~
databricks clusters list --output JSON | jq </br>
databricks fs ls dbfs:/ </br>
databricks jobs list --output JSON | jq </br>
~~~

## Remote Connect
  [Help can be found here](https://docs.databricks.com/dev-tools/databricks-connect.html)
  
  
## Example

~~~
dblib/cli_extension.py rank-query --rank 3
~~~
The above utilizes our rank-query command. Utilizing --rank 3 requests that we return the **third ranked company on the Fortune 1000 list**

~~~
Apple is rank 3 in our dataset.
~~~

This code is also fairly robust, and will only accept integer values as an input to --rank.


 
