# 3D Shape Prediction by 2D Image Information 
The  following  Bachelor  Thesis covers  the  topic on  how  the  shape of  an  object can  be estimated based on 2D information, i.e. images, which is a difficult problem for machines. This work treats this problem in the specific case of reconstructing and estimating the shape and volume of red blood cells, based on single microscopic images. Therefore the goal of this thesis was to present a method on how this task can be fulfilled. The SHAPR-Framework provides an open-source package which can generate 3D cell predictions based on single cell images. Over 10’000 microscopic images, containing single red blood cells from a patient, have been used to make predictions. The results show that these predictions create realistic cell shapes and accurate  volume  estimations,  which  align with  the  true values  from  the blood sample. With the presented SHAPR-Framework, the diagnosis of home patients can be further enhanced. 

![Image](https://github.com/DominiquePeytrignet/BachelorThesis_DPeytrignet/blob/main/readme_image.png)

## Installation
To run this project, following Python libraries have to be installedwith the pip command:

- **shapr**: SHAPR Framework with the pip command "**pip install shapr**".
- **tensorflow**: Tensorflow library with the pip command "**pip install tensorflow**".
- **keras**: keras library with the pip command "**pip install keras**".
- **matplotlib**: matplotlib library with the pip command "**pip install matplotlib**".
- **numpy**: numpy library with the pip command "**pip install numpy**".
- **scikit-image**: scikit-image library with the pip command "**pip install scikit-image**".
- **scikit-learn**: scikit-learn library with the pip command "**pip install scikit-learn**".
- **tifffile**: tifffile library with the pip command "**pip install tifffile**".
- **scipy**: scipy library with the pip command "**pip install scipy**".
- **cv2**: OpenCV library with the pip command "**pip install cv2**".
- **PIL**: Pillow library with the pip command "**pip install Pillow**".
- **openpyxl**: Openpyxl library with the pip command "**pip install openpyxl**".
- **vedo**: Vedo library with the pip command "**pip install vedo**".

## Folder Structure
- The [Images_for_prediction](https://github.com/DominiquePeytrignet/BachelorThesis_DPeytrignet/tree/main/Images_for_prediction) folder is for storing the input image, from which the shape prediction is going to be made. These input images don't  have the required 64x64pixels format yet, are not in grayscale yet or both.
- The [Images](https://github.com/DominiquePeytrignet/BachelorThesis_DPeytrignet/tree/main/image) folder is used for storing the grayscale images which are preprocessed. Initially this folder can be empty.
- The[Mask](https://github.com/DominiquePeytrignet/BachelorThesis_DPeytrignet/tree/main/mask) folder is used for storing the binary segmentation of the RBC which are preprocessed. Initially this folder can be empty.
- The [Logs](https://github.com/DominiquePeytrignet/BachelorThesis_DPeytrignet/tree/main/logs) folder, the pre_trained model can be stored, which will perform the prediction. 
- In the [Results](https://github.com/DominiquePeytrignet/BachelorThesis_DPeytrignet/tree/main/Results) folder, the predictions are stored as tif-files.
- In the [Created_Images](https://github.com/DominiquePeytrignet/BachelorThesis_DPeytrignet/tree/main/Created_Images) folder, all the images are stored which are created during execution of the scripts.
- In the [Data_Analysis](https://github.com/DominiquePeytrignet/BachelorThesis_DPeytrignet/tree/main/Data_Analysis) folder,excel files are stored with the absorption imaging data, and data from the training set of SHAPR.
### Note, that it is important to not change the folder names. 



## Create Predictions
1. To create new predictions, paste the microscopic images in the [ImagesForPredictionFolder](https://github.com/DominiquePeytrignet/BachelorThesis_DPeytrignet/tree/main/Images_for_prediction)
2. If the images are not pre-processed yet, i.e. are not grayscaled, execute the [Extracting_Red_Channel](https://github.com/DominiquePeytrignet/BachelorThesis_DPeytrignet/blob/main/BTHE_Extracting_Red_Channel.ipynb) file to extract the red channel from the images and create grayscaled images. 
3. To resize the grayscaled images to the desired 64x64 pixel size, use the notebook [Altering_Images](https://github.com/DominiquePeytrignet/BachelorThesis_DPeytrignet/blob/main/BTHE_Altering_Images.ipynb)
4. To perform the predictions on the altered images, use the notebook [Applying_SHAPR](https://github.com/DominiquePeytrignet/BachelorThesis_DPeytrignet/blob/main/BTHE_Applying_SHAPR.ipynb), which applies the loaded pretrained weights from the logs folder on the images.
5. After the predictions have been stored in the results folder, their volume can be calculated by two different methods: [Manual_Thresholding](https://github.com/DominiquePeytrignet/BachelorThesis_DPeytrignet/blob/main/BTHE_Volume_Calculation_manualThresh.ipynb) and [bySHAPR](https://github.com/DominiquePeytrignet/BachelorThesis_DPeytrignet/blob/main/BTHE_Volume_Calculation_bySHAPR.ipynb)
6. To visualize specific results, in terms of a 3D mesh model, use the file [3D_Visualization](https://github.com/DominiquePeytrignet/BachelorThesis_DPeytrignet/blob/main/BTHE_3D_Visualization.py)

## Data Analysis
1. After the volumes have been stored in excel files, the data can be analysed by generating histograms with the notebooks [prediction_data](https://github.com/DominiquePeytrignet/BachelorThesis_DPeytrignet/blob/main/Data_Analysis/histogram_prediction_data.ipynb) and [normalization_data](https://github.com/DominiquePeytrignet/BachelorThesis_DPeytrignet/blob/main/Data_Analysis/Normalization_Comparison.ipynb)
2. Also the absorption analysis data, stored in an excel file, can be analyzed with the notebook [absorption_data](https://github.com/DominiquePeytrignet/BachelorThesis_DPeytrignet/blob/main/Data_Analysis/histogram_absorption_data.ipynb)
