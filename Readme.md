# Dominant colour extractor
The objective of this project was to demonstrate the ability to isolate the dominant colours in an image.

# Import the libraries
import the basic libraries including matplotlib.pyplot and numpy. To extract the count, we will use Counter from the collections library. To use OpenCV, we will use cv2. KMeans algorithm is part of the sklearn's cluster subpackage.

# Determining the technique.
A statistical approach would have been a better approach to this problem however the drawbacks using traditional image processing techniques is that its either too rigid since those are rules based or too manually involved since the parameters of the rules (threshold values) are hard coded and hence have to be modified according to the use case scenario. Example would be histogram-frequency analysis which involves plotting the histogram of  the image intensities and then determining the histogram values using the frequency analysis of the pixels.
A more automated and less labour intensive approach is to use unsupervised machine learning.    
K-Means algorithm creates clusters based on the supplied count of clusters. In our case, it will form clusters of colors and these clusters will be our top colors. We then fit and predict on the same image to extract the prediction into the variable labels.

# Working
KMeans expects the input to be of two dimensions, so we use Numpy’s reshape function to reshape the image data.
although it is not required to resize it to a smaller size but we do so to lessen the pixels which’ll reduce the time needed to extract the colors from the image.
We use Counter to get count of all labels. To find the colors, we use clf.cluster_centers_. The ordered_colors iterates over the keys present in count, and then divides each value by 255. We could have directly divided each value by 255 but that would have disrupted the order.

##### Helper functions
 A function that will convert RGB to hex so that we can use them as labels for further processing.
On reading the color which is in RGB space, we return a string. {:02x} which simply displays the hex value for the respective color.

# Removing the neutral colors
 This was fairly straight forward since the extraction of the colors was done using K-Means clustering and the values can be easily iterated over using Counter methods.
 The filtering of neutral colors is a simple text based filtering which involves checking the clustered Hex values against a list of color values, if its true then that color is replaced with None.