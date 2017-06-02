#!/bin/bash
scrapy runspider WebCameraXP.py 2>&1 | tee result.txt | grep "find a WebCameraXP without password" | tee openWebCameraXP.txt

