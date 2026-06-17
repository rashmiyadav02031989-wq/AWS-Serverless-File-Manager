# AWS-Serverless-File-Manager
## Overview  
A serverless file management application that allows users to upload, list, download, and delete files through a web interface using Amazon S3, Lambda, API Gateway and pre-signed URLs.  
## Architecture  
```mermaid
flowchart TD
    U[User Browser] --> CF[CloudFront]
    CF --> S3F[S3 Frontend Bucket<br/>index.html]
    S3F --> APIGW[API Gateway]

    subgraph "Lambda Functions"
        direction LR
        UL[Upload Lambda]
        LL[List Lambda]
        DL[Delete Lambda]
    end

    APIGW --> UL
    APIGW --> LL
    APIGW --> DL

    S3D[S3 Files Bucket]

    UL --> S3D
    LL --> S3D
    DL --> S3D

    UL -. Pre-signed Upload URL .-> U
    LL -. Pre-signed Download URLs .-> U

    U -. Direct Upload/Download .-> S3D
```

## AWS Services Used:  
-Amazon Web Services  
-Amazon S3  
-AWS Lambda  
-Amazon API Gateway   
-Amazon CloudFront  

## Features:   
-Upload files using S3 pre-signed URLs  
-View uploaded files  
-Download files securely  
-Delete files  
-Responsive web interface  
-Fully serverless architecture  

## Implementation Steps:  
### Step1 :   
 Created an S3 bucket to store uploaded files and a separate S3 bucket to host the frontend.  
 ### Step 2:  
 Developed the frontend (`index.html`) for file upload, listing, download, and deletion.  
### Step 3:  
Created Lambda functions for generating pre-signed upload URLs, listing files with download URLs, and deleting files.  
### Step 4:  
Configured API Gateway routes and integrated them with the Lambda functions.  
### Step 5:  
Enabled CORS for seamless communication between the frontend and backend services.  
### Step 6:  
Deployed the frontend to S3 and configured CloudFront for secure content delivery.  
### Step 7:
Tested end-to-end functionality, including upload, download, list, and delete operations.  

## Security Best Practises:  
-Files are uploaded directly to S3 using time-limited pre-signed URLs.   
-CloudFront is used to securely distribute the frontend.  
-No long-term AWS credentials are exposed in the browser.  

## Screenshots:     
### Website Homepage

![Website Homepage](screenshots/website-homepage.png)

### File upload  

![File Upload](screenshots/file-upload.png)  

### Uploaded files list  

![Uploaded Files](screenshots/file-list.png)  

### Download functionality  

![Select File To Download](screenshots/file4-download.png)   

![Downloaded File](screenshots/file4-downloaded.png)  

### Delete functionality  

![Website Homepage](screenshots/file5-delete.png)  

![Website Homepage](screenshots/files-after-delete.png)  


