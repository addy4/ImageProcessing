## Author: Aadhaar Bhatia
## Created: 2019-06-17

# code for histogram(color matching) matching for RGB images
# cd <path of directory containing the file>
# octave
# run("histogram_matching.m")

function mosaicing

cd /Users/PremBhatia1/Desktop/picaz/random
pkg load image
im1_a = imread('small_src.jpg')
im2_a = imread('small_tar.jpg')
for_show = im1_a
im1 = im1_a
im2 = im2_a
#im1 as well as im1_a is the source image
im1_red = im1(:,:,1)
im1_green = im1(:,:,2)
im1_blue = im1(:,:,3)
#im2 as well as im2_a is the target image
im2_red = im2(:,:,1)
im2_green = im2(:,:,2)
im2_blue = im2(:,:,3)

pkg load image
hist1R = imhist(im1_red)
hist1G = imhist(im1_green)
hist1B = imhist(im1_blue)

hist2R = imhist(im2_red)
hist2G = imhist(im2_green)
hist2B = imhist(im2_blue)

cdf_1R = cumsum(hist1R)/numel(im1(:,:,1))
cdf_1G = cumsum(hist1G)/numel(im1(:,:,2))
cdf_1B = cumsum(hist1B)/numel(im1(:,:,3))

cdf_2R = cumsum(hist2R)/numel(im2(:,:,1))
cdf_2G = cumsum(hist2G)/numel(im2(:,:,2))
cdf_2B = cumsum(hist2B)/numel(im2(:,:,3))

for idx = 1 : 256
diff = abs(cdf_1R(idx)-cdf_2R)
[~,ind] = min(diff)
M(idx) = ind-1
endfor

for idx = 1 : 256
diff = abs(cdf_1G(idx)-cdf_2G)
[~,ind] = min(diff)
N(idx) = ind-1
endfor

for idx = 1 : 256
diff = abs(cdf_1B(idx)-cdf_2B)
[~,ind] = min(diff)
O(idx) = ind-1
endfor
out_imR = zeros(183,279)
out_imG = zeros(183,279)
out_imB = zeros(183,279)
out_imR = M(double(im1(:,:,1))+1)
out_imG = N(double(im1(:,:,2))+1)
out_imB = O(double(im1(:,:,3))+1)
for_show(:,:,1) = out_imR
for_show(:,:,2) = out_imG
for_show(:,:,3) = out_imB
subplot(2,3,1),imshow(im1);
title('Source Image');
subplot(2,3,2),imshow(im2);
title('Target Image');
subplot(2,3,3)
imshow(for_show);
title('Source matched to Target');
subplot(2,3,4),imhist(im1(:,:,1));
title('Histogram of Source');
subplot(2,3,5),imhist(im2(:,:,1));
title('Histogram of Target');
subplot(2,3,6),imhist(for_show(:,:,1));
title('Histogram of - Source matched with target');

