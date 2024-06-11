close all;
clear all;

inputImage = imread('Number Plate Images/images.jpg');
grayscaleImage = rgb2gray(inputImage);
binaryImage = imbinarize(grayscaleImage);
edgeImage = edge(grayscaleImage, 'prewitt');

regionProps = regionprops(edgeImage, 'BoundingBox', 'Area', 'Image');
numberOfRegions = numel(regionProps);

maxArea = 0;
numberPlateBoundingBox = [];

for i = 1:numberOfRegions
   if regionProps(i).Area > maxArea
       maxArea = regionProps(i).Area;
       numberPlateBoundingBox = regionProps(i).BoundingBox;
   end
end    

croppedNumberPlateImage = imcrop(binaryImage, numberPlateBoundingBox);
cleanedNumberPlateImage = bwareaopen(~croppedNumberPlateImage, 500);

[imageHeight, imageWidth] = size(cleanedNumberPlateImage);
imshow(cleanedNumberPlateImage);

letterRegionProps = regionprops(cleanedNumberPlateImage, 'BoundingBox', 'Area', 'Image');
numberOfLetters = numel(letterRegionProps);

detectedNumberPlate = [];

for i = 1:numberOfLetters
   letterWidth = length(letterRegionProps(i).Image(1,:));
   letterHeight = length(letterRegionProps(i).Image(:,1));
   
   if letterWidth < (imageHeight / 2) && letterHeight > (imageHeight / 3)
       recognizedLetter = readLetter(letterRegionProps(i).Image); % Ensure the function name matches
       detectedNumberPlate = [detectedNumberPlate recognizedLetter];
   end
end

disp(['Detected Number Plate: ', detectedNumberPlate]);

