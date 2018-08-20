#For feedback = "This is an example feedback", and size = 8,
#the output should be

#feedbackReview(feedback, size) = ["This is",
#                                  "an",
#                                  "example",
#                                  "feedback"]

import textwrap

def feedbackReview(feedback, size):
    return textwrap.wrap(feedback, width = size)
