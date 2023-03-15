# import os
import shutil


files = {
    # figure 1
    "./figures/free_surface_identification_demonstration/circle_geometry_normals.png": "fig_1_a.png",
    "./figures/free_surface_identification_demonstration/circle_geometry.png": "fig_1_b.png",

    # figure 2
    "./figures/free_surface_identification_demonstration/circle_with_boundary_normals.png": "fig_2_a.png",
    "./figures/free_surface_identification_demonstration/circle_with_boundary.png": "fig_2_b.png",

    # figure 3
    "./figures/free_surface_identification_demonstration/normals_dam_break_final_zoomed.png": "fig_3.png",

    # figure 4
    "./figures/free_surface_identification_demonstration/boundary_particles_final_zoomed.png": "fig_4.png",

    # figure 5
    "./images/pst_free_surf/pst_free_surface.png": "fig_5_a.png",
    "./images/pst_free_surf/pst_free_surface_zoomed.png": "fig_5_b.png",

    # figure 6
    "./figures/taylor_green/tg_decay.pdf": "fig_6_a.pdf",
    "./figures/taylor_green/tg_l1.pdf": "fig_6_b.pdf",

    # figure 7
    "./figures/taylor_green/tg_decay_ipst.pdf": "fig_7_a.pdf",
    "./figures/taylor_green/tg_l1_ipst.pdf": "fig_7_b.pdf",

    # figure 8
    "./figures/taylor_green_re_1000/tg_decay_ipst.pdf": "fig_8_a.pdf",
    "./figures/taylor_green_re_1000/tg_l1_ipst.pdf": "fig_8_b.pdf",

    # figure 9
    "./figures/taylor_green_re_1000/tg_decay.pdf": "fig_9_a.pdf",
    "./figures/taylor_green_re_1000/tg_l1.pdf": "fig_9_b.pdf",

    # figure 10
    "./figures/taylor_green_sun2019_corrections_test/tg_l1_re_100.pdf": "fig_10_a.pdf",
    "./figures/taylor_green_sun2019_corrections_test/tg_l1_re_1000.pdf": "fig_10_b.pdf",

    # figure 11
    "./figures/taylor_green_ipst_corrections_test/tg_l1_re_100.pdf": "fig_11_a.pdf",
    "./figures/taylor_green_ipst_corrections_test/tg_l1_re_1000.pdf": "fig_11_b.pdf",

    # figure 12
    "./figures/taylor_green_re_1000/tg_pplot_p_re_1000.pdf": "fig_12.pdf",

    # figure 13
    "./figures/cavity_sun2019_corrections_test/good_vs_bad.pdf": "fig_13.pdf",

    # figure 14
    "./figures/cavity/uv_re100.pdf": "fig_14.pdf",

    # figure 15
    "./figures/cavity/uv_re1000.pdf": "fig_15.pdf",

    # figure 16
    "./figures/dam_break_2d/etvf_sun2019/x_vs_t.png": "fig_16.png",

    # figure 17
    "./figures/dam_break_2d/db2d_vmag.pdf": "fig_17.pdf",


    # figure 18
    "./figures/oscillating_plate_gtvf/gtvf_original.pdf": "fig_18_a.pdf",
    "./figures/oscillating_plate/gtvf_sun2019.pdf": "fig_18_b.pdf",

    # figure 19
    "./figures/oscillating_plate/etvf_sun2019_l_0_2_h_0_02.pdf": "fig_19.pdf",

    # figure 20
    "./figures/oscillating_plate/etvf_sun2019_l_0_2_h_0_01.pdf": "fig_20.pdf",

    # figure 21
    "./figures/oscillating_plate_large_deformation/ctvf_ipst.pdf": "fig_21.pdf",

    # figure 22
    "./figures/oscillating_plate/ipst_convergence_plot.pdf": "fig_22.pdf",


    # figure 23
    "./images/uniaxial_compression/uniaxial_compression.png": "fig_23.png",

    # figure 24
    "./figures/uniaxial_compression/von_mises_A.pdf": "fig_24.pdf",

    # figure 25
    "./figures/rings/etvf_sun2019_poisson_ratio_0.3975/time1.png": "fig_25_a.png",

    "./figures/rings/etvf_sun2019_poisson_ratio_0.3975/time2.png": "fig_25_b.png",

    "./figures/rings/etvf_sun2019_poisson_ratio_0.3975/time3.png": "fig_25_c.png",

    "./figures/rings/etvf_sun2019_poisson_ratio_0.3975/time4.png": "fig_25_d.png",

    # figure 26
    "./figures/rings/etvf_sun2019_poisson_ratio_0.47/time1.png": "fig_26_a.png",

    "./figures/rings/etvf_sun2019_poisson_ratio_0.47/time2.png": "fig_26_b.png",

    "./figures/rings/etvf_sun2019_poisson_ratio_0.47/time3.png": "fig_26_c.png",

    "./figures/rings/etvf_sun2019_poisson_ratio_0.47/time4.png": "fig_26_d.png",


    # figure 27
    "./figures/rings/etvf_ipst_poisson_ratio_0.47/time1.png": "fig_27_a.png",

    "./figures/rings/etvf_ipst_poisson_ratio_0.47/time2.png": "fig_27_b.png",

    "./figures/rings/etvf_ipst_poisson_ratio_0.47/time3.png": "fig_27_c.png",

    "./figures/rings/etvf_ipst_poisson_ratio_0.47/time4.png": "fig_27_d.png",

    # figure 28
    "./images/rings/rings_initial.png": "fig_28.png",

    # figure 29
    "./figures/rings/sun_vs_ipst_vs_gray_a_b_0_3975_x.pdf": "fig_29_a.pdf",
    "./figures/rings/sun_vs_ipst_vs_gray_a_b_0_3975_y.pdf": "fig_29_b.pdf",

    # figure 30
    "./figures/high_velocity_impact/etvf_sun2019/time0.png": "fig_30_a.png",

    "./figures/high_velocity_impact/etvf_sun2019/time1.png": "fig_30_b.png",

    "./figures/high_velocity_impact/etvf_sun2019/time2.png": "fig_30_c.png",

    "./figures/high_velocity_impact/etvf_sun2019/time3.png": "fig_30_d.png",

    "./figures/high_velocity_impact/etvf_sun2019/time4.png": "fig_30_e.png",

    "./figures/high_velocity_impact/etvf_sun2019/time5.png": "fig_30_f.png",

    "./figures/high_velocity_impact/etvf_sun2019/time6.png": "fig_30_g.png",

    "./figures/high_velocity_impact/etvf_sun2019/time7.png": "fig_30_h.png",

    "./figures/high_velocity_impact/etvf_sun2019/time8.png": "fig_30_i.png",
}

for before, after in files.items():
    shutil.copy(before, after)
