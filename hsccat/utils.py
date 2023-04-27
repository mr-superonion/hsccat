import numpy as np


def get_snr(catalog, band="i"):
    """This utility computes the S/N for each object in the catalog, based on
    cmodel_flux. It does not impose any cuts and returns NaNs for invalid S/N
    values.
    """
    if "snr" in catalog.dtype.names:
        return catalog["snr"]
    elif "%s_cmodel_fluxsigma" % band in catalog.dtype.names:  # s18
        snr = catalog["i_cmodel_flux"] / catalog["i_cmodel_fluxsigma"]
    elif "%sflux_cmodel" % band in catalog.dtype.names:  # s15
        snr = catalog["iflux_cmodel"] / catalog["iflux_cmodel_err"]
    elif "%s_cmodel_fluxerr" % band in catalog.dtype.names:  # s19
        snr = catalog["i_cmodel_flux"] / catalog["i_cmodel_fluxerr"]
    else:
        raise ValueError("Cannot derive SNR in %s band" % band)
    return snr


def get_sdss_inc_angle(catalog, psf_deconv=False):
    """This utility derives the inclination angle from the SDSS shape
    Args:
        catalog (ndarray):  Simulation or data catalog
        psf_deconv (bool):  Whether removing PSF effect
    Returns:
        inc (ndarray):      galaxy's inclination angle
    """
    # to be implement
    pass


def get_sdss_resolution(catalog):
    """This utility derives the galaxy resolution
    Args:
        catalog (ndarray):      Simulation or data catalog
    Returns:
        resolution (ndarray):   galaxy's resolution
    """
    # to be implement
    pass


def get_sdss_size(catalog, dtype="det"):
    """This utility gets the observed galaxy size from a data or sims catalog
    using the specified size definition from the second moments matrix.
    Args:
        catalog (ndarray):  Simulation or data catalog
        dtype (str):        Type of psf size measurement in
                            ['trace', 'determin']
    Returns:
        size (ndarray):     galaxy size
    """
    if "base_SdssShape_xx" in catalog.dtype.names:  # pipe 7
        gal_mxx = catalog["base_SdssShape_xx"] * 0.168**2.0
        gal_myy = catalog["base_SdssShape_yy"] * 0.168**2.0
        gal_mxy = catalog["base_SdssShape_xy"] * 0.168**2.0
    elif "i_sdssshape_shape11" in catalog.dtype.names:  # s18 & s19
        gal_mxx = catalog["i_sdssshape_shape11"]
        gal_myy = catalog["i_sdssshape_shape22"]
        gal_mxy = catalog["i_sdssshape_shape12"]
    elif "ishape_sdss_ixx" in catalog.dtype.names:  # s15
        gal_mxx = catalog["ishape_sdss_ixx"]
        gal_myy = catalog["ishape_sdss_iyy"]
        gal_mxy = catalog["ishape_sdss_ixy"]
    else:
        raise ValueError("Cannot derive SDSS size")

    if dtype == "trace":
        size = np.sqrt(gal_mxx + gal_myy)
    elif dtype == "det":
        size = (gal_mxx * gal_myy - gal_mxy**2) ** (0.25)
    else:
        raise ValueError("Unknown PSF size type: %s" % dtype)
    return size


def get_log_blendness(catalog):
    """Returns the log of i-band blendedness"""
    if "logb" in catalog.dtype.names:
        logb = catalog["logb"]
    elif "base_Blendedness_abs" in catalog.dtype.names:  # pipe 7
        logb = np.log10(np.maximum(catalog["base_Blendedness_abs"], 1.0e-6))
    elif "i_blendedness_abs_flux" in catalog.dtype.names:  # s18
        logb = np.log10(np.maximum(catalog["i_blendedness_abs_flux"], 1.0e-6))
    elif "i_blendedness_abs" in catalog.dtype.names:  # s19
        logb = np.log10(np.maximum(catalog["i_blendedness_abs"], 1.0e-6))
    elif "iblendedness_abs_flux" in catalog.dtype.names:  # s15
        logb = np.log10(np.maximum(catalog["iblendedness_abs_flux"], 1.0e-6))
    else:
        raise ValueError("Cannot derive the log of blendness from this catalog")
    return logb
