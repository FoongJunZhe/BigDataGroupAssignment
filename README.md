# AWS Hadoop Streaming Comparative Analysis Resarch 
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
The Amazon Athena SQL script defines the steps to create and manage an external table for analyzing Apache access logs stored in an S3 bucket. Using a RegexSerDe, the script parses log fields such as IP address, request time, HTTP method, requested URL, status code, and user agent. Subsequent queries are designed to:

* Validate parsed data.
* Identify the most requested URLs
* Summarize HTTP response code frequencies
* Count requests by IP address.
* Detect all HTTP 404 “Not Found” errors.

## Big Data Controller Log
The controller log records the orchestration of a Hadoop streaming job on AWS EMR. The job uses Python scripts (mapper.py and reducer.py) stored on S3 to process data from an S3 input location and output results back to S3. The environment configuration, EMR step ID, and command execution details are captured, confirming successful completion of the step within 294 seconds.

## Big Data Hadoop MapReduce System Log
This system log provides a detailed account of the MapReduce job execution. It records connections to the YARN ResourceManager and Application History Server, file access from S3, and the job submission process. Progress is tracked for the map and reduce phases, culminating in successful job completion. Performance metrics are provided, including:

* Map input records: 10,365,152
* Reduce output records: 258,606
* Total bytes read from S3: 3,502,850,345 bytes
* Total bytes written to S3: 4,159,283 bytes
* Memory and CPU usage statistics.

## Query CSV and pictures
The CSV result files contain the output of Athena queries, and the accompanying PNG files document the steps taken and resources used during query execution. These artifacts collectively represent both the input–output relationship and the execution plan for the analytical tasks.

## Mapper and Reducer Python File
This Python script serves as the Mapper in the MapReduce process. It reads each line from standard input, uses a regular expression to extract the client’s IP address from the log entry, and outputs it as a key-value pair in the format:

* <IP_Address>    1

This output indicates that the IP address was observed once in the processed log line. The tab-separated format is essential for Hadoop Streaming to correctly parse the mapper output for the reducer.

This script functions as the Reducer. It reads the tab-separated key-value pairs produced by the mapper, aggregates the counts for each unique IP address, and outputs the final tally in the format:

* <IP_Address>    <Total_Count>

The reducer assumes that the input is sorted by IP address (as ensured by the Hadoop framework) and accumulates counts until a new IP address is encountered.

## MapReduce result file
This file represents the output of the Hadoop Streaming job. It contains the final aggregated results from the reducer, listing each unique IP address alongside the total number of times it appears in the dataset. This output is the primary result of the analysis and can be further processed or visualized for insights such as identifying the most frequent visitors to a website or detecting abnormal traffic patterns.
