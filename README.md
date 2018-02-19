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

= Part 2: Model training pipeline =
== Questions and Answers ==

- How did you choose to load each batch of data asynchronously, and why did you choose that method? Were there other methods that you considered - what are the pros/cons of each?

If I have time, I would write the batch into a queue from one process and then read the batch from another process. 

- What kinds of error checking and/or safeguards, if any, did you build into this part of the pipeline to prevent the pipeline from crashing when run on thousands of studies?

I would implement another queue for batches that are under processing. The process needs to take the batch out of the queue to signify it has finished processing the batch. Otherwise, the batch will requeue into the work queue so that the next process will work on it.

- Did you change anything from the pipelines built in Parts 1 to better streamline the pipeline built in this part? If so, what? If not, is there anything that you can imagine changing in the future?

- How did you verify that the pipeline was working correctly?
To verify the pipeline is working correctly, we can implement a dummy model that only validate the batches of data it can see through. For example, how many batches of data it sees, compute some statistic of the data to see if it is aligned with the input data.

- Given the pipeline you have built, can you see any deficiencies that you would change if you had more time? If not, can you think of any improvements/enhancements to the pipeline that you could build in?