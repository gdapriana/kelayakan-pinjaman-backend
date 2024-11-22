# Kelayakan Pinjaman
Menggunakan metode fuzzy tsukamoto.

| API | https://kelayakan-pinjaman-193ac292bee1.herokuapp.com/  |
|-----|---------------------------------------------------------|
|Colab| <a href="https://colab.research.google.com/drive/1P2qeWxOnwBv67Jkw47Z5kVm2ykOqkxY_?usp=sharing">Google Colab</a> |

## API Documentations
| <b>endpoint</b> | `API/predict`                                                                                          |
|-----------------|--------------------------------------------------------------------------------------------------------|
| method          | `POST`                                                                                                 |
| req body        | ```{ "pendapatan": float, "usia": float, "tanggungan": float, "pengeluaran": float, "aset": float }``` |
| res body        | ```{"result": float}```                                                                                |

| <b>endpoint</b> | `API/dataset`                                                                                                                                                                               |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| method          | `GET`                                                                                                                                                                                       |
| res body        | ```{"dataset": [{"aset (juta)": string, "kelayakan": string, "pendapatan (jt/bln)": string, "pengeluaran (jt/bln)": string, "tanggungan (orang)": string, "usia (tahun)": string}, ...]}``` |



