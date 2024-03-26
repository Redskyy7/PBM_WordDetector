import numpy as np
from itertools import product

def _dilation(img, as_gray, sel):
    """Interface function to call erosion filter"""
    return apply_filter(_apply_dilation, img, as_gray, sel)

def _apply_dilation(neighbors, as_gray):
    """Modifies the current pixel value considering its neighbors
        and the dilation operation rules."""
    if not as_gray:
        if max(neighbors.ravel()) == 0:
            return 0
        return 1
    return max(neighbors.ravel())

def _erosion(img, as_gray, sel):
    """Interface function to call erosion filter"""
    return apply_filter(_apply_erosion, img, as_gray, sel)

def _apply_erosion(neighbors, as_gray):
    """Modifies the current pixel value considering its neighbors
        and the erosion operation rules."""
    if not as_gray:
        if max(neighbors.ravel()) == 1:
            if _selem_is_contained_in(neighbors):
                return 1
        return 0
    return min(neighbors.ravel())

def _opening(img, as_gray, sel):
    """Applies the opening operation"""
    eroded = _erosion(img, as_gray, sel)
    dilated = _dilation(eroded, as_gray, sel)
    return dilated

def _closing(img, as_gray, sel):
    """Applies the closing operation"""
    dilated = _dilation(img, as_gray, sel)
    return _erosion(dilated, as_gray, sel)



def _selem_is_contained_in(window):
    """Returns True if ee is contained in win. Otherwise, returns False"""        
    #selem_white_idx = np.where(_SELEM.flatten() == 1)[0]
    #selem_sum = np.sum(_SELEM)
    #win_sum = np.sum(np.take(window, selem_white_idx))
    #return True if win_sum == selem_sum else False

    idx_selem = np.where(_SELEM.ravel() == 1)[0]
    idx_win = np.where(window.ravel() == 1)[0]
    return set(idx_selem) <= set(idx_win)

def apply_filter(operation, img, as_gray, sel):
    """Applies a morphological operator to an image"""
    global _SELEM
    _SELEM = sel
    img = img if as_gray else apply_threshold(img)
    width, height = img.shape
    prod = product(range(width), range(height))
    img_result = np.zeros_like(img)
    radius = _SELEM.shape[0]
    pad_img = add_padding(img, radius)
    for i, j in prod:
        img_result[i, j] = process_pixel(i, j, operation, as_gray, pad_img)
    return img

def add_padding(img, radius):
    width, height = img.shape
    pad_img_shape = (width + radius - 1, height + radius - 1)
    pad_img = np.zeros(pad_img_shape, bool)
    pad_img[radius-2:(width + radius-2), radius-2:(height + radius-2)] = img
    return pad_img

def process_pixel(i, j, operation, as_gray, img):
    radius = _SELEM.shape[0]
    neighbors = img[i:i+radius, j:j+radius]
    if as_gray:
        neighbors = np.delete(neighbors.flatten(), radius+1)
    return operation(neighbors, as_gray)

def apply_threshold(img, threshold=.5):
    """Applies the given threshold to an image, converting it into black and white"""
    result = np.ones_like(img, dtype=bool)
    result[np.abs(img) <= threshold] = 0
    result[np.abs(img) > threshold] = 1
    return result

_OPS = {
    'er': _erosion,
    'di': _dilation,
}

def morph_filter(operator='er',
                 img=None,
                 sel=np.ones((3, 2), dtype=bool),
                 as_gray=False):
    """Allows to apply multiple morphological operations over an image"""
    return _OPS[operator](img, as_gray, sel)