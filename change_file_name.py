import glob
import shutil

# root_dir needs a trailing slash (i.e. /root/dir/)
root_dir = "./"
for file_type in ['**/*.pdf', '**/*.png', '**/*.svg']:
    for filename in glob.iglob(root_dir + file_type, recursive=True):
        filename_dash = filename.replace("figures_free_surface_identification_demonstration", "f0")
        filename_dash = filename_dash.replace("images_pst_free_surf_pst_free_surface", "im0")
        filename_dash = filename_dash.replace("figures_taylor_green_re", "f01")
        filename_dash = filename_dash.replace("figures_taylor_green_tg", "ft1")
        filename_dash = filename_dash.replace("figures_taylor_green_sun2019_corrections_test", "fs1")
        filename_dash = filename_dash.replace("figures_taylor_green_ipst_corrections_test", "fi1")
        filename_dash = filename_dash.replace("figures_cavity_sun2019_corrections_test", "f2")
        filename_dash = filename_dash.replace("figures_dam_break_2d_etvf_sun2019", "f3")
        filename_dash = filename_dash.replace("figures_oscillating_plate_gtvf", "f4")
        filename_dash = filename_dash.replace("figures_oscillating_plate_etvf_sun2019", "f5")
        filename_dash = filename_dash.replace("figures_oscillating_plate_large_deformation_ctvf", "f6")
        filename_dash = filename_dash.replace("images_uniaxial_compression", "im1")
        filename_dash = filename_dash.replace("figures_uniaxial_compression", "f7")
        filename_dash = filename_dash.replace("figures_rings_etvf_sun2019_poisson_ratio", "f8")
        filename_dash = filename_dash.replace("figures_rings_etvf_ipst_poisson_ratio", "f9")
        filename_dash = filename_dash.replace("figures_rings_sun_vs_ipst_vs_gray", "f10")
        filename_dash = filename_dash.replace("figures_high_velocity_impact_etvf_sun2019", "f11")

        print(filename_dash[2:])
        try:
            shutil.move(filename, filename_dash[2:])
        except shutil.SameFileError:
            pass
