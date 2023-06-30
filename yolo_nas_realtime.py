from ultralytics import NAS
model = NAS('yolo_nas_s.pt')
model.predict(0,show=True)

@misc{supergradients,
  doi = {10.5281/ZENODO.7789328},
  url = {https://zenodo.org/record/7789328},
  author = {Aharon,  Shay and {Louis-Dupont} and {Ofri Masad} and Yurkova,  Kate and {Lotem Fridman} and {Lkdci} and Khvedchenya,  Eugene and Rubin,  Ran and Bagrov,  Natan and Tymchenko,  Borys and Keren,  Tomer and Zhilko,  Alexander and {Eran-Deci}},
  title = {Super-Gradients},
  publisher = {GitHub},
  journal = {GitHub repository},
  year = {2021},
}
