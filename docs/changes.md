## Main changes

- fixes to `extrude()` thanks to @JeffreyWardman
- filter out triangle strips in Ribbon and extrude()
- improvements in doc strings
- add `utils.madcad2vedo` conversion as per #976 by @JeffreyWardman
- add `utils.camera_to_dict()`
- add `Axes(title_backface_color=...)` keyword
- improvements on `plotter.__init__()`
- fix `labels()` and `labels2d()`
- add `shapes.plot_scalar()` plot a scalar along a line.
- add support for `tetgenpy`
- add `transformations.compute_main_axes()`
- add `transformations.__call__()` to apply it
- fix small bug in `pointcloud.distance_to()`
- add `applications.MorphPlotter()` to morph a polygonal mesh to a target mesh
- add `smooth_data()` to smooth/diffuse data attributes
- add `shapes.Tubes()`
- add `utils.Minimizer()` class
- add `CellCenters(Points)` class
- add `core.apply_transform_from_actor()`
- add `add volume.slab()`


## Breaking changes
- improvements to `shapes.Ellipsoid()` and bug fixes in #978 by @daniel-a-diaz
- improvements to `pointcloud.pca_ellipsoid()` and bug fixes
- improvements to `pointcloud.pca_ellipse()` and bug fixes
- change `clone2d(scale=...)` to `clone2d(size=...)`
- remove `shapes.StreamLines()` becoming `object.compute_streamlines()`
- split `mesh.decimate()` into `mesh.decimate()`, `mesh.decimate_pro()` and `mesh.decimate_binned()` as per #992


### Bug Fixes
- fix plotter `a` toggle
- fix viz on jupyter notebook as per #994


## New/Revised Examples
```
examples/advanced/warp4c.py
examples/advanced/diffuse_data.py
examples/volumetric/slab_vol.py
examples/volumetric/streamlines1.py
examples/volumetric/streamlines2.py
examples/volumetric/streamlines3.py
examples/volumetric/streamlines4.py
examples/volumetric/office.py
examples/simulations/mag_field1.py
examples/pyplot/plot_stream.py
examples/other/madcad1.py
examples/other/tetgen1.py
examples/other/nelder-mead.py

tests/issues/issue_968.py
tests/snippets/test_discourse_1956.py
tests/snippets/test_ellipsoid_main_axes.py
tests/snippets/test_compare_fit1.py
```

### Broken Examples
```
markpoint.py
cut_and_cap.py

gyroscope1.py broken physics
mousehover1.py (long indicator?)
mousehover2.py (unstable hovering?)
read_volume3.py interactor is lost

tests/issues/discussion_800.py
tests/issues/issue_905.py
```

#### Broken Projects
umap_viewer3d
trackviewer (some problems with removing a track, and z spacing)

#### Broken Exports to .npz:
boolean.py
cartoony.py
mesh_lut.py
mesh_map2cell.py
texturecubes.py
meshquality.py
streamlines1.py


