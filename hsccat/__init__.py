import numpy as np


def get_mag(data, band="i"):
    """This utility gets the cmodel magnitude

    Args:
        data (ndarray):  Simulation or data
    """
    return data["%s_cmodel_mag" % band] - data["a_%s" % band]


def get_snr(data, band="i"):
    """This utility computes the S/N for each object in the data, based on
    cmodel_flux.

    Args:
        data (ndarray):  Simulation or data
    """
    if "snr" in data.dtype.names:
        return data["snr"]
    elif "%s_cmodel_fluxsigma" % band in data.dtype.names:  # s18
        snr = data["i_cmodel_flux"] / data["i_cmodel_fluxsigma"]
    elif "%sflux_cmodel" % band in data.dtype.names:  # s15
        snr = data["iflux_cmodel"] / data["iflux_cmodel_err"]
    elif "%s_cmodel_fluxerr" % band in data.dtype.names:  # s19
        snr = data["i_cmodel_flux"] / data["i_cmodel_fluxerr"]
    else:
        raise ValueError("Cannot derive SNR in %s band" % band)
    return snr


def get_log_blendness(data):
    """This utility gets the log of i-band blendedness, which quantify how much
    the galaxy is inflenced by blending

    Args:
        data (ndarray):  Simulation or data
    """
    if "logb" in data.dtype.names:
        logb = data["logb"]
    elif "base_Blendedness_abs" in data.dtype.names:  # pipe 7
        logb = np.log10(np.maximum(data["base_Blendedness_abs"], 1.0e-6))
    elif "i_blendedness_abs_flux" in data.dtype.names:  # s18
        logb = np.log10(np.maximum(data["i_blendedness_abs_flux"], 1.0e-6))
    elif "i_blendedness_abs" in data.dtype.names:  # s19
        logb = np.log10(np.maximum(data["i_blendedness_abs"], 1.0e-6))
    elif "iblendedness_abs_flux" in data.dtype.names:  # s15
        logb = np.log10(np.maximum(data["iblendedness_abs_flux"], 1.0e-6))
    else:
        raise ValueError(
            "Cannot derive the log of blendness from this data"
        )
    return logb


def get_inc_angle(data, psf_deconv=False):
    """This utility derives the inclination angle from the SDSS shape

    Args:
        data (ndarray):  Simulation or data
        psf_deconv (bool):  Whether removing PSF effect
    Returns:
        inc (ndarray):      galaxy's inclination angle in degrees
    """
    if not psf_deconv:
        xx = data['i_sdssshape_shape11']
        xy = data['i_sdssshape_shape12']
        yy = data['i_sdssshape_shape22']
    else:
        xx = data['i_sdssshape_shape11'] - data['i_sdssshape_psf_shape11']
        xy = data['i_sdssshape_shape12'] - data['i_sdssshape_psf_shape12']
        yy = data['i_sdssshape_shape22'] - data['i_sdssshape_psf_shape22']
    qmat = np.array(
        [[xx, xy],
         [xy, yy]]
    )
    qmat = np.moveaxis(qmat, -1, 0)
    ab = np.linalg.eigvals(qmat)
    rmax = np.max(ab, axis=-1)
    rmin = np.min(ab, axis=-1)
    inc = np.arccos(rmin / rmax)*180. / np.pi
    return inc


def get_sdss_resolution(data, band="i"):
    """This utility derives the galaxy resolution from a data from the
    second-order moment matrix.

    Args:
        data (ndarray):      Simulation or data
    Returns:
        resolution (ndarray):   galaxy's resolution
    """
    pn11 = "%s_sdssshape_psf_shape11" % band
    pn22 = "%s_sdssshape_psf_shape22" % band
    gn11 = "%s_sdssshape_shape11" % band
    gn22 = "%s_sdssshape_shape22" % band
    trace_psf = (data[pn11] + data[pn22])
    trace_obs = (data[gn11] + data[gn22])
    return 1. - trace_psf / trace_obs


def get_sdss_size(data, dtype="det"):
    """This utility gets the observed galaxy size from a data
    using the specified size definition from the second-order moments matrix.

    Args:
        data (ndarray):  Simulation or data
        dtype (str):        Type of psf size measurement in
                            ['trace', 'determin']
    Returns:
        size (ndarray):     galaxy size
    """
    if "base_SdssShape_xx" in data.dtype.names:  # pipe 7
        gal_mxx = data["base_SdssShape_xx"] * 0.168**2.0
        gal_myy = data["base_SdssShape_yy"] * 0.168**2.0
        gal_mxy = data["base_SdssShape_xy"] * 0.168**2.0
    elif "i_sdssshape_shape11" in data.dtype.names:  # s18 & s19
        gal_mxx = data["i_sdssshape_shape11"]
        gal_myy = data["i_sdssshape_shape22"]
        gal_mxy = data["i_sdssshape_shape12"]
    elif "ishape_sdss_ixx" in data.dtype.names:  # s15
        gal_mxx = data["ishape_sdss_ixx"]
        gal_myy = data["ishape_sdss_iyy"]
        gal_mxy = data["ishape_sdss_ixy"]
    else:
        raise ValueError("Cannot derive SDSS size")

    if dtype == "trace":
        size = np.sqrt(gal_mxx + gal_myy)
    elif dtype == "det":
        size = (gal_mxx * gal_myy - gal_mxy**2) ** (0.25)
    else:
        raise ValueError("Unknown PSF size type: %s" % dtype)
    return size
