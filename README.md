= Part 1: Parse the DICOM images and Contour Files =
== Questions and Answers == 
- How did you verify that you are parsing the contours correctly?

I didn't do that in the exercise but if I do, I would check the the contour coordinates are within the image boundaries. Also the the first and last coordinates in the contour file should meet within 0.5.

- What changes did you make to the functions that we provided, if any, in order to integrate them into a production code base?

I did just some simple changes. For example, checking if the coordinates has 2 elements. Also in the parse_dicom_file, I change it to return the dicom data directly instead of a dictionary that contains that dicom data. The reason is that I don't see the usage of dictionary of a single element. 

- If the pipeline was going to be run on millions of images, and speed was paramount, how would you parallelize it to run as fast as possible?

In this case, I would use pyspark to execute the process_image function given the image_filepath and contour_filepath that could be reference a s3 location. 

- If this pipeline were parallelized, what kinds of error checking and/or safeguards, if any, would you add into the pipeline?

With the approach mentioned above, pyspark already guarantee fault-tolerance so retry on failure is done by the framework. 