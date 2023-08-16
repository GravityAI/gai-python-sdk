# GravityAiInferenceSDK Usage Guide

This guide offers a comprehensive view of utilizing the GravityAiInferenceSDK for engaging with the Gravity AI Inference API, encompassing a range of tasks including job submission on the Gravity AI platform, retrieval of job outcomes, modification of job names, and more.
## Prerequisites

Before you begin, make sure you have the following prerequisites:

- Python 3.8 or higher installed
- Gravity AI Inference SDK

## Installation

1. Clone or download the Gravity AI Inference SDK repository from [GitHub](https://github.com/GravityAI/gai-python-sdk).
2. Install the required packages using pip:

   ```bash
   pip install -r requirements.txt

## Getting Started
1. Import the necessary modules:

    ```bash
    from gravity_ai_inference_sdk.GravityInference import GravityAiInferenceSDK
    import requests

2. Provide your API key obtained from the Gravity AI Inference portal:

    ```bash
     API_KEY = "GAI-choooOfd.hQD8f44557txX677b84RRtV-gTko9kQ"

3. Create an instance of the GravityAiInferenceSDK class:
     ```bash
     gai = GravityAiInferenceSDK(API_KEY)

4. Specify Input and output paths:
    ```bash
    inputFilePath = "test.jpeg"
    outputFilePath = "out"

## Usage Examples

###   1. Getting Latest Jobs

Use the following method to retrieve the latest job information:
    ```bash

     gai.get_latest_jobs()

### 2. Posting a Job

You can post a job with the postJob method. Specify the inputFilePath parameter, and optionally provide name, version, and mimetype:

   ```bash
    jobId = gai.postJob(inputFilePath, name="Job1", version="0.0.1", mimetype="image/jpeg")
```

### 3. Downloading Result

To download the result of a job, use the downloadResultWithOutPath method:
     
     gai.downloadResultWithOutPath(jobId, outputFilePath)

### 4. Posting and Downloading Result Together
You can post a job and download the result in a single step using the getPostResult method. Specify the inputFilePath parameter, and optionally provide name, version, and mimetype:

```
 gai.getPostResult(inputFilePath, name="Job1", version=None, mimetype=None)
```

### 5. Getting Raw Job Result
Get job result in a raw format. Data is in the form of String, bytes etc.
```
 result = gai.getJobResult(jobId)
```
### 6. Changing Job Name
Change job name by passing API_KEY, and JobId of the job which is already present.
```
 Job_Name = "Job2"
 gai.changeJobName(API_KEY, jobId, Job_Name)
```

### 7. Posting Different Data Types
a. Text Data

Post a job with text data using the PostJobWithStringData method:
#### Example:
```
 data = " A man sitting on a chair."
 jobId = gai.PostJobWithStringData(data)
 gai.downloadResultWithOutPath(jobId, outputFilePath)
```
b. JSON Data

Post a job with JSON data using the PostJobWithJsonData method:
#### Example:
```
 data = 
  {
    "Source Language": "English",
    "Target Language": "Spanish",
    "Translation Text": "Hello, How are you?"
  }
 jobId = gai.PostJobWithJsonData(data)
 gai.downloadResultWithOutPath(jobId, outputFilePath)
```
c. Image Data

Create an image using any preferred library and post it as job input:

#### Example:

```
 from PIL import Image
 content = Image.new(mode="RGB", size=(200, 200), color=(153, 153, 255))
 
 jobId = gai.PostJobWithImageData(content)
 gai.downloadResultWithOutPath(jobId, outputFilePath)
```
d. Binary Data

Post a job with binary data from a zip file:

#### Example:
```
 with open("gravityAI.zip", "rb") as zip_file:
    content = zip_file.read()

 jobId = gai.PostJobWithBinaryData(content, "application/octet-stream")
 gai.downloadResultWithOutPath(jobId, outputFilePath)
```
## Conclusion

This guide provides an introduction to using the GravityAiInferenceSDK for interacting with the Gravity AI Inference API.
