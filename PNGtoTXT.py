from PIL import Image, ImageOps
from IPython.display import display

def convert_image_to_array(image, width, height):
    image = image.resize((width, height))
    image = image.convert('L')
    display(image)
    pixels = image.getdata()
    array_image = [[] for _ in range(height)]
    index = 0
    for i, pixel in enumerate(pixels):
        array_image[index].append(pixel)
        if (i+1)%width == 0:
            index+=1
    return array_image
def create_array_with_average(target_average, size):
    num_ones = int(size * target_average)
    num_zeros = size - num_ones
    array = '.' * num_ones + ' ' * num_zeros 
    return array
def convert_array_to_dots(pixels, ratio, width, height):
    ASCII_CHARS = create_array_with_average(ratio, 64)
    segment_size = (256 // (len(ASCII_CHARS))) + 1
    dot_image = [''] * height
    for i, pixel_list in enumerate(pixels):
        for pixel in pixel_list:
            dot_image[i]+= ASCII_CHARS[pixel // segment_size]
    return dot_image
def convert_2d(array_1d):
    """Convert a 1D array to 2D (array[x] => array[x][y])"""
    char_array = [[char for char in string.replace('\n', '')] for string in array_1d]
    return char_array
def fragment_array(array, w, h):
    """Fragments the 2D array into 2 x 4 arrays for the compression"""
    smaller_arrays = [] 
    for row in range(0, h, 4):
        for col in range(0, w, 2):
            smaller = []
            for i in range(4):
                smaller.append(array[row + i][col:col + 2])
            smaller_arrays.append(smaller)
    return smaller_arrays
def test_for_dots(char):
    if char == '.':
        return 1
    else:
        return 0
    
def compress_to_dots(section_str):
    """Has to be a 2 by 4 array"""
    compressed_value = [0,0,0,0,0,0,0,0]
#                      ⡿ ⢿ ⣟ ⣯⣷ ⣻⣽ ⣾
#                      7 6  5 43  21 0
    compressed_value[0] = test_for_dots(section_str[3][1])
    compressed_value[1] = test_for_dots(section_str[3][0])
    compressed_value[2] = test_for_dots(section_str[2][1])
    compressed_value[3] = test_for_dots(section_str[1][1])
    compressed_value[4] = test_for_dots(section_str[0][1])
    compressed_value[5] = test_for_dots(section_str[2][0])
    compressed_value[6] = test_for_dots(section_str[1][0])
    compressed_value[7] = test_for_dots(section_str[0][0])
    
    binary_string = ''.join(map(str, compressed_value))
    bin_value = int(binary_string,2)
    return_chr = chr(0x2800+(bin_value)) if bin_value > 0 else chr(0x2801) #'⡀' #0x2800 isn't the same size as ' '
    return return_chr
def compress_dot_image(dot_image, width, height):
    fragmented_arrays = fragment_array(convert_2d(dot_image), width, height)
    final_string = ""
    for idx, braille in enumerate(fragmented_arrays):
        final_string += compress_to_dots(braille)
        if (idx+1) % (width/2) == 0 and idx > 0:
            final_string += '\n'
    return final_string
def image_to_txt(image, width, height, ratio):
    pixels = convert_image_to_array(image, width, height)
    dot_image = convert_array_to_dots(pixels, ratio, width, height)
    final_string = compress_dot_image(dot_image, width, height)
    return final_string

# image = Image.open('Images/stick.jpg')
# height = 81
# width = 1.5*height
# height = int((height // 4) * 4)
# width = int((width // 2) * 2)
# print(image_to_txt(image, width, height, 0.37))

