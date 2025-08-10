# BigDataGroupAssignment
Big Data Group Assignment dataset and relevant files

Dataset source:
https://www.kaggle.com/datasets/eliasdabbas/web-server-access-logs

## Table 1. Dataset Descriptions

| Field Name                          | Description                                                                                              | Example                                                                                                          |
|--------------------------------------|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| IP Address                           | The public IP address of the client making the request to the web server.                                | 178.253.33.51                                                                                                    |
| Timestamp                            | The exact date and time when the request occurred.                                                       | [22/Jan/2019:03:56:19 +0330]                                                                                     |
| HTTP Method                          | The type of HTTP request made by the client, typically GET or POST.                                      | GET                                                                                                              |
| Requested URL                        | The specific resource or endpoint requested from the website.                                            | /m/product/32574/62991/...                                                                                       |
| HTTP Protocol                        | The version of HTTP used by the client.                                                                  | HTTP/1.1                                                                                                         |
| Status Code                          | The HTTP response code returned by the server.                                                           | 200                                                                                                              |
| Response Size                        | The number of bytes sent in the response body.                                                           | 20406                                                                                                            |
| Referrer URL                         | The webpage the client came from before making this request. May be "-" if not available.                | https://www.zanbil.ir/m/filter/...                                                                               |
| User Agent                           | Information about the client’s browser, operating system, or bot.                                        | Mozilla/5.0 (Linux; Android 5.1; HTC Desire 728 dual sim)...                                                      |
| Remote Logname / Authenticated User  | Placeholder fields in Apache logs; often unused and appear as hyphens “-“.                               | -                                                                                                                |


## Amazon Athena Codes
Consists of the codes ran in Amazon Athena

## Big Data Controller Log
Controller log for MapReduce job

## Big Data Hadoop MapReduce System Log
System log for MapReduce job

## Big Data Controller Log
Controller log for MapReduce job

## Query CSV and pictures
Results for the query including the resources, time ran and query results

## Mapper and Reducer Python File
Python script for the MapReduce job

## MapReduce result file
Consists of total ping request of each IP address within the dataset
