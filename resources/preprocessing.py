def encode_pendapatan(pendapatan):
  return 0 if pendapatan == "rendah" else 1 if pendapatan == "sedang" else 2
def encode_usia(usia):
  return 0 if usia == "muda" else 1 if usia == "parobaya" else 2 if usia == "tua" else 3
def encode_tanggungan(tanggungan):
  return 0 if tanggungan == "sedikit" else 1 if tanggungan == "sedang" else 2
def encode_pengeluaran(pengeluaran):
  return 0 if pengeluaran == "rendah" else 1 if pengeluaran == "sedang" else 2
def encode_aset(aset):
  return 0 if aset == "sedikit" else 1 if aset == "sedang" else 2

def get_input(data):
  pendapatan  = float(data["pendapatan"])
  usia        = float(data["usia"])
  tanggungan  = float(data["tanggungan"])
  pengeluaran = float(data["pengeluaran"])
  aset        = float(data["aset"])
  return pendapatan, usia, tanggungan, pengeluaran, aset

def preprocessing(dataset):
  df = dataset.rename(columns={"pendapatan (jt/bln)": "pendapatan",
                          "usia (tahun)": "usia",
                          "tanggungan (orang)": "tanggungan",
                          "pengeluaran (jt/bln)": "pengeluaran",
                          "aset (juta)": "aset",
                          "kelayakan": "kelayakan"})

  df['pendapatan'] = df['pendapatan'].apply(encode_pendapatan)
  df['usia'] = df['usia'].apply(encode_usia)
  df['tanggungan'] = df['tanggungan'].apply(encode_tanggungan)
  df['pengeluaran'] = df['pengeluaran'].apply(encode_pengeluaran)
  df['aset'] = df['aset'].apply(encode_aset)
  return df.to_numpy()