SELECT
        object_id
      , f1.ra
      , f1.dec
      , f1.g_cmodel_flux
      , f1.g_cmodel_fluxerr
      , f1.r_cmodel_flux
      , f1.r_cmodel_fluxerr
      , f1.i_cmodel_flux
      , f1.i_cmodel_fluxerr
      , f1.z_cmodel_flux
      , f1.z_cmodel_fluxerr
      , f1.y_cmodel_flux
      , f1.y_cmodel_fluxerr
	  , f1.g_cmodel_mag
	  , f1.g_cmodel_magerr
	  , f1.r_cmodel_mag
	  , f1.r_cmodel_magerr
	  , f1.i_cmodel_mag
	  , f1.i_cmodel_magerr
	  , f1.z_cmodel_mag
	  , f1.z_cmodel_magerr
	  , f1.y_cmodel_mag
	  , f1.y_cmodel_magerr
      , f1.a_g
      , f1.a_r
      , f1.a_i
      , f1.a_z
      , f1.a_y
	  , f1.tract
	  , f1.patch
	  , f2.i_sdssshape_psf_shape11
	  , f2.i_sdssshape_psf_shape12
	  , f2.i_sdssshape_psf_shape22
	  , f2.i_sdssshape_shape11
	  , f2.i_sdssshape_shape11err
	  , f2.i_sdssshape_shape12
	  , f2.i_sdssshape_shape12err
	  , f2.i_sdssshape_shape22
	  , f2.i_sdssshape_shape22err
	  , m2.g_blendedness_abs
	  , m2.r_blendedness_abs
	  , m2.i_blendedness_abs
	  , m2.z_blendedness_abs
	  , m2.y_blendedness_abs
	  , pzm.photoz_best
	  , pzm.photoz_conf_best
	  , pzm.photoz_err68_max
	  , pzm.photoz_err68_min
	  , pzm.photoz_err95_max
	  , pzm.photoz_err95_min
	  , pzm.reduced_chisq
	  , pzm.sfr
	  , pzm.sfr_err68_max
	  , pzm.sfr_err68_min
	  , pzm.stellar_mass
	  , pzm.stellar_mass_err68_max
	  , pzm.stellar_mass_err68_min
    FROM
        pdr3_wide.forced as f1
        JOIN pdr3_wide.forced2 as f2 USING (object_id)
		JOIN pdr3_wide.masks as msk USING (object_id)
		JOIN pdr3_wide.photoz_mizuki as pzm USING (object_id)
		JOIN pdr3_wide.meas2 as m2 USING (object_id)
    WHERE
        isprimary
	AND i_extendedness_value >0
    AND NOT f2.g_sdsscentroid_flag
    AND NOT f2.r_sdsscentroid_flag
    AND NOT f2.i_sdsscentroid_flag
    AND NOT f2.z_sdsscentroid_flag
    AND NOT f2.y_sdsscentroid_flag
	AND NOT f2.g_sdssshape_flag
    AND NOT f2.r_sdssshape_flag
    AND NOT f2.i_sdssshape_flag
    AND NOT f2.z_sdssshape_flag
    AND NOT f2.y_sdssshape_flag
    AND NOT f1.g_pixelflags_edge
    AND NOT f1.r_pixelflags_edge
    AND NOT f1.i_pixelflags_edge
    AND NOT f1.z_pixelflags_edge
    AND NOT f1.y_pixelflags_edge
    AND NOT f1.g_pixelflags_interpolatedcenter /**/
    AND NOT f1.r_pixelflags_interpolatedcenter /**/
    AND NOT f1.i_pixelflags_interpolatedcenter /**/
    AND NOT f1.z_pixelflags_interpolatedcenter /**/
    AND NOT f1.y_pixelflags_interpolatedcenter /**/
    AND NOT f1.g_pixelflags_saturatedcenter
    AND NOT f1.r_pixelflags_saturatedcenter
    AND NOT f1.i_pixelflags_saturatedcenter
    AND NOT f1.z_pixelflags_saturatedcenter
    AND NOT f1.y_pixelflags_saturatedcenter
    AND NOT f1.g_pixelflags_crcenter /**/
    AND NOT f1.r_pixelflags_crcenter /**/
    AND NOT f1.i_pixelflags_crcenter /**/
    AND NOT f1.z_pixelflags_crcenter /**/
    AND NOT f1.y_pixelflags_crcenter /**/
    AND NOT f1.g_pixelflags_bad
    AND NOT f1.r_pixelflags_bad
    AND NOT f1.i_pixelflags_bad
    AND NOT f1.z_pixelflags_bad
    AND NOT f1.y_pixelflags_bad
    AND NOT f1.g_cmodel_flag
    AND NOT f1.r_cmodel_flag
    AND NOT f1.i_cmodel_flag
    AND NOT f1.z_cmodel_flag
    AND NOT f1.y_cmodel_flag
	AND NOT msk.g_mask_brightstar_any
	AND NOT msk.r_mask_brightstar_any
	AND NOT msk.i_mask_brightstar_any
	AND NOT msk.z_mask_brightstar_any
	AND NOT msk.y_mask_brightstar_any
    LIMIT 100
;
